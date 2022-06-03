from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.publication import Publication, PublicationRepository


def test_repository_method_should_edit_publication_by_id():
    pub_repository = PublicationRepository(temp_file())
    app = create_app(repositories={"publications": pub_repository})
    client = app.test_client()

    initial_publication = Publication(
        id_pub="1",
        user_id="user-1",
        publication_type=0,
        title="necesito clases de mates",
        description="hola me llamo Nerea y busco alguien que me de clases por las tardes en Bilbao",
        date="2022-03-30",
        location="Bilbao",
    )
    pub_repository.save(initial_publication)

    modified_publication = Publication(
        id_pub="1",
        user_id="user-1",
        publication_type=0,
        title="título editado",
        description="descripción editada",
        date="2022-03-30",
        location="lugar editado",
    )
    # EJECUTAR MÉTODO EDIT del REPOSITORIO (se manda objeto Publication)
    pub_repository.edit_publication(modified_publication)

    # COMPARACIÓN
    response_user1_edit = client.get(
        "/api/publications/1", headers={"Authorization": "user-1"}
    )

    response_json = response_user1_edit.json

    # Compara el json por claves
    assert response_json["id_pub"] == "1"
    assert response_json["user_id"] == "user-1"
    assert response_json["publication_type"] == 0
    assert response_json["title"] == "título editado"
    assert response_json["description"] == "descripción editada"
    assert response_json["date"] == "2022-03-30"
    assert response_json["location"] == "lugar editado"
    assert response_json["categories"] == []

    # Compara el json entero
    assert response_json == {
        "id_pub": "1",
        "user_id": "user-1",
        "publication_type": 0,
        "title": "título editado",
        "description": "descripción editada",
        "date": "2022-03-30",
        "location": "lugar editado",
        "categories": [],
    }


def test_server_should_edit_publication_by_id_using_put_method():
    pub_repository = PublicationRepository(temp_file())
    app = create_app(repositories={"publications": pub_repository})
    client = app.test_client()

    initial_publication = Publication(
        id_pub="1",
        user_id="user-1",
        publication_type=0,
        title="necesito clases de mates",
        description="hola me llamo Nerea y busco alguien que me de clases por las tardes en Bilbao",
        date="2022-03-30",
        location="Bilbao",
    )
    pub_repository.save(initial_publication)

    modified_publication = Publication(
        id_pub="1",
        user_id="user-1",
        publication_type=0,
        title="título editado",
        description="descripción editada",
        date="2022-03-30",
        location="lugar editado",
    )
    modified_pub_json = modified_publication.to_dict()

    # EJECUTAR MÉTODO PUT del SERVIDOR (se envía objeto en formato JSON)
    sending_put = client.put(
        "/api/publications/1",
        json=modified_pub_json,
        headers={"Authorization": "user-1"},
    )

    # COMPARACIÓN
    response_user1_edit = client.get(
        "/api/publications/1", headers={"Authorization": "user-1"}
    )

    response_json = response_user1_edit.json

    assert response_user1_edit.status_code == 200

    assert response_json["id_pub"] == "1"
    assert response_json["user_id"] == "user-1"
    assert response_json["publication_type"] == 0
    assert response_json["title"] == "título editado"
    assert response_json["description"] == "descripción editada"
    assert response_json["date"] == "2022-03-30"
    assert response_json["location"] == "lugar editado"
    assert response_json["categories"] == []


def test_other_user_should_not_edit_other_user_publication():
    pub_repository = PublicationRepository(temp_file())
    app = create_app(repositories={"publications": pub_repository})
    client = app.test_client()

    initial_publication = Publication(
        id_pub="1",
        user_id="user-1",
        publication_type=0,
        title="título no editado",
        description="descripción no editada",
        date="2022-03-30",
        location="lugar no editado",
    )
    pub_repository.save(initial_publication)

    # other user

    modified_publication = Publication(
        id_pub="1",
        user_id="user-1",
        publication_type=0,
        title="otro título",
        description="hola",
        date="2022-03-30",
        location="otro lugar",
    )
    # EJECUTAR MÉTODO EDIT del REPOSITORIO (se manda objeto Publication)
    # pub_repository.edit_publication(modified_publication)

    # EJECUTAR MÉTODO PUT del SERVIDOR (se envía objeto en formato JSON)
    modified_pub_json = modified_publication.to_dict()
    sending_put = client.put(
        "/api/publications/1",
        json=modified_pub_json,
        headers={"Authorization": "other-user"},
    )

    # COMPARACIÓN
    response_user1_edit = client.get(
        "/api/publications/1", headers={"Authorization": "user-1"}
    )

    response_json = response_user1_edit.json

    assert sending_put.status_code == 403

    # Compara el json por claves
    assert response_json["id_pub"] == "1"
    assert response_json["user_id"] == "user-1"
    assert response_json["publication_type"] == 0
    assert response_json["title"] == "título no editado"
    assert response_json["description"] == "descripción no editada"
    assert response_json["date"] == "2022-03-30"
    assert response_json["location"] == "lugar no editado"
    assert response_json["categories"] == []

    # Compara el json entero
    assert response_json == {
        "id_pub": "1",
        "user_id": "user-1",
        "publication_type": 0,
        "title": "título no editado",
        "description": "descripción no editada",
        "date": "2022-03-30",
        "location": "lugar no editado",
        "categories": [],
    }
