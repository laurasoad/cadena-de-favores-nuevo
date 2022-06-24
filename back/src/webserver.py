from json import dumps
from flask import Flask, jsonify, request
from flask_cors import CORS

from src.domain.publication import Publication
from src.domain.user import User
from src.lib.utils import object_to_json


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "...magic!"

    @app.route("/api/publications", methods=["GET"])
    def pub_get_all():
        # No auth por ahora, todos pueden ver las publicaciones
        pub_list = repositories["publications"].get_publications()
        return object_to_json(pub_list)

    @app.route("/api/publications", methods=["POST"])
    def pub_save_new():
        # Auth
        user_id_auth = request.headers.get("Authorization")

        body = request.json
        newPublication = Publication(
            id_pub=body["id_pub"],
            user_id=user_id_auth,
            publication_type=body["publication_type"],
            title=body["title"],
            description=body["description"],
            date=body["date"],
            location=body["location"],
            category_id=body["category_id"],
            tags=body["tags"],
        )

        repositories["publications"].save(newPublication)
        repositories["publications"].save_publication_tags(body["id_pub"], body["tags"])
        return "", 200

    @app.route("/api/publications/<id>", methods=["GET"])
    def pub_get_by_id(id):
        # No auth: todos pueden ver un detalle de publicación
        # user_id_auth = request.headers.get("Authorization")

        publication = repositories["publications"].get_publication_by_id(id)

        return object_to_json(publication), 200

        """
        if user_id_auth == publication.user_id:
            return object_to_json(publication), 200

        else:
            return "", 403
        """

    @app.route("/api/publications/<id>", methods=["PUT"])
    def pub_edit_by_id(id):
        # auth -- > solo el usuario puede modificar su propia publicación

        user_id_auth = request.headers.get("Authorization")
        body = request.json

        # comprobar si es el mismo usuario
        is_authorized = body["user_id"] == user_id_auth
        if not is_authorized:
            return "", 403  # cláusula de guarda

        publication = Publication(
            id_pub=body["id_pub"],
            user_id=user_id_auth,
            publication_type=body["publication_type"],
            title=body["title"],
            description=body["description"],
            date=body["date"],
            location=body["location"],
            category_id=body["category_id"],
            tags=[],
        )
        # Guardamos las nuevas tags
        repositories["publications"].save_publication_tags(
            publication.id_pub, body["tags"]
        )
        repositories["publications"].edit_publication(publication)
        return "", 200

    @app.route("/api/publications/<id>", methods=["DELETE"])
    def pub_delete_by_id(id):
        # auth -- > solo el usuario puede borrar su propia publicación

        user_id_auth = request.headers.get("Authorization")
        body = request.json

        # comprobar si es el mismo usuario
        is_authorized = body["user_id"] == user_id_auth
        print(body["user_id"])
        print(user_id_auth)
        if not is_authorized:
            return "", 403  # cláusula de guarda

        repositories["publications"].delete_by_id(id)
        return "", 200

    # TAGS
    @app.route("/api/tags", methods=["GET"])
    def tag_get_all():
        tags = repositories["tags"].get_all_tags()
        return object_to_json(tags)

    # USERS

    @app.route("/api/users", methods=["GET"])
    def users_get_all():
        users = repositories["users"].get_all()
        return object_to_json(users)

    @app.route("/api/users/<id>", methods=["GET"])
    def users_get_by_id(id):
        users = repositories["users"].get_by_id(id)
        return object_to_json(users)

    # @app.route("/api/users", methods=["POST"])
    # def users_save():
    #     body = request.json
    #     oneUser = User(**body)
    #     users = repositories["users"].save(oneUser)
    #     return "", 200
    @app.route("/api/users", methods=["POST"])
    def user_save_new():
        # No Auth
        body = request.json
        newUser = User(
            user_id=body["user_id"],
            first_name=body["first_name"],
            last_name=body["last_name"],
            email=body["email"],
        )

        repositories["users"].save(newUser)
        return "", 200

    @app.route("/api/users/<id>/publications", methods=["GET"])
    def users_get_publications_by_user_id(id):

        user_publication_list = repositories[
            "publications"
        ].search_publications_by_user_id(id)
        return object_to_json(user_publication_list), 200

    @app.route("/api/categories", methods=["GET"])
    def categories_get_all():

        categories_id_list = repositories["publications"].get_all_categories_id()
        return dumps(categories_id_list), 200

    return app
