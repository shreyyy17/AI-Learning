import sqlite3


class DatabaseConnection:
    def __init__(self,host):
        self.connection = None
        self.host = host

    def __enter__(self):
        self.connection = sqlite3.connect(self.host)
        return self.connection

# exc_type: execption type, exc_val: exception_value, exc_tb:exception_TraceBack
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_tb or exc_val:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()


