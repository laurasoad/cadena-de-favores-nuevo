import sqlite3


class Tag:
    def __init__(self, tag_id, name):
        self.tag_id = tag_id
        self.name = name

    def to_dict(self):
        return {
            "tag_id": self.tag_id,
            "name": self.name,
        }


class TagRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):

        sql_table_tags = """
            CREATE TABLE IF NOT EXISTS tags (
                tag_id INTEGER NOT NULL PRIMARY KEY,
                name VARCHAR
            )
        """

        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql_table_tags)

        conn.commit()

    def get_all_tags(self):
        sql = """select * from tags"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()
        result = []
        for item in data:
            oneTag = Tag(**item)
            result.append(oneTag)

        return result

    def save(self, tag):
        sql = """INSERT INTO tags(tag_id, name) values
        (:tag_id, :name
        )"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, tag.to_dict())
        conn.commit()

    def delete_publication_tags(self, id_pub):  # No es mejor en el repo de Pubs?
        sql = """DELETE from publicationstags
                where id_pub= :id_pub"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"id_pub": id_pub})
        conn.commit()
