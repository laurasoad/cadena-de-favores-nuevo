from flask import Flask, request
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
        )

        repositories["publications"].save(newPublication)
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

        categories_to_extract = body.pop("categories")
        publication = Publication(
            id_pub=body["id_pub"],
            user_id=user_id_auth,
            publication_type=body["publication_type"],
            title=body["title"],
            description=body["description"],
            date=body["date"],
            location=body["location"],
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

    # USERS

    @app.route("/api/users", methods=["GET"])
    def users_get_all():
        users = repositories["users"].get_all()
        return object_to_json(users)

    @app.route("/api/users", methods=["POST"])
    def users_save():
        body = request.json
        oneUser = User(**body)
        users = repositories["users"].save(oneUser)
        return "", 200

    @app.route("/api/users/<id>", methods=["GET"])
    def users_get_by_id(id):
        users = repositories["users"].get_by_id(id)
        return object_to_json(users)

    return app
