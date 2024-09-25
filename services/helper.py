import os
os.listdir('data')
import pandas as pd
import csv

import sqlite3

def csv_to_sqlite():
    # Path to your CSV file
    csv_file_path = 'data/hiring.csv'

    # Path to the SQLite database file (it will be created if it doesn't exist)
    sqlite_db_path = 'data/hiring.db'

    # Connect to the SQLite database
    conn = sqlite3.connect(sqlite_db_path)
    cursor = conn.cursor()

    # Read data from the CSV file and create a table in the SQLite database
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)  # Read the header row

        # Create a table with columns based on the CSV file's header
        create_table_query = f'CREATE TABLE IF NOT EXISTS data ({", ".join(header)});'
        cursor.execute(create_table_query)

        # Insert data from the CSV file into the SQLite table
        for row in csv_reader:
            insert_query = f'INSERT INTO data ({", ".join(header)}) VALUES ({", ".join(["?"] * len(header))});'
            cursor.execute(insert_query, row)

    # Commit the changes and close the connections
    conn.commit()
    conn.close()

    print('CSV data successfully converted to SQLite database.')
