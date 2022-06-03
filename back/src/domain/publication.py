import sqlite3


class Publication:
    def __init__(
        self, id_pub, user_id, publication_type, title, description, date, location
    ):

        self.id_pub = id_pub
        self.user_id = user_id
        self.publication_type = publication_type
        self.title = title
        self.description = description
        self.date = date
        self.location = location
        self.categories = []

    def to_dict(self):
        return {
            "id_pub": self.id_pub,
            "user_id": self.user_id,
            "publication_type": self.publication_type,
            "title": self.title,
            "description": self.description,
            "date": self.date,
            "location": self.location,
            "categories": self.categories,
        }


class PublicationRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql_table_publications = """
            CREATE TABLE IF NOT EXISTS publications (
                id_pub VARCHAR NOT NULL PRIMARY KEY,
                user_id VARCHAR,
                publication_type INTEGER,
                title VARCHAR,
                description VARCHAR,
                date VARCHAR,
                location VARCHAR                
            )
        """

        sql_table_categories = """
            CREATE TABLE IF NOT EXISTS categories (
                id_cat INTEGER PRIMARY KEY,
                name VARCHAR
            )
        """
        sql_table_publications_categories = """
                CREATE TABLE IF NOT EXISTS publicationscategories (
                id_cat INTEGER NOT NULL PRIMARY KEY,
                id_pub VARCHAR NOT NULL,
                FOREIGN KEY("id_pub") REFERENCES "publications"("id_pub"),
                FOREIGN KEY("id_cat") REFERENCES "categories"("id_cat")

                )"""

        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql_table_publications)
        cursor.execute(sql_table_categories)
        cursor.execute(sql_table_publications_categories)
        conn.commit()

    def get_publications(self):
        sql = """SELECT * FROM publications"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()

        publications_list = []

        for element in data:
            publication = Publication(**element)
            # falta añadir aqui las categorias en publication.categories (crear metodo)
            publications_list.append(publication)

        return publications_list

        # book_categories = self.get_book_categories(book)
        # book.categories = book_categories

    def get_publication_by_id(self, id):
        sql = """SELECT * FROM publications WHERE id_pub = :id_pub"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"id_pub": id})

        data = cursor.fetchone()
        publication = Publication(**data)
        # falta añadir categories en publication.categories

        return publication

    def save(self, publication):

        sql = """INSERT INTO publications (id_pub, user_id, publication_type, title, description, date,
         location) values (
           :id_pub, :user_id, :publication_type, :title, :description, :date, :location
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            {
                "id_pub": publication.id_pub,
                "user_id": publication.user_id,
                "publication_type": publication.publication_type,
                "title": publication.title,
                "description": publication.description,
                "date": publication.date,
                "location": publication.location,
            },
        )
        conn.commit()

    def edit_publication(self, publication):
        sql = """UPDATE publications SET title= ?, description = ?, location= ?  WHERE id_pub = ?"""
        conn = self.create_conn()
        cursor = conn.cursor()

        # publication.publication_type  NO publication.date, book.categories,
        cursor.execute(
            sql,
            (
                publication.title,
                publication.description,
                publication.location,
                publication.id_pub,
            ),
        )
        conn.commit()

    def delete_by_id(self, id):
        sql = """DELETE FROM publications WHERE id_pub = :id_pub"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"id_pub": id})

        conn.commit()
