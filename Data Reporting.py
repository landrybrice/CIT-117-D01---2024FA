import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('retirement.db')
cursor = conn.cursor()

# Join tables and process data
cursor.execute('''
SELECT e.Name, p.Year, p.Earnings, s.Minimum
FROM Employee e
JOIN Pay p ON e.EmployeeID = p.EmployeeID
JOIN SocialSecurityMin s ON p.Year = s.Year
''')

# Process each record
for row in cursor.fetchall():
    name, year, earnings, minimum = row
    if earnings >= minimum:
        print(f"{name} in {year}: Yes")
    else:
        print(f"{name} in {year}: No")

# Close the connection
conn.close()
