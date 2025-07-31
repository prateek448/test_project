import mysql.connector
import pandas as pd

# Connect to the database
connection = mysql.connector.connect(
  host='localhost',          # your MySQL host
  user='root',      # your MySQL username
  password='password',  # your MySQL password
  database='new_schema'   # your database name
)

cursor = connection.cursor()

# Load CSV data into a DataFrame
csv_file = '/Users/prateeksharma/Downloads/archive/products.csv'        # path to your CSV file
data = pd.read_csv(csv_file)

# Insert data row by row

data = data.where(pd.notnull(data), None)
sql = """
INSERT INTO Products 
(id, cost, category, name, brand, retail_price, department, sku, distribution_center_id)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Insert each row
for index, row in data.iterrows():
    cursor.execute(sql, (
        row['id'],
        row['cost'],
        row['category'],
        row['name'],
        row['brand'],
        row['retail_price'],
        row['department'],
        row['sku'],
        row['distribution_center_id']
    ))

# Commit and close
connection.commit()
cursor.close()
connection.close()
print("Data imported successfully!")
