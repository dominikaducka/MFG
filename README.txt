MFG: Migration File Generator

A program generating all the configuration files necessary to conduct company migrations based on the migration schedule.

* Migration schedule file
    - file name: migration_plan.txt
    - must include columns: company_name, runner_id, nip_1, nip_2, migration_date

Generated files:
    1. RRU_RRK_1_{company name} - configuration file for RRU1 and RRK1 reports
    2. RRU_RRK_2_{company name} - configuration file for RRU2 and RRK2 reports
    3. migration_lvl_1_{company name} - configuration file for conducting the first stage of migration (assigning IDs)
    4.1 migration_lvl_2_{current month date}_{company name} - configuration file for conducting the secend stage of migration (subscription opening in the current month)
    4.2 migration_lvl_2_{next month date}_{company name} - configuration file for conducting the secend stage of migration (subscription opening for the next month)
    5. migration_lvl_2_{company name} - configuration file for final report 