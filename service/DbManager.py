import sqlite3


class DbConnectionManager():

    def __init__(self) -> None:
        super().__init__()
        self.db = sqlite3.connect('../url.db', check_same_thread=False)
        self.sql = self.db.cursor()
        self.url_repo = UrlsBdRepository(self.db)
        self.sql.execute("""CREATE TABLE IF NOT EXISTS users (
            
            
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
