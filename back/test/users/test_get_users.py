from src.lib.utils import temp_file
from src.domain.user import User, UserRepository
from src.webserver import create_app


def test_should_return_empty_list_of_users():
    user_repository = UserRepository(temp_file())
    app = create_app(repositories={"users": user_repository})
    client = app.test_client()

    response = client.get("/api/users")

    assert response.json == []


def test_should_resturn_list_of_users():
    # ARRANGE (given)
    user_repository = UserRepository(temp_file())
    app = create_app(repositories={"users": user_repository})
    client = app.test_client()

    paco = User(
        id="user-1",
        name="Paco",
    )

    pepa = User(
        id="user-2",
        name="Pepa",
    )

    user_repository.save(paco)
    user_repository.save(pepa)
    # ACT
    response = client.get("/api/users")

    # ASSERT
    assert response.json == [
        {
            "id": "user-1",
            "name": "Paco",
        },
        {
            "id": "user-2",
            "name": "Pepa",
        },
    ]
