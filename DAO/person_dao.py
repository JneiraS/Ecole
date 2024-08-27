from DAO.database_manager import DatabaseConnectionManager
from models.person import Person
from src.table_name import TableName


class PersonManager(DatabaseConnectionManager):

    def query_all(self, table_name: TableName) -> list:
        try:
            self.open_connection()

            query = f"SELECT * FROM {table_name};"
            self.cursor.execute(query)

            rows = self.cursor.fetchall()

            self.close_connection()

            return rows
        except Exception as e:
            print(f"An error occurred: {e}")
            self.close_connection()
            return []
