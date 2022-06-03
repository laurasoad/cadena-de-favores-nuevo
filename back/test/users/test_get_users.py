from src.lib.utils import temp_file
from src.domain.user import User, UserRepository
from src.webserver import create_app


def test_should_return_empty_list_of_users():
    user_repository = UserRepository(temp_file())
    app = create_app(repositories={"users": user_repository})
    client = app.test_client()

    response = client.get("/api/users")

    assert response.json == []


def test_should_save_a_user():
    # ARRANGE (given)
    user_repository = UserRepository(temp_file())
    app = create_app(repositories={"users": user_repository})
    client = app.test_client()

    paco = User(
        user_id="user-1", first_name="Paco", last_name="Tilla", email="paco@outlook.es"
    )

    user_repository.save(paco)

    response = client.get("/api/users/user-1")

    assert response.status_code == 200


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


def test_should_return_list_of_users():
    # ARRANGE (given)
    user_repository = UserRepository(temp_file())
    app = create_app(repositories={"users": user_repository})
    client = app.test_client()

    paco = User(
        user_id="user-1", first_name="Paco", last_name="Tilla", email="paco@outlook.es"
    )

    pepa = User(
        user_id="user-2",
        first_name="Pepa",
        last_name="Flores",
        email="flores@outlook.es",
    )

    user_repository.save(paco)
    user_repository.save(pepa)
    # ACT
    response = client.get("/api/users")

    # ASSERT
    assert response.json == [
        {
            "user_id": "user-1",
            "first_name": "Paco",
            "last_name": "Tilla",
            "email": "paco@outlook.es",
        },
        {
            "user_id": "user-2",
            "first_name": "Pepa",
            "last_name": "Flores",
            "email": "flores@outlook.es",
        },
    ]
