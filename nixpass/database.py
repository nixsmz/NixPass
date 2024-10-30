import mariadb, sys

class Database:
    TAG = "DB"
    SQL_MODEL = "./srv/tables.sql"
    connection = None
    def __init__(self, host: str, port: str, user: str, password: str, name: str):
        try:
            self.connection = mariadb.connect(host=host, port=int(port), user=user, password=password)
            cursor = self.connection.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {name};")
            cursor.execute(f"USE {name};")
            with open(self.SQL_MODEL, "r") as file:
                for cmd in list(filter(lambda x: len(x) > 10, file.read().split(";"))):
                    cursor.execute(cmd)
                file.close()
        except mariadb.Error as e: sys.exit(f"[{self.TAG}] Error: {e}")
        cursor.close()
    def close(self):
        if self.connection: self.connection.close()
