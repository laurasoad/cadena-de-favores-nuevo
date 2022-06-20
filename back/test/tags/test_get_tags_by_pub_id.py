from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.publication import Publication, PublicationRepository
from src.domain.tag import TagRepository, Tag


def test_get_all_tags_endpoint():

    tag_repository = TagRepository(temp_file())
    app = create_app(repositories={"tags": tag_repository})
    client = app.test_client()

    tag_repository.save(Tag(tag_id=1, name="#education"))
    tag_repository.save(Tag(tag_id=2, name="#math"))
    tag_repository.save(Tag(tag_id=3, name="#online"))

    # ACT (real)
    response = client.get("/api/tags")

    # COMPARACIÓN
    assert response.status_code == 200

    # response_user1_publication = response_user1_publication.json   assert response["id_pub"] == "1"
    assert response.json[0] == {"tag_id": 1, "name": "#education"}
    assert response.json[1] == {"tag_id": 2, "name": "#math"}


def test_get_all_tags_method():

    tag_repository = TagRepository(temp_file())
    pub_repository = PublicationRepository(temp_file())
    app = create_app(repositories={"tags": tag_repository})
    client = app.test_client()

    # SET UP (lo esperado)

    # ["#education", "#math", "#online"]
    tag_repository.save(Tag(tag_id=1, name="#education"))
    tag_repository.save(Tag(tag_id=2, name="#math"))
    tag_repository.save(Tag(tag_id=3, name="#online"))

    # pub_repository.add_tag("1", ["#education", "#math", "#online"])
    # ACT (real)
    tag_list = tag_repository.get_all_tags()

    # COMPARACIÓN

    # response_user1_publication = response_user1_publication.json   assert response["id_pub"] == "1"
    assert tag_list[0].to_dict() == {"tag_id": 1, "name": "#education"}
    assert tag_list[1].to_dict() == {"tag_id": 2, "name": "#math"}
