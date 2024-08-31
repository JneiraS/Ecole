from DAO import execute_query, find_value
from DAO.database_manager import DatabaseConnectionManager
from models.student import Student
from src.table_name import TableName


class StudentDAO(DatabaseConnectionManager):

    def create(self, person_id: int, student_nbr: int):
        """
        Crée un nouveau etudiant dans la base de données.
        :param student_nbr:
        :param person_id:
        :return:
        """
        try:
            self.open_connection()
            query = (f"INSERT INTO {TableName.STUDENT.value} (`student_nbr`, `id_person`) VALUES ({student_nbr}, "
                     f"{person_id}) ;")

            self.cursor.execute(query)
            new_student_id = self.cursor.lastrowid
            self.conn.commit()
            self.close_connection()
            return new_student_id
        except Exception as e:
            print(f"An error occurred: {e}")
            self.close_connection()


    def get_all_student_ids(self):
        """
        Renvoit la liste de tous id etudiants
        :return:
        """
        try:
            self.open_connection()
            query = (
                f"SELECT * FROM `{TableName.STUDENT.value}`;"
            )
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            self.close_connection()
            return rows
        except Exception as e:
            print(f"An error occurred: {e}")
            self.close_connection()
            return []

    def query_all(self) -> list:
        """
        Renvoit la liste de tous les etudiants avec leurs informations
        :return:
        """
        try:
            self.open_connection()
            query = (
                f"SELECT DISTINCT  student.student_nbr, person.first_name, person.last_name, person.age "
                f"FROM {TableName.STUDENT.value} "
                f"JOIN person ON student.id_person = person.id_person "
                f"JOIN takes ON student.student_nbr = takes.student_nbr;"
            )
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            self.close_connection()
            return rows
        except Exception as e:
            print(f"An error occurred: {e}")
            self.close_connection()
            return []

    def course_taken_by_student(self):
        """
        Reenvoit l'information de la table takes
        :return:
        """
        try:
            self.open_connection()
            query = f"SELECT * FROM `{TableName.TAKES.value}`;"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            self.close_connection()
            return rows

        except Exception as e:
            print(f"An error occurred: {e}")
            self.close_connection()
            return []

    def update(self, student_to_update: Student) -> bool:
        try:

            self.open_connection()
            query = (
                f"UPDATE {TableName.PERSON.value} "
                f"SET "
                f"first_name = '{student_to_update.first_name}', "
                f"last_name = '{student_to_update.last_name}', "
                f"age = {student_to_update.age} "
                f"WHERE "
                f"id_person = {student_to_update.id};"
            )
            self.cursor.execute(query)
            self.conn.commit()
            self.close_connection()
            return True

        except Exception as e:
            print(f"An error occurred: {e}")
            self.close_connection()
            return False

    def delete(self,student_to_update: Student):
        try:
            self.open_connection()
            query = f"DELETE FROM {TableName.STUDENT.value} WHERE id_person = {student_to_update.id};"
            self.cursor.execute(query)
            self.conn.commit()
            self.close_connection()
            return True

        except Exception as e:
            print(f"An error occurred: {e}")
            self.close_connection()
            return False

    def assign_student_to_course(self, student_id, course_id):

        query = f"""INSERT INTO `{TableName.TAKES.value}` (`student_nbr`, `id_course`) VALUES ({student_id},
        {course_id});"""

        return execute_query(self, query)

    def find_id_person_by_student_nbr(self, student_nbr):
        query = f"SELECT id_person FROM `{TableName.STUDENT.value}` WHERE student_nbr = {student_nbr};"

        return find_value(self, query)
