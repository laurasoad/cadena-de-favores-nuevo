from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.publication import Publication, PublicationRepository
from src.domain.tag import TagRepository, Tag


def test_should_return_one_publication_by_id_in_database():
    tag_repository = TagRepository(temp_file())
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
    # Se crean varias Tags
    tag_repository.save(Tag(tag_id=1, name="#education"))
    tag_repository.save(Tag(tag_id=2, name="#math"))
    tag_repository.save(Tag(tag_id=3, name="#online"))

    # Relacionamos una publicación con sus Tags
    pub_repository.save_publication_tags("1", [1, 3])

    # ACT (real)
    response_user1_publication = client.get(
        "/api/publications/1", headers={"Authorization": "user-1"}
    )
    # COMPARACIÓN
    assert response_user1_publication.status_code == 200

    response_user1_publication = response_user1_publication.json

    assert response_user1_publication["id_pub"] == "1"
    assert response_user1_publication["user_id"] == "user-1"
    assert response_user1_publication["publication_type"] == 0
    assert response_user1_publication["title"] == "necesito clases de mates"
    assert (
        response_user1_publication["description"]
        == "hola me llamo Nerea y busco alguien que me dé clases por las tardes en Bilbao"
    )
    assert response_user1_publication["date"] == "2022-03-30"
    assert response_user1_publication["location"] == "Bilbao"
    assert response_user1_publication["category_id"] == "CAT_EDUCATION"
    assert response_user1_publication["tags"] == [1, 3]


def test_other_users_should_see_one_publication_by_id_and_its_detailss():
    tag_repository = TagRepository(temp_file())
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
            category_id="CAT_EDUCATION",
            tags=[],
        )
    )
    # Se crean varias Tags
    tag_repository.save(Tag(tag_id=1, name="#education"))
    tag_repository.save(Tag(tag_id=2, name="#math"))
    tag_repository.save(Tag(tag_id=3, name="#online"))

    # Relacionamos una publicación con sus Tags
    pub_repository.save_publication_tags("1", [1, 2, 3])

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
        "category_id": "CAT_EDUCATION",
        "tags": [1, 2, 3],
    }
