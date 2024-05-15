import mysql.connector
import pandas as pd

# Connect to the database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="viaduct.proxy.rlwy.net",
            user="root",
            password="bDgjXpCXhsPUXzTzJKhEDBbtafoDkjtV",
            port=50270,
            database="railway"
        )
        print(f"Connected to database railway successfully")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Create the Suspicious and filteredTransactions tables
def create_tables(connection, table_definitions):
    try:
        cursor = connection.cursor()
        for table_name, table_definition in table_definitions.items():
            cursor.execute(table_definition)
            print(f"Table '{table_name}' created successfully")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Insert data from CSV into the table
def insert_data(connection, file_path, table_name, columns_to_insert):
    try:
        cursor = connection.cursor()
        df = pd.read_csv(file_path)

        # Check if the specified columns exist in the CSV file
        csv_columns = set(df.columns)
        if not set(columns_to_insert).issubset(csv_columns):
            print(f"Columns specified for insertion not found in CSV file: {file_path}")
            print(f"Missing columns: {set(columns_to_insert) - csv_columns}")
            return

        # Create the SQL insert statement dynamically
        sql_insert_statement = f"""
            INSERT INTO {table_name} ({', '.join(columns_to_insert)})
            VALUES ({', '.join(['%s'] * len(columns_to_insert))})
        """

        # Insert data into the table
        for index, row in df.iterrows():
            values = tuple(row[column] for column in columns_to_insert)
            cursor.execute(sql_insert_statement, values)

        connection.commit()
        print(f"Data inserted into '{table_name}' successfully")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Main function
def main():
    database_name = "railway"
    matched_transactions_path = "reports/matched_transactions.csv"
    filtered_data_path = "data_processed/filtered_data_2.csv"

    connection = connect_to_database()
    if connection:
        table_definitions = {
            "Suspicious": """
                CREATE TABLE IF NOT EXISTS Suspicious (
                    type VARCHAR(255),
                    amount FLOAT,
                    nameOrig VARCHAR(255),
                    oldbalanceOrg FLOAT,
                    newbalanceOrig FLOAT,
                    nameDest VARCHAR(255),
                    oldbalanceDest FLOAT,
                    newbalanceDest FLOAT,
                    isFraud INT
                )
            """,
            "filteredTransactions": """
                CREATE TABLE IF NOT EXISTS filteredTransactions (
                    amount FLOAT,
                    nameOrig VARCHAR(255),
                    oldbalanceOrg FLOAT,
                    nameDest VARCHAR(255),
                    oldbalanceDest FLOAT,
                    isFraud INT
                )
            """
        }

        create_tables(connection, table_definitions)

        # Define columns to insert for each table
        suspicious_columns = [
            'type', 'amount', 'nameOrig', 'oldbalanceOrg', 'newbalanceOrig',
            'nameDest', 'oldbalanceDest', 'newbalanceDest', 'isFraud'
        ]
        filtered_columns = [
            'amount', 'nameOrig', 'oldbalanceOrg', 'nameDest',
            'oldbalanceDest', 'isFraud'
        ]

        # Insert data into both tables
        insert_data(connection, matched_transactions_path, "Suspicious", suspicious_columns)
        # insert_data(connection, filtered_data_path, "filteredTransactions", filtered_columns)

        connection.close()

if __name__ == "__main__":
    main()
