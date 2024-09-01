from DAO.database_manager import DatabaseConnectionManager
from models.person import Person
from src.table_name import TableName


class PersonDAO(DatabaseConnectionManager):

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

    def create(self, class_name: Person, id_address):

        try:
            self.open_connection()
            query = (
                f"INSERT INTO {TableName.PERSON.value} (`first_name`, `last_name`, `age`, `id_address`) "
                f"VALUES ('{class_name.first_name}', '{class_name.last_name}', '{class_name.age}',"
                f" '{id_address}');"
            )
            self.cursor.execute(query)
            new_person_id = self.cursor.lastrowid
            self.conn.commit()
            self.close_connection()
            return new_person_id
        except Exception as e:
            print(f"An error occurred: {e}")
            self.close_connection()
            return []

    def read(self, table_name: str):
        ...

    def update(self, person_to_update: Person) -> bool:
        try:
            self.open_connection()
            query = (
                f"UPDATE {TableName.PERSON.value} SET first_name = '{person_to_update.first_name}', last_name = '{person_to_update.last_name}',"
                f" age = '{person_to_update.age}' WHERE "
                f"{TableName.PERSON.value}.id_person = '{person_to_update.id}';"
            )
            print(query)
            self.cursor.execute(query)
            self.conn.commit()
            self.close_connection()
            return True

        except Exception as e:
            print(f"An error occurred: {e}")
            self.close_connection()
            return False


    def delete(self, course) -> bool:
        ...
