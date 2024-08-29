from DAO.database_manager import DatabaseConnectionManager
from models.person import Person
from src.table_name import TableName


class PersonManager(DatabaseConnectionManager):

    def query_all(self) -> list:
        try:
            self.open_connection()

            query = f"SELECT * FROM {TableName.PERSON.value};"
            self.cursor.execute(query)

            rows = self.cursor.fetchall()

            self.close_connection()

            return rows
        except Exception as e:
            print(f"An error occurred: {e}")
            self.close_connection()
            return []

    def create(self, class_name):
        ...

    def read(self, table_name: str):
        ...

    def update(self, table) -> bool:
        ...

    def delete(self, course) -> bool:
        ...
