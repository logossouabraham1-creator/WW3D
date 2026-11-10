import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DATABASE_PATH = BASE_DIR / "data" / "ww3d.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)

    # Return database rows that support column-name access.
    connection.row_factory = sqlite3.Row

    # Enable foreign-key enforcement for this connection.
    connection.execute("PRAGMA foreign_keys = ON")

    return connection
