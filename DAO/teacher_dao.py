from DAO.database_manager import DatabaseConnectionManager
from models.teacher import Teacher
from src.table_name import TableName


class TeacherDAO(DatabaseConnectionManager):

    def get_all_teacher_ids(self):
        """
        Renvoit la liste de tous id enseignants
        :return:
        """
        try:
            self.open_connection()
            query = (
                f"SELECT * FROM `{TableName.TEACHER.value}`;"
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

            query = (
                f"SELECT t.id_teacher,t.start_date, p.first_name, p.last_name, p.age, p.id_address, t.id_person "
                f"FROM {TableName.TEACHER.value} t "
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
        Crée un nouvel enseignant dans la base de données.
        ""
        :param new_teacher:
        :return:
        """
        try:
            self.open_connection()

            query = f"START TRANSACTION;"
            self.cursor.execute(query)
            # Créer la personne
            query = (f"INSERT INTO person (first_name, last_name, age) "
                     f"VALUES ('{new_teacher.first_name}', '{new_teacher.last_name}', {new_teacher.age});")
            print(query)
            self.cursor.execute(query)
            # Créer l'enseignant en récupérant l'ID de la personne créée
            query = (f"INSERT INTO teacher (start_date, id_person)"
                     f"VALUES ('{new_teacher.hiring_date}', "
                     f"LAST_INSERT_ID());")

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

    def update(self, teacher_to_update: Teacher):
        """Mett à jour la base de données avec les nouvelles informations du professeur."""
        self.open_connection()
        query = f"SELECT id_person FROM teacher WHERE id_teacher = '{teacher_to_update.id}';"
        self.cursor.execute(query)

        result = self.cursor.fetchone()
        id_person = result['id_person']

        query = (f"UPDATE person SET "
                 f"first_name = '{teacher_to_update.first_name}', "
                 f"last_name = '{teacher_to_update.last_name}', "
                 f"age = {teacher_to_update.age} "
                 f"WHERE id_person = '{id_person}';")

        self.cursor.execute(query)
        self.conn.commit()
        self.close_connection()

    def delete(self, ):
        """
        Supprime le professeur de la base de données.
        :return:
        """
        pass
