from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.publication import Publication, PublicationRepository


def test_should_return_info_in_database():
    pub_repository = PublicationRepository(temp_file())
    app = create_app(repositories={"publications": pub_repository})
    client = app.test_client()

    pub_repository.save(
        Publication(
            id_pub="1",
            publication_type=0,
            title="necesito clases de mates",
            description="hola me llamo Nerea y busco alguien que me de clases por las tardes en Bilbao",
            date="2022-03-30",
            location="Bilbao",
        )
    )

    response = client.get("/api/publications/1")
    assert response.json == {
        "id_pub": "1",
        "publication_type": 0,
        "title": "necesito clases de mates",
        "description": "hola me llamo Nerea y busco alguien que me de clases por las tardes en Bilbao",
        "date": "2022-03-30",
        "location": "Bilbao",
        "categories": [],
    }
