import sqlite3


class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def to_dict(self):
        return {"id": self.id, "name": self.name}


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
            create table if not exists users (
                id varchar,
                name varchar
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
        sql = """SELECT * FROM users WHERE id = :id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"id": user_id})

        data = cursor.fetchone()  # OJO! devuelve un diccionario

        user = User(**data)

        return user

    def save(self, oneUser):
        sql_insert_data = """insert into users (id, name) values (
            :id, :name) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql_insert_data, oneUser.to_dict())
        conn.commit()
