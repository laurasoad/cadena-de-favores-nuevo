from crypt import methods
from flask import Flask, request
from flask_cors import CORS
from src.domain.publication import Publication

from src.lib.utils import object_to_json


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "...magic!"

    @app.route("/api/publications", methods=["GET"])
    def pub_get_all():
        pub_list = repositories["publications"].get_publications()
        return object_to_json(pub_list)

    @app.route("/api/publications/<id>", methods=["GET"])
    def pub_get_by_id(id):
        publication = repositories["publications"].get_publication_by_id(id)
        return object_to_json(publication)

    @app.route("/api/publications/<id>", methods=["PUT"])
    def pub_edit_by_id(id):
        publication_diccionary = request.json
        categories_to_extract = publication_diccionary.pop("categories")
        publication = Publication(**publication_diccionary)

        repositories["publications"].edit_publication(publication)
        return ""

    @app.route("/api/publications", methods=["POST"])
    def pub_save_new():
        body = request.json
        newPublication = Publication(**body)
        repositories["publications"].save(newPublication)
        return "", 200

    @app.route("/api/users", methods=["GET"])
    def users_get_all():
        users = repositories["users"].get_all()
        return object_to_json(users)

    return app
