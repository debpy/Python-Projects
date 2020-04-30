import sqlite3

class DatabaseConnection:

    def __init__(self, host):
        self.host = host
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.host)
        return self.connection

    #exc_type, exc_value, exc_tb -exception type, exception value, exception traceback
    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type or exc_value or exc_tb:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()