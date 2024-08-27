from DAO.database_manager import DatabaseConnectionManager
from models.teacher import Teacher


class TeacherManager(DatabaseConnectionManager):



    def query_all(self, table_name) -> list:
        try:
            self.open_connection()

            query = (f"SELECT t.id_teacher,t.start_date, p.first_name, p.last_name, p.age, p.id_address "
                     f"FROM teacher t "
                     f"INNER JOIN "
                     f"person p ON t.id_person = p.id_person;")
            self.cursor.execute(query)

            rows = self.cursor.fetchall()

            self.close_connection()

            return rows
        except Exception as e:
            print(f"An error occurred: {e}")
            self.close_connection()
            return []

    def create(self, new_teacher: Teacher):
        """
        Crée un nouveau cours dans la base de données.
        :param new_teacher:
        :return:
        """
        try:
            self.open_connection()
            query = (f"INSERT INTO courses (name, start_date, end_date) VALUES ('{new_teacher.name}',"
                     f" '{new_teacher.start_date}', '{new_teacher.end_date}');")
            self.cursor.execute(query)
            self.conn.commit()
            self.close_connection()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.close_connection()

    def read(self, teacher_to_read: Teacher):
        """
        Renvoit le professeur correspondant à l'entité dont l'id est id_teacher (ou None s'il n'a pu être 
        trouvé)
        :param teacher_to_read:
        :return:
        """
        if teacher_to_read.id is not None:

            try:
                self.open_connection()
                query = (f"SELECT t.id_teacher,t.start_date, p.first_name, p.last_name, p.age, p.id_address "
                         f"FROM teacher t "
                         f"INNER JOIN "
                         f"person p ON t.id_person = p.id_person;")
                self.cursor.execute(query)
                rows = self.cursor.fetchall()
                self.close_connection()
                return rows

            except Exception as e:
                print(f"An error occurred: {e}")
                self.close_connection()

        return None

    def update(self, course_to_update: Teacher):
        """Mett à jour la base de données avec les nouvelles informations du cours."""
        self.open_connection()
        query = (f" UPDATE course SET name = '{course_to_update.name}', start_date = '"
                 f"{course_to_update.start_date}', end_date = '{course_to_update.end_date}', id_teacher = "
                 f"{course_to_update.teacher};")
        self.cursor.execute(query)
        self.close_connection()

    def delete(self): ...
