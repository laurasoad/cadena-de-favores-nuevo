from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.publication import Publication, PublicationRepository
from src.domain.tag import TagRepository, Tag


def test_should_add_tags_to_publication():

    tag_repository = TagRepository(temp_file())
    pub_repository = PublicationRepository(temp_file())
    app = create_app(
        repositories={"publications": pub_repository, "tags": tag_repository}
    )
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
            tags=[],
        )
    )
    # ["#education", "#math", "#online"]
    tag_repository.save(Tag(tag_id=1, name="#education"))
    tag_repository.save(Tag(tag_id=2, name="#math"))
    tag_repository.save(Tag(tag_id=3, name="#online"))

    # ACT (real)
    pub_repository.save_publication_tags("1", [1, 2, 3])

    publication_returned = pub_repository.get_publication_by_id("1")
    response = client.get("/api/tags")

    # COMPARACIÓN
    assert response.status_code == 200

    # response_user1_publication = response_user1_publication.json   assert response["id_pub"] == "1"

    assert publication_returned.tags == [1, 2, 3]
    assert publication_returned.id_pub == "1"
    assert publication_returned.title == "necesito clases de mates"
