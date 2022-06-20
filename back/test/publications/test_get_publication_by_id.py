from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.publication import Publication, PublicationRepository


def test_should_return_one_publication_by_id_in_database():
    pub_repository = PublicationRepository(temp_file())
    app = create_app(repositories={"publications": pub_repository})
    client = app.test_client()

    # SET UP (lo esperado)
    pub_repository.save(
        Publication(
            id_pub="1",
            user_id="user-1",
            publication_type=0,
            title="necesito clases de mates",
            description="hola me llamo Nerea y busco alguien que me dé clases por las tardes en Bilbao",
            date="2022-03-30",
            location="Bilbao",
            category_id="CAT_EDUCATION",
            tags=["#education", "#math", "#online"],
        )
    )

    # ACT (real)
    response_user1_publication = client.get(
        "/api/publications/1", headers={"Authorization": "user-1"}
    )

    # COMPARACIÓN
    assert response_user1_publication.status_code == 200
    assert response_user1_publication.json == {
        "id_pub": "1",
        "user_id": "user-1",
        "publication_type": 0,
        "title": "necesito clases de mates",
        "description": "hola me llamo Nerea y busco alguien que me de clases por las tardes en Bilbao",
        "date": "2022-03-30",
        "location": "Bilbao",
        "category_id": "CAT_EDUCATION",
        "categories": [["#education", "#math", "#online"]],
    }


def test_other_users_should_see_one_publication_by_id_and_its_detailss():
    pub_repository = PublicationRepository(temp_file())
    app = create_app(repositories={"publications": pub_repository})
    client = app.test_client()

    # SET UP (lo esperado)
    pub_repository.save(
        Publication(
            id_pub="1",
            user_id="user-1",
            publication_type=0,
            title="necesito clases de mates",
            description="hola me llamo Nerea y busco alguien que me de clases por las tardes en Bilbao",
            date="2022-03-30",
            location="Bilbao",
        )
    )

    # ACT (real)
    response_user1_publication = client.get(
        "/api/publications/1", headers={"Authorization": "other-user"}
    )

    # COMPARACIÓN
    json_response = response_user1_publication.json
    assert response_user1_publication.status_code == 200

    assert json_response["id_pub"] == "1"
    assert json_response == {
        "id_pub": "1",
        "user_id": "user-1",
        "publication_type": 0,
        "title": "necesito clases de mates",
        "description": "hola me llamo Nerea y busco alguien que me de clases por las tardes en Bilbao",
        "date": "2022-03-30",
        "location": "Bilbao",
        "categories": [],
    }
