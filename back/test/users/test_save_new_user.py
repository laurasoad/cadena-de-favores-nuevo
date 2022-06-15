from src.lib.utils import temp_file
from src.domain.user import User, UserRepository
from src.webserver import create_app


def test_should_save_a_user_repository_method():
    # ARRANGE (given)
    user_repository = UserRepository(temp_file())
    app = create_app(repositories={"users": user_repository})
    client = app.test_client()

    paco = User(
        user_id="user-1", first_name="Paco", last_name="G", email="paco@outlook.es"
    )

    user_repository.save(paco)

    response = client.get("/api/users/user-1")

    assert response.status_code == 200
    assert response.json["user_id"] == "user-1"
    assert response.json["first_name"] == "Paco"


def test_should_save_a_user_endpoint_webserver():
    # ARRANGE (given)
    user_repository = UserRepository(temp_file())
    app = create_app(repositories={"users": user_repository})
    client = app.test_client()

    lisa = User(
        user_id="user-2", first_name="Lisa", last_name="S", email="lisa@outlook.es"
    )

    lisa_json = lisa.to_dict()
    print(lisa_json)
    # response = client.post("/api/process/diagnostic/exit", json=lisa)

    sending_post = client.post("/api/users", json=lisa_json)

    response = client.get("/api/users/user-2")

    assert sending_post.status_code == 200
    assert response.status_code == 200
    assert response.json["user_id"] == "user-2"
    assert response.json["first_name"] == "Lisa"
