import sys

sys.path.insert(0, "")


def main():

    from src.domain.publication import Publication, PublicationRepository
    from src.domain.user import User, UserRepository

    database_path = "data/database.db"

    user_repository = UserRepository(database_path)

    homero = User(
        user_id="user-1",
        first_name="Homer",
        last_name="Simpson",
        email="homer@gmail.com",
    )

    lisa = User(
        user_id="user-2",
        first_name="Lisa",
        last_name="Simpson",
        email="lisa@gmail.com",
    )

    ruth = User(
        user_id="user-3",
        first_name="Ruth",
        last_name="D",
        email="ruti@gmail.com",
    )

    jeff = User(
        user_id="user-4",
        first_name="Jeff",
        last_name="No bin",
        email="jjohan@gmail.com",
    )

    user_repository.save(homero)
    user_repository.save(lisa)
    user_repository.save(ruth)
    user_repository.save(jeff)

    pub_repository = PublicationRepository(database_path)
    pub_repository.save(
        Publication(
            id_pub="1",
            user_id="user-1",
            publication_type=0,
            title="Busco clases de mates",
            description="Busco alguien que me dé clases por las tardes en Bilbao",
            date="2022-03-29",
            location="Bilbao",
        )
    )

    pub_repository.save(
        Publication(
            id_pub="2",
            user_id="user-2",
            publication_type=1,
            title="Ofrezco clases de mates",
            description="Licenciada en matematicas se ofrece a dar clases",
            date="2022-03-30",
            location="Bilbao",
        )
    )

    pub_repository.save(
        Publication(
            id_pub="3",
            user_id="user-3",
            publication_type=1,
            title="Ofrezco clases de guitarra",
            description="¿Te apetece iniciarte en el mundo de la guitarra? háblame!",
            date="2022-03-28",
            location="Online",
        )
    )

    pub_repository.save(
        Publication(
            id_pub="4",
            user_id="user-1",
            publication_type=0,
            title="Necesito que cuiden a mi hijo el fin de semana",
            description="bla bla bla",
            date="2022-03-29",
            location="Donosti",
        )
    )
    pub_repository.save(
        Publication(
            id_pub="5",
            user_id="user-4",
            publication_type=0,
            title="Necesito que reparen mi lavadora",
            description="Creo que tiene el tambor estropeado",
            date="2022-06-11",
            location="Getxo",
        )
    )
    pub_repository.save(
        Publication(
            id_pub="6",
            user_id="user-3",
            publication_type=0,
            title="Ofrezco clases de administración",
            description="Gradudada en administración ofrece clases, tengo disponibilidad los fines de semana",
            date="2022-06-12",
            location="Portugalete",
        )
    )


if __name__ == "__main__":
    main()
