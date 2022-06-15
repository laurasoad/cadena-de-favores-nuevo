from src.lib.utils import temp_file
from src.domain.user import User, UserRepository
from src.webserver import create_app


def test_should_get_a_user_by_user_id():

    user_repository = UserRepository(temp_file())
    app = create_app(repositories={"users": user_repository})
    client = app.test_client()

    paco = User(
        user_id="user-1", first_name="Paco", last_name="Tilla", email="paco@outlook.es"
    )

    user_repository.save(paco)

    response = client.get("/api/users/user-1")

    assert response.json == {
        "user_id": "user-1",
        "first_name": "Paco",
        "last_name": "Tilla",
        "email": "paco@outlook.es",
    }
