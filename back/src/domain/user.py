import sqlite3


class User:
    def __init__(self, user_id, first_name, last_name, email):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
        }


class UserRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            CREATE TABLE IF NOT EXISTS users (
                user_id VARCHAR,
                first_name VARCHAR, 
                last_name VARCHAR, 
                email VARCHAR,
                PRIMARY KEY("user_id") 
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_all(self):
        sql = """select * from users"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()

        users_list = []
        for item in data:
            user = User(**item)
            users_list.append(user)

        return users_list

    def get_by_id(self, user_id):
        sql = """SELECT * FROM users WHERE user_id = :user_id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"user_id": user_id})

        data = cursor.fetchone()  # OJO! devuelve un diccionario

        user = User(**data)

        return user

    def save(self, oneUser):
        sql_insert_data = """insert into users (user_id, first_name, last_name, email) values (
            :user_id, :first_name, :last_name, :email) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql_insert_data, oneUser.to_dict())
        conn.commit()
