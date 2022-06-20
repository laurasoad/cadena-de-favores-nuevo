from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.publication import Publication, PublicationRepository
from src.domain.tag import TagRepository, Tag


def test_search_publications_by_user_id_in_database():
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
    tag_repository.save(Tag(tag_id=4, name="#music"))

    # Relacionamos una publicación con sus Tags
    pub_repository.save_publication_tags("1", [1, 2, 3])

    publication_pepa = Publication(
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

    # ACT (real)
    pub_repository.save(publication_pepa)
    pub_repository.save_publication_tags("2", [1, 4])

    pepa_publication_list = pub_repository.search_publications_by_user_id("user-pepa")

    # COMPARACIÓN
    assert len(pepa_publication_list) == 1
    assert pepa_publication_list[0].to_dict()["id_pub"] == "2"
    assert pepa_publication_list[0].to_dict()["user_id"] == "user-pepa"
    assert pepa_publication_list[0].to_dict()["tags"] == [1, 4]


def test_search_publications_by_user_id_endpoint():
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
    tag_repository.save(Tag(tag_id=4, name="#music"))

    # Relacionamos una publicación con sus Tags
    pub_repository.save_publication_tags("1", [1, 2, 3])

    publication_pepa = Publication(
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
    pub_repository.save(publication_pepa)
    pub_repository.save_publication_tags("2", [1, 4])

    # ACT (real)
    response = client.get("/api/users/user-pepa/publications")
    # COMPARACIÓN
    json_response = response.json
    assert response.status_code == 200

    assert json_response[0]["id_pub"] == "2"
    assert json_response[0]["user_id"] == "user-pepa"
    assert json_response[0]["tags"] == [1, 4]
