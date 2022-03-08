# Auto-Grader for Database Queries


# Installation Overview
1. Python installation  
2. MySQL installation
3. Code editors (Optional)
4. Setup Python virtual environment
5. Python Project setup
6. Creating and updating credentials

Detailed steps available in file installation_instructions.md

--------------------------------------------------------------------------------------------
# Running Queries

1. In your command line, go to the project folder and activate the python virtual environment using the command:
    ```
        source env/bin/activate 
    ```
2. Write or copy/paste your queries in `queries.sql` located in `solution_sql` folder.
3. In your command line, go to `solution_sql` folder while in `solution_sql` folder.   
   All subsequent steps need to be run in this folder.
5. To generate the answers, use the command below. This creates the answers.json file
```
    python produce_answers.py
```
5. To generate the report, use the command below. This creates the `report.json` file.
```
    python report.py
```
--------------------------------------------------------------------------------------------
# Important Notes

1. All queries must be in queries.sql
2. Do not include a semi-colon(;) in comments in any of the SQL file
3. Must use semicolon(;) after each command in the SQL file
4. Do not change any of the database files inside the folder `testDBs`
5. Do not change or add any file inside the folder `testDBs`
6. Do not change `create_empty_tables.sql` file or its location

--------------------------------------------------------------------------------------------
