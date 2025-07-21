import sqlite3
import pandas as pd

#Connect to the database
conn = sqlite3.connect('data.sqlite')

#Employee Data table
employee_data = pd.read_sql("""SELECT * FROM employees""", conn)

#Queries
df_first_five = pd.read_sql("""SELECT employeeNumber,lastName FROM employees""",conn)

df_five_reverse = pd.read_sql("""SELECT lastName, employeeNumber FROM employees""",conn)

df_alias = pd.read_sql("""SELECT lastName, employeeNumber AS ID FROM employees""", conn)

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

df_name_length = pd.read_sql("""SELECT length(lastName) AS name_length from employees""",conn)

df_short_title = pd.read_sql("""SELECT substr(jobTitle, 1, 2) AS short_title from employees""",conn)

#Order details table
order_details = pd.read_sql("""SELECT * FROM orderDetails;""", conn) 
print(order_details)

sum_total_price = pd.read_sql("""SELECT CAST(round(priceEach * quantityOrdered) AS INTEGER) AS total_price from orderDetails""",conn).sum()

df_day_month_year = pd.read_sql("""
SELECT orderDate,
       strftime("%m", orderDate) AS month,
       strftime("%Y", orderDate) AS year,
       strftime("%d", orderDate) AS day
  FROM orders;
""", conn)

conn.close()