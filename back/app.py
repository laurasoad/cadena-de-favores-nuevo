import sqlite3
from src.domain.publication import PublicationRepository
from src.domain.user import UserRepository

from src.webserver import create_app


database_path = "data/database.db"

repositories = {
    "publications": PublicationRepository(database_path),
    "users": UserRepository(database_path),
}

app = create_app(repositories)

app.run(debug=True, host="0.0.0.0", port="5000")
