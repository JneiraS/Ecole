from DAO.database_manager import DatabaseConnectionManager
from src.table_name import TableName


class StudentManager(DatabaseConnectionManager):
    def query_all(self) -> list:
        """
        Renvoit la liste de tous les etudiants avec leurs informations
        :return:
        """
        try:
            self.open_connection()
            query = (f"SELECT DISTINCT  student.student_nbr, person.first_name, person.last_name, person.age "
                     f"FROM {TableName.STUDENT.value} "
                     f"JOIN person ON student.id_person = person.id_person "
                     f"JOIN takes ON student.student_nbr = takes.student_nbr;")
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

