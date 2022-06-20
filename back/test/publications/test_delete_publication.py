from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.publication import Publication, PublicationRepository


def test_should_delete_one_publication_by_id():
    pub_repository = PublicationRepository(temp_file())
    app = create_app(repositories={"publications": pub_repository})
    client = app.test_client()

    publication_example = Publication(
        id_pub="1",
        user_id="user-pepa",
        publication_type=0,
        title="necesito clases de mates",
        description="hola me llamo Nerea y busco alguien que me de clases por las tardes en Bilbao",
        date="2022-03-30",
        location="Bilbao",
        category_id="CAT_EDUCATION",
        tags=[],
    )
    publication_example2 = Publication(
        id_pub="2",
        user_id="user-pepa",
        publication_type=0,
        title="busco clases de piano",
        description="Me gustaría aprender a tocar el piano",
        date="2022-03-30",
        location="Deusto",
        category_id="CAT_MUSIC",
        tags=[],
    )
    # pub_repository.save(publication_example)
    # pub_repository.save(publication_example2)
    sending_post = client.post(
        "/api/publications",
        json=publication_example.to_dict(),
        headers={"Authorization": "user-pepa"},
    )
    sending_post2 = client.post(
        "/api/publications",
        json=publication_example2.to_dict(),
        headers={"Authorization": "user-pepa"},
    )

    pub_repository.delete_by_id(id="1")

    response = client.get("/api/publications")

    assert response.json == [
        {
            "id_pub": "2",
            "user_id": "user-pepa",
            "publication_type": 0,
            "title": "busco clases de piano",
            "description": "Me gustaría aprender a tocar el piano",
            "date": "2022-03-30",
            "location": "Deusto",
            "category_id": "CAT_MUSIC",
            "tags": [],
        }
    ]


def test_server_should_not_allow_one_unauthorized_user_to_delete_a_publication():
    pub_repository = PublicationRepository(temp_file())
    app = create_app(repositories={"publications": pub_repository})
    client = app.test_client()

    publication_example = Publication(
        id_pub="1",
        user_id="user-pepa",
        publication_type=0,
        title="necesito clases de mates",
        description="hola me llamo Pepa y busco alguien que me de clases por las tardes en Bilbao",
        date="2022-03-30",
        location="Bilbao",
        category_id="CAT_EDUCATION",
        tags=[],
    )
    publication_example2 = Publication(
        id_pub="2",
        user_id="user-pepa",
        publication_type=0,
        title="busco clases de piano",
        description="Me gustaría aprender a tocar el piano",
        date="2022-03-30",
        location="Deusto",
        category_id="CAT_MUSIC",
        tags=[],
    )
    # pub_repository.save(publication_example)
    # pub_repository.save(publication_example2)
    sending_post = client.post(
        "/api/publications",
        json=publication_example.to_dict(),
        headers={"Authorization": "user-pepa"},
    )
    sending_post2 = client.post(
        "/api/publications",
        json=publication_example2.to_dict(),
        headers={"Authorization": "user-pepa"},
    )

    response = client.delete(
        "/api/publications/2",
        json=publication_example2.to_dict(),
        headers={"Authorization": "other_user_not_allowed"},
    )

    assert response.status_code == 403
