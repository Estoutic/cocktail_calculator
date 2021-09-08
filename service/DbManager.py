import sqlite3


class DbConnectionManager():

    def __init__(self) -> None:
        super().__init__()
        self.db = sqlite3.connect('../url.db', check_same_thread=False)
        self.sql = self.db.cursor()
        self.url_repo = UrlsBdRepository(self.db)
        self.sql.execute("""CREATE TABLE IF NOT EXISTS menu (
            name TEXT,
            count INT,
            number INT
        ) """)

        self.db.commit()

    def get_url_repository(self):
        return self.url_repo


class UrlsBdRepository:
    def __init__(self, connection) -> None:
        super().__init__()
        self.connection = connection
        self.db = sqlite3.connect('../url.db', check_same_thread=False)
        self.sql = self.db.cursor()

    def add_cocktail(self, name, count, number):
        cursor = self.sql.execute(f"SELECT name FROM menu WHERE  name = '{name}'")
        if cursor.fetchone() is None:
            self.sql.execute(f"INSERT INTO users VALUES(?,?,?)",
                             (name, count, number))
            self.db.commit()
            return True
        return False

    def get_personal_menu(self):
        cursor = self.sql.execute(f"SELECT * FROM users")
        return list(cursor.fetchall())
