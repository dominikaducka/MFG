import csv
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta

email = "d.ducka@benefitsystems.pl"

def create_company_files(input_csv):
#   Function reads the original CSV file, each row as a dictionary
    with open(input_csv, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

#   then iterates through each row, extracts the company name, NIP number, migration date
        for row in reader:
            company_name = row['company_name']
            runner_id = row['runner_id']
            nip_1 = row['nip_1']
            nip_2 = row['nip_2']
            migration_date = row['migration_date']

#   Create main migration folder
            main_folder = "Migracje"
            os.makedirs(main_folder, exist_ok=True)

#   Create migration date folder for each month
            migration_month_folder = os.path.join(main_folder, f"{migration_date}")
            os.makedirs(migration_month_folder, exist_ok=True)

#   Create a folder for each company
            company_folder = os.path.join(migration_month_folder, f"{company_name}")
            os.makedirs(company_folder, exist_ok=True)

  #For each company, it creates all configuration files for migration with separate foler for reports 
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

            date_format = "%m.%Y"
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

            reports_folder = os.path.join(company_folder, "reports")
            os.makedirs(reports_folder, exist_ok=True)

            RRU_RRK_1_folder = os.path.join(reports_folder, "RRU_RRK_1")
            os.makedirs(RRU_RRK_1_folder, exist_ok=True)

            RRU_RRK_2_folder = os.path.join(reports_folder, "RRU_RRK_2")
            os.makedirs(RRU_RRK_2_folder, exist_ok=True)

            migration_1_lvl_folder = os.path.join(reports_folder, "lvl_1")
            os.makedirs(migration_1_lvl_folder, exist_ok=True)

            migration_2_1_lvl_folder = os.path.join(reports_folder, "lvl_2.1")
            os.makedirs(migration_2_1_lvl_folder, exist_ok=True)

            migration_2_2_lvl_folder = os.path.join(reports_folder, "lvl_2.2")
            os.makedirs(migration_2_2_lvl_folder, exist_ok=True)

if __name__ == "__main__":
    input_csv_file = 'migration_plan.txt'
    create_company_files(input_csv_file)