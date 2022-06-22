import sqlite3


""" TIMEOUT
import optuna

  # Relax timeout to circumvent the error. Suitable value depends on environment
        # and e.g. trial/process parallelism. (With my local MacBook Pro and a trial parallelism of 64,
        #  a timeout of 100 seemed stable.
        # Note that keys/values of `engine_kwargs` depends on the actual RDB backend.
        storage = optuna.storages.RDBStorage(
            url="sqlite:///mystorage.db",
            engine_kwargs={"connect_args": {"timeout": 100}},
        )
        study = optuna.create_study(storage=storage)

"""


class Publication:
    def __init__(
        self,
        id_pub,
        user_id,
        publication_type,
        title,
        description,
        date,
        location,
        category_id,
        tags,
    ):

        self.id_pub = id_pub
        self.user_id = user_id
        self.publication_type = publication_type
        self.title = title
        self.description = description
        self.date = date
        self.location = location
        self.category_id = category_id

        if tags is not None:
            self.tags = tags
        else:
            self.tags = []

    def to_dict(self):
        return {
            "id_pub": self.id_pub,
            "user_id": self.user_id,
            "publication_type": self.publication_type,
            "title": self.title,
            "description": self.description,
            "date": self.date,
            "location": self.location,
            "category_id": self.category_id,
            "tags": self.tags,
        }


class PublicationRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):

        # conn = sqlite.connect("database.sql", timeout=30.0)
        # conn = sqlite3.connect(self.database_path)
        conn = sqlite3.connect(self.database_path, timeout=100.0)
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
                location VARCHAR,
                category_id VARCHAR               
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql_table_publications)

        sql_table_publications_tags = """
        CREATE TABLE IF NOT EXISTS publicationstags (
        tag_id INTEGER,
        id_pub VARCHAR,
       
        FOREIGN KEY("tag_id") REFERENCES "tags"("tag_id")
        FOREIGN KEY("id_pub") REFERENCES "publications"("id_pub") ON DELETE CASCADE);

        """
        cursor.execute(sql_table_publications_tags)

        conn.commit()

    def get_publications(self):
        sql = """SELECT * FROM publications"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()

        publications_list = []

        for element in data:
            id = element["id_pub"]
            publication = Publication(
                id_pub=element["id_pub"],
                user_id=element["user_id"],
                publication_type=element["publication_type"],
                title=element["title"],
                description=element["description"],
                date=element["date"],
                location=element["location"],
                category_id=element["category_id"],
                tags=self.get_publication_id_tags(
                    id
                ),  # Rellenamos el atributo con la lista
            )

            publications_list.append(publication)

        return publications_list

    def get_publication_by_id(self, id_pub):
        sql = """SELECT * FROM publications WHERE id_pub = :id_pub"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"id_pub": id_pub})

        data = cursor.fetchone()
        # Extraemos la lista de tag_id asociados
        if data is not None:
            tag_list = self.get_publication_id_tags(id_pub)
            # Instanciamos el objeto publicación con los datos de la
            # tabla publications y el método que obtiene las 'tags'
            publication = Publication(
                id_pub=data["id_pub"],
                user_id=data["user_id"],
                publication_type=data["publication_type"],
                title=data["title"],
                description=data["description"],
                date=data["date"],
                location=data["location"],
                category_id=data["category_id"],
                tags=tag_list,  # Rellenamos el atributo con la lista
            )

            return publication
        else:
            return None

    def get_publication_id_tags(self, id_pub):
        sql = """SELECT * FROM publicationstags  WHERE id_pub=:id_pub"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"id_pub": id_pub})

        data = cursor.fetchall()

        tag_id_list = [i["tag_id"] for i in data]

        return tag_id_list

    def get_all_tags_with_names_by_publication_id(self, id_pub):
        sql = """select * from  publicationstags
                where id_pub=?"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, (id_pub,))
        data = cursor.fetchall()
        tags_list = [dict(row) for row in data]
        return tags_list

    def save(self, publication):
        sql = """INSERT INTO publications (id_pub, user_id, publication_type, title, description, date,
         location, category_id) values (
           :id_pub, :user_id, :publication_type, :title, :description, :date, :location, :category_id
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
                "category_id": publication.category_id,
            },
        )
        # Database is locked - Cuando guardamos 1 nueva publicación no se pueden añadir etiquetas
        # Remedio: usar el método save_publication_tags
        # self.save_publication_tags(publication.id_pub, publication.tags)
        conn.commit()

    def save_publication_tags(self, id_pub, tag_list):
        sql_first_delete = """DELETE FROM publicationstags WHERE id_pub=:id_pub
        """
        sql_then_insert = """ INSERT INTO publicationstags (id_pub, tag_id)
                            VALUES (:id_pub, :tag_id)
                    """
        conn = self.create_conn()
        cursor = conn.cursor()
        # Borramos las 'tags'antiguas
        cursor.execute(sql_first_delete, {"id_pub": id_pub})
        # Para que sólo se guarden las nuevas
        for tag in tag_list:
            cursor.execute(sql_then_insert, {"id_pub": id_pub, "tag_id": tag})
        conn.commit()

    def edit_publication(self, publication):  # añadido puedes editar " category_id"
        sql = """UPDATE publications SET title= ?, description = ?, location= ?,  category_id=?  WHERE id_pub = ?"""
        conn = self.create_conn()
        cursor = conn.cursor()

        # publication.publication_type  NO publication.date, .tags,
        cursor.execute(
            sql,
            (
                publication.title,
                publication.description,
                publication.location,
                publication.category_id,
                publication.id_pub,
            ),
        )
        conn.commit()

    def delete_by_id(self, id):
        sql = """DELETE FROM publications WHERE id_pub = :id_pub"""
        sql_delete_tags_conections = """DELETE FROM publicationstags WHERE id_pub=:id_pub
        """

        conn = self.create_conn()
        cursor = conn.cursor()
        # Borramos las relaciones del "pub_id" con sus 'tags' de la tabla intermedia
        cursor.execute(sql_delete_tags_conections, {"id_pub": id})
        cursor.execute(sql, {"id_pub": id})

        conn.commit()

    def search_publications_by_user_id(self, user_id):
        sql = """ SELECT * FROM publications WHERE user_id = :user_id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"user_id": user_id})

        data = cursor.fetchall()

        publications_list = []

        for element in data:
            id = element["id_pub"]
            publication = Publication(
                id_pub=element["id_pub"],
                user_id=element["user_id"],
                publication_type=element["publication_type"],
                title=element["title"],
                description=element["description"],
                date=element["date"],
                location=element["location"],
                category_id=element["category_id"],
                tags=self.get_publication_id_tags(id)
                # Rellenamos el atributo con la lista
            )

            publications_list.append(publication)

        return publications_list

    def get_all_categories_id(self):
        sql = """SELECT DISTINCT category_id FROM publications"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()

        results = [tuple(row) for row in data]
        # lista de listas [["CAT_EDUCATION"], ["CAT_SOCIAL_SERVICES"], ["CAT_JOBS"]]
        return results
