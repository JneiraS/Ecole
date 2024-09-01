from DAO.database_manager import DatabaseConnectionManager
from models.course import Course
from src.table_name import TableName




class CourseDAO(DatabaseConnectionManager):

    def get_all_course_ids(self):
        """
        Renvoit la liste de tous id enseignants
        :return:
        """
        try:
            self.open_connection()
            query = (
                f"SELECT * FROM `{TableName.COURSE.value}`;"
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
        try:
            self.open_connection()
            query = f"SELECT * FROM {TableName.COURSE.value};"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            self.close_connection()
            return rows
        except Exception as e:
            print(f"An error occurred: {e}")
            self.close_connection()
            return []

    def create(self, new_course: Course):
        """
        Crée un nouveau cours dans la base de données.
        :param new_course:
        :return:
        """
        try:
            self.open_connection()
            query = (f"INSERT INTO course (name, start_date, end_date) VALUES ('{new_course.name}',"
                     f" '{new_course.start_date}', '{new_course.end_date}');")
            self.cursor.execute(query)
            new_teacher_id = self.cursor.lastrowid
            self.conn.commit()
            self.close_connection()
            return new_teacher_id
        except Exception as e:
            print(f"An error occurred: {e}")
            self.close_connection()

    def read(self, course_to_read):
        """
        Renvoit le cours correspondant à l'entité dont l'id est id_course (ou None s'il n'a pu être trouvé)
        :param course_to_read:
        :return:
        """
        if course_to_read.id is not None:

            try:
                self.open_connection()
                query = f"SELECT * FROM course where id_course = {course_to_read.id};"
                self.cursor.execute(query)
                rows = self.cursor.fetchall()
                self.close_connection()
                return rows

            except Exception as e:
                print(f"An error occurred: {e}")
                self.close_connection()

        return None

    def update(self, course_to_update):
        """Mett à jour la base de données avec les nouvelles informations du cours."""
        self.open_connection()
        query = (f" UPDATE course SET name = '{course_to_update.name}', start_date = '"
                 f"{course_to_update.start_date}', end_date = '{course_to_update.end_date}', id_teacher = "
                 f"{course_to_update.teacher} "
                 f"WHERE id_course = {course_to_update.id};")
        print(query)

        self.cursor.execute(query)
        self.conn.commit()
        self.close_connection()

    def delete(self):
        ...
