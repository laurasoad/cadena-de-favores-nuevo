from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.publication import Publication, PublicationRepository


def test_should_delete_publication_by_id():
    pub_repository = PublicationRepository(temp_file())
    app = create_app(repositories={"publications": pub_repository})
    client = app.test_client()

    publication_example = Publication(
        id_pub="1",
        publication_type=0,
        title="necesito clases de mates",
        description="hola me llamo Nerea y busco alguien que me de clases por las tardes en Bilbao",
        date="2022-03-30",
        location="Bilbao",
    )
    publication_example2 = Publication(
        id_pub="2",
        publication_type=0,
        title="busco clases de piano",
        description="Me gustaría aprender a tocar el piano",
        date="2022-03-30",
        location="Deusto",
    )
    pub_repository.save(publication_example)
    pub_repository.save(publication_example2)

    pub_repository.delete(id="1")

    response = client.get("/api/publications")

    assert response.json == [
        {
            "id_pub": "2",
            "publication_type": 0,
            "title": "busco clases de piano",
            "description": "Me gustaría aprender a tocar el piano",
            "date": "2022-03-30",
            "location": "Deusto",
            "categories": [],
        }
    ]
