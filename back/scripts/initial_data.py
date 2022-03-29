def main():
    import sys

    sys.path.insert(0, "")

    from src.domain.publication import Publication, PublicationRepository

    database_path = "data/database.db"

    pub_repository = PublicationRepository(database_path)
    pub_repository.save(
        Publication(
            id_pub="1",
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
            publication_type=0,
            title="necesito que vegan a cuidar de mi hijo los fines de semana",
            description="bla bla bla",
            date="2022-03-29",
            location="Donosti",
        )
    )


if __name__ == "__main__":
    main()
