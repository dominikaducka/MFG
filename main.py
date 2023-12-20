import csv
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta

email = "d.ducka@benefitsystems.pl"
input_csv_file = 'migration_plan.txt'

def generate_migration_files(input_csv):
#   Create main migration folder
   def generate_folders():
      main_folder = "Migracje"
      os.makedirs(main_folder, exist_ok=True)

#   Create migration date folder for each month
      migration_month_folder = os.path.join(main_folder, f"{migration_date}")
      os.makedirs(migration_month_folder, exist_ok=True)

#   Create a folder for each company
      company_folder = os.path.join(migration_month_folder, f"{company_name}")
      os.makedirs(company_folder, exist_ok=True)
      return company_folder

#creates configuration files: 
   def generate_files(company_folder):
      RRU_RRK_1_file = os.path.join(company_folder, f"RRU_RRK_1_{company_name}.csv")
      with open(RRU_RRK_1_file, 'w', newline='', encoding='utf-8') as RRU_RRK_1_file:
         writer = csv.writer(RRU_RRK_1_file, delimiter=',')
         writer.writerow(['RUNNER ID', 'MyB NIP', 'EMS NIP', 'Report type', 'Emails'])
         writer.writerow([runner_id, nip_1, nip_2, '1', email])

      RRU_RRK_2_file = os.path.join(company_folder, f"RRU_RRK_2_{company_name}.csv")
      with open(RRU_RRK_2_file, 'w', newline='', encoding='utf-8') as RRU_RRK_2_file:
         writer = csv.writer(RRU_RRK_2_file, delimiter=',')
         writer.writerow(['RUNNER ID', 'MyB NIP', 'EMS NIP', 'Report type', 'Emails'])
         writer.writerow([runner_id, nip_1, nip_2, '2', email])

      migration_lvl_1_file = os.path.join(company_folder, f"migration_lvl_1_{company_name}.csv")
      with open(migration_lvl_1_file, 'w', newline='', encoding='utf-8') as migration_lvl_1_file:
         writer = csv.writer(migration_lvl_1_file, delimiter=',')
         writer.writerow(['RUNNER ID', 'MyB NIP', 'EMS NIP', 'Emails'])
         writer.writerow([runner_id, nip_1, nip_2, email])

      date_format = "%m.%Y" #
      date_format_2 = "%Y-%m-%d"
      date_object = datetime.strptime(migration_date, date_format)
      date_2_object = date_object + relativedelta(months=1)
      date_3_object = date_object.replace(day=1)
      date_4_object = date_2_object.replace(day=1)
      date_1 = migration_date
      date_2 = date_2_object.strftime(date_format)
      date_3 = date_3_object.strftime(date_format_2)
      date_4 = date_4_object.strftime(date_format_2)

      migration_lvl_2_1_file = os.path.join(company_folder, f"migration_lvl_2_{date_1}_{company_name}.csv")
      with open(migration_lvl_2_1_file, 'w', newline='', encoding='utf-8') as migration_lvl_2_1_file:
         writer = csv.writer(migration_lvl_2_1_file, delimiter=',')
         writer.writerow([runner_id, date_3, email])

      migration_lvl_2_2_file = os.path.join(company_folder, f"migration_lvl_2_{date_2}_{company_name}.csv")
      with open(migration_lvl_2_2_file, 'w', newline='', encoding='utf-8') as migration_lvl_2_2_file:
         writer = csv.writer(migration_lvl_2_2_file, delimiter=',')
         writer.writerow([runner_id, date_4, email])

      migration_lvl_3_file = os.path.join(company_folder, f"migration_lvl_3_{company_name}.csv")
      with open(migration_lvl_3_file, 'w', newline='', encoding='utf-8') as migration_lvl_3_file:
         writer = csv.writer(migration_lvl_3_file, delimiter=',')
         writer.writerow(['RUNNER ID', 'MyB NIP', 'EMS NIP', 'Emails'])
         writer.writerow([runner_id, nip_1, nip_2, email])

# creates reports folders
   def generate_repors_folders(company_folder):
      report_names = ["RRU_RRK_1", "RRU_RRK_2", "lvl_1", "lvl_2.1", "lvl_2.2"]
      reports_folder = os.path.join(company_folder, "reports")
      os.makedirs(reports_folder, exist_ok=True)

      for report_name in report_names:
         folder_path = os.path.join(reports_folder, report_name)
         os.makedirs(folder_path, exist_ok=True)

# Function reads the original CSV file, each row as a dictionary
   with open(input_csv, 'r', newline='', encoding='utf-8') as csvfile:
      reader = csv.DictReader(csvfile)

#   then iterates through each row, extracts the company name, NIP number, migration date
      for row in reader:
         company_name = row['company_name']
         runner_id = row['runner_id']
         nip_1 = row['nip_1']
         nip_2 = row['nip_2']
         migration_date = row['migration_date']

         company_folder = generate_folders()
         generate_files(company_folder)
         generate_repors_folders(company_folder)

if __name__ == "__main__":
    generate_migration_files(input_csv_file)