from DAO import execute_query_with_confirmation, find_value, execute_query
from DAO.database_manager import DatabaseConnectionManager
from models.course import Course
from src.table_name import TableName


class CourseDAO(DatabaseConnectionManager):

    def get_all_course_ids(self):
        """
        Récupère une liste de tous les identifiants de cours de la base de données.
        :return: Une liste de lignes contenant les identifiants de cours. Si une erreur se produit, une liste
        vide est renvoyée.
        """
        query = (
            f"SELECT * FROM `{TableName.COURSE.value}`;")
        return find_value(self, query)

    def query_all(self) -> list | None:
        """
        Récupère toutes les données de la table des cours.
        :return: Une liste de toutes les données des cours ou None si la requête échoue.
        """
        query = f"SELECT * FROM {TableName.COURSE.value};"
        return find_value(self, query)

    def create(self, new_course: Course):
        """
        Crée un nouveau cours dans la base de données.
        :param new_course:
        :return:
        """
        query = (f"INSERT INTO course (name, start_date, end_date) VALUES ('{new_course.name}',"
                 f" '{new_course.start_date}', '{new_course.end_date}');")
        return execute_query(self, query)

    def read(self, course_to_read) -> list | None:
        """
        Renvoit le cours correspondant à l'entité dont l'id est id_course (ou None s'il n'a pu être trouvé)
        :param course_to_read:
        :return: liste des cours correspondant à l'entité dont l'id est id_course
        (ou None s'il n'a pu être trouvé)
        """
        if course_to_read.id is not None:
            query = f"SELECT * FROM course where id_course = {course_to_read.id};"
            return find_value(self, query)

    def update(self, course_to_update):
        """Mett à jour la base de données avec les nouvelles informations du cours."""
        query = (f" UPDATE course SET name = '{course_to_update.name}', start_date = '"
                 f"{course_to_update.start_date}', end_date = '{course_to_update.end_date}', id_teacher = "
                 f"{course_to_update.teacher} "
                 f"WHERE id_course = {course_to_update.id};")
        return execute_query_with_confirmation(self, query)

    def delete(self, course_to_delete: Course) -> bool:
        query = f"DELETE FROM {TableName.COURSE.value} WHERE id_course = {course_to_delete.id};"
        return execute_query_with_confirmation(self, query)
