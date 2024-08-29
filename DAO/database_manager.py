from threading import Lock

import pymysql


class SingletonMeta(type):
    """
    Singleton metaclass
    """
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class DatabaseConnectionManager(metaclass=SingletonMeta):
    def __init__(self):
        """
        Initializes a new instance of the DatabaseConnectionManager class.
        """
        self.conn = None
        self.cursor = None

    def open_connection(self):
        """Opens a database connection."""
        # TODO : Extraire dans un json
        config = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': '',
            'database': 'ecole'
        }
        self.conn = pymysql.connect(**config, cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.conn.cursor()

    def close_connection(self):
        """Closes the database connection."""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def query_all(self) -> list:
        ...

    def create(self, class_name):
        """
        Crée une nouvelle entit dans la base de données.
        :param class_name:
        :return:
        """
        ...

    def read(self, table_name: str):
        """Renvoit le cours correspondant à l'entité dont l'id est id_course
        (ou None s'il n'a pu être trouvé)
        """
        pass

    def update(self, table) -> bool:
        """Met à jour en BD l'entité Course correspondant à course, pour y correspondre

        :param table:
        :return: True si la mise à jour a pu être réalisée
        """
        pass

    def delete(self, course) -> bool:
        """Supprime en BD l'entité Course correspondant à course

        :param course: cours dont l'entité Course correspondante est à supprimer
        :return: True si la suppression a pu être réalisée
        """
        pass
