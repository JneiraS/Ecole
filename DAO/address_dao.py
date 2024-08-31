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

    def create(self, class_name):
        try:
            self.open_connection()
            query = (
                f"INSERT INTO {TableName.ADDRESS.value} (`street`, `city`, `postal_code`) "
                f"VALUES ('{class_name.street}', '{class_name.city}', '{class_name.postal_code}');"
            )
            self.cursor.execute(query)
            new_address_id = self.cursor.lastrowid
            self.conn.commit()
            self.close_connection()
            return new_address_id
        except Exception as e:
            print(f"An error occurred: {e}")
            self.close_connection()
            return []

    def read(self, table_name: str):
        ...

    def update(self, table) -> bool:
        ...

    def delete(self, course) -> bool:
        ...
