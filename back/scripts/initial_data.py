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
        last_name="Simpsons",
        email="homer@gmail.es",
    )

    lisa = User(
        user_id="user-2",
        first_name="Lisa",
        last_name="Simpsons",
        email="lisa@gmail.es",
    )

    jeff = User(
        user_id="user-3",
        first_name="JJ",
        last_name="No binario",
        email="jjoh@gmail.es",
    )

    user_repository.save(homero)
    user_repository.save(lisa)
    user_repository.save(jeff)

    pub_repository = PublicationRepository(database_path)
    pub_repository.save(
        Publication(
            id_pub="1",
            user_id="user-1",
            publication_type=0,
            title="necesito clases de mates",
            description="busco alguien que me de clases por las tardes en Bilbao",
            date="2022-03-29",
            location="Bilbao",
        )
    )

    pub_repository.save(
        Publication(
            id_pub="2",
            user_id="user-2",
            publication_type=1,
            title="ofrezco clases de mates",
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
            title="ofrezco clases de guitarra",
            description="¿te apetece iniciarte en el mundo de la guitarra? háblame!",
            date="2022-03-28",
            location="Online",
        )
    )

    pub_repository.save(
        Publication(
            id_pub="4",
            user_id="user-1",
            publication_type=0,
            title="necesito que vegan a cuidar de mi hijo los fines de semana",
            description="bla bla bla",
            date="2022-03-29",
            location="Donosti",
        )
    )


if __name__ == "__main__":
    main()
