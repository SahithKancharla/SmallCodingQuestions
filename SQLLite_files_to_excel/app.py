import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect("users.db")

# Read data from SQLite into a pandas DataFrame
df = pd.read_sql_query("SELECT * FROM users;", conn)
print(df)

# Close the database connection
conn.close()

df.to_csv("output.csv", index=False)
