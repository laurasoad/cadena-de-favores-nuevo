from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.publication import Publication, PublicationRepository
from src.domain.tag import Tag, TagRepository


def test_repository_method_should_edit_publication_by_id():
    tag_repository = TagRepository(temp_file())
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
        category_id="CAT_EDUCATION",
        tags=[],
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
        category_id="CAT_MODIFICADA",
        tags=[],
    )

    # EJECUTAR MÉTODO EDIT del REPOSITORIO (se manda objeto Publication)
    # 1º Se edita la publicación 2º Se editan las tags (Si no, el endpoint PUT las borra)
    pub_repository.edit_publication(modified_publication)
    # Modificamos la lista de tags
    tag_repository.save(Tag(tag_id=1, name="#education"))
    pub_repository.save_publication_tags("1", [1])

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
    assert response_json["category_id"] == "CAT_MODIFICADA"
    assert response_json["location"] == "lugar editado"
    assert response_json["tags"] == [1]

    # Compara el json entero
    assert response_json == {
        "id_pub": "1",
        "user_id": "user-1",
        "publication_type": 0,
        "title": "título editado",
        "description": "descripción editada",
        "date": "2022-03-30",
        "location": "lugar editado",
        "category_id": "CAT_MODIFICADA",
        "tags": [1],
    }


def test_server_should_edit_publication_by_id_using_put_method():
    tag_repository = TagRepository(temp_file())
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
        category_id="CAT_EDUCATION",
        tags=[],
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
        category_id="CAT_MODIFICADA",
        tags=[],
    )

    modified_pub_json = modified_publication.to_dict()

    # EJECUTAR MÉTODO PUT del SERVIDOR (se envía objeto en formato JSON)
    # 1º Se edita la publicación 2º Se editan las tags (Si no, el endpoint PUT las borra)
    sending_put = client.put(
        "/api/publications/1",
        json=modified_pub_json,
        headers={"Authorization": "user-1"},
    )
    # 2º Se editan las tags
    tag_repository.save(Tag(tag_id=1, name="#education"))
    pub_repository.save_publication_tags("1", [1])

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
    assert response_json["category_id"] == "CAT_MODIFICADA"
    assert response_json["tags"] == [1]


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
        category_id="CAT_NO_EDITADA",
        tags=[],
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
        category_id="CAT_OTRA",
        tags=[],
    )

    pub_repository.save_publication_tags("1", [1])
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
