import sqlite3
import os

# Get the current working directory
current_directory = os.getcwd()
print("Current Directory:", current_directory)

# List all files in the current directory
files_in_directory = os.listdir(current_directory)
print("Files in Directory:", files_in_directory)

# Ensure the required text files are present
required_files = ['Employee.txt', 'Pay.txt', 'SocialSecurityMinimum.txt']
for file in required_files:
    if file not in files_in_directory:
        print(f"Error: {file} is not in the current directory.")
    else:
        print(f"{file} is present.")

# Create a SQLite database
conn = sqlite3.connect('retirement.db')
cursor = conn.cursor()

try:
    # Drop existing tables
    cursor.execute('DROP TABLE IF EXISTS Employee')
    cursor.execute('DROP TABLE IF EXISTS Pay')
    cursor.execute('DROP TABLE IF EXISTS SocialSecurityMin')

    # Create tables
    cursor.execute('''
    CREATE TABLE Employee (
        EmployeeID INTEGER PRIMARY KEY,
        Name TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE Pay (
        EmployeeID INTEGER,
        Year INTEGER,
        Earnings REAL,
        FOREIGN KEY(EmployeeID) REFERENCES Employee(EmployeeID)
    )
    ''')

    cursor.execute('''
    CREATE TABLE SocialSecurityMin (
        Year INTEGER PRIMARY KEY,
        Minimum REAL
    )
    ''')

    def import_data(file_path, table_name, skip_header=True):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if skip_header:
                lines = lines[1:]
            for line in lines:
                data = line.strip().split(',')
                cursor.execute(f"INSERT INTO {table_name} VALUES ({', '.join(['?' for _ in data])})", data)

    # Import data into tables
    import_data('Employee.txt', 'Employee')
    import_data('Pay.txt', 'Pay')
    import_data('SocialSecurityMinimum.txt', 'SocialSecurityMin')

    # Commit the data
    conn.commit()

except sqlite3.OperationalError as e:
    print(f"Operational Error: {e}")

finally:
    # Close the connection
    conn.close()
