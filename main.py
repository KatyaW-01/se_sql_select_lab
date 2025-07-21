# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect('data.sqlite')

employee_data = pd.read_sql("""SELECT * FROM employees""", conn)
print(employee_data)
# STEP 2
# Replace None with your code
df_first_five = pd.read_sql("""SELECT employeeNumber,lastName FROM employees""",conn)
print(df_first_five)

# STEP 3
# Replace None with your code
df_five_reverse = pd.read_sql("""SELECT lastName, employeeNumber FROM employees""",conn)

# STEP 4
# Replace None with your code
df_alias = pd.read_sql("""SELECT lastName, employeeNumber AS ID FROM employees""", conn)

# STEP 5
# Replace None with your code
df_executive = pd.read_sql("""
SELECT jobTITLE,
    CASE
    WHEN jobtitle = "President"
    OR jobTitle = "VP Sales" 
    OR jobTitle = "VP Marketing" THEN "Executive"
    ELSE "Not Executive"
    END AS role
  FROM employees;
""",conn)

# STEP 6
# Replace None with your code
df_name_length = pd.read_sql("""SELECT length(lastName) AS name_length from employees""",conn)

# STEP 7
# Replace None with your code
df_short_title = pd.read_sql("""SELECT substr(jobTitle, 1, 2) AS short_title from employees""",conn)
print(df_short_title)

# STEP 8
# Replace None with your code
sum_total_price = None

# STEP 9
# Replace None with your code
df_day_month_year = None