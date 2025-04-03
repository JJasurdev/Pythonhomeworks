import sqlite3
import pandas as pd

# Load the chinook.db database and connect
conn = sqlite3.connect('chinook.db')

# Perform an inner join between the customers and invoices tables on the CustomerId column
query = """
    SELECT c.CustomerId, c.FirstName, c.LastName, COUNT(i.InvoiceId) AS TotalInvoices
    FROM customers c
    INNER JOIN invoices i ON c.CustomerId = i.CustomerId
    GROUP BY c.CustomerId;
"""
df_inner_join = pd.read_sql_query(query, conn)

# Display the result of the inner join with the total number of invoices for each customer
print("Inner Join: Total number of invoices for each customer:")
print(df_inner_join)

# Close the connection to the database
conn.close()
