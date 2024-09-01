def execute_query(self, query: str) -> int | None:
    """
    Execute une requête dans la base de données
    """
    try:
        self.open_connection()
        self.cursor.execute(query)
        id_generated = self.cursor.lastrowid
        self.conn.commit()
        self.close_connection()
        return id_generated

    except Exception as e:
        print(f"Une erreur est survenue : {e}")
        self.close_connection()
        return None


def find_value(self, query: str) -> int | None:
    """
    Execute une requête dans la base de données
    """
    try:
        self.open_connection()
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.close_connection()
        return rows

    except Exception as e:
        print(f"Une erreur est survenue : {e}")
        self.close_connection()
        return None


def execute_query_with_condition(self, query: str):
    try:
        self.open_connection()
        self.cursor.execute(query)
        self.conn.commit()
        self.close_connection()
        return True

    except Exception as e:
        print(f"An error occurred: {e}")
        self.close_connection()
        return False
