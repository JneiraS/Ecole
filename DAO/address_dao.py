from .database_manager import DatabaseConnectionManager
from src.table_name import TableName


class AddressManager(DatabaseConnectionManager):
    def query_all(self) -> list:
        try:
            self.open_connection()
            query = f"SELECT * FROM {TableName.ADDRESS.value};"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            self.close_connection()
            return rows
        except Exception as e:
            print(f"An error occurred: {e}")
            self.close_connection()
            return []