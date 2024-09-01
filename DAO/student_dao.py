from DAO import execute_query, find_value, execute_query_with_condition
from DAO.database_manager import DatabaseConnectionManager
from models.student import Student
from src.table_name import TableName


class StudentDAO(DatabaseConnectionManager):

    def create(self, person_id: int, student_nbr: int) -> int | None:
        """
        Crée un nouveau etudiant dans la base de données.
        :param student_nbr:
        :param person_id:
        :return:
        """
        query = (
            f"INSERT INTO {TableName.STUDENT.value} (`student_nbr`, `id_person`) VALUES ({student_nbr}, "
            f"{person_id}) ;")

        return execute_query(self, query)

    def get_all_student_ids(self) -> int | None:
        """
        Renvoit la liste de tous id etudiants
        :return:
        """

        query = (
            f"SELECT * FROM `{TableName.STUDENT.value}`;"
        )

        return find_value(self, query)

    def query_all(self) -> list | None:
        """
        Renvoit la liste de tous les etudiants avec leurs informations
        :return:
        """
        query = (
            f"SELECT DISTINCT  student.student_nbr, person.first_name, person.last_name, person.age "
            f"FROM {TableName.STUDENT.value} "
            f"JOIN person ON student.id_person = person.id_person "
            f"JOIN takes ON student.student_nbr = takes.student_nbr;"
        )
        return find_value(self, query)

    def course_taken_by_student(self) -> list | None:
        """
        Reenvoit l'information de la table takes
        :return:
        """
        query = f"SELECT * FROM `{TableName.TAKES.value}`;"
        return find_value(self, query)

    def update(self, student_to_update: Student) -> bool:

        query = (
            f"UPDATE {TableName.PERSON.value} "
            f"SET "
            f"first_name = '{student_to_update.first_name}', "
            f"last_name = '{student_to_update.last_name}', "
            f"age = {student_to_update.age} "
            f"WHERE "
            f"id_person = {student_to_update.id};"
        )
        return execute_query_with_condition(self, query)

    def delete(self, student_to_update: Student):

        query = f"DELETE FROM {TableName.STUDENT.value} WHERE id_person = {student_to_update.id};"
        return execute_query_with_condition(self, query)

    def assign_student_to_course(self, student_id: int, course_id: int):

        query = f"""INSERT INTO `{TableName.TAKES.value}` (`student_nbr`, `id_course`) VALUES ({student_id},
        {course_id});"""

        return execute_query(self, query)

    def find_id_person_by_student_nbr(self, student_nbr: int):
        query = f"SELECT id_person FROM `{TableName.STUDENT.value}` WHERE student_nbr = {student_nbr};"

        return find_value(self, query)
