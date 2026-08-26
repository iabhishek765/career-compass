from pathlib import Path
import sqlite3


# Project Root
BASE_DIR = Path(__file__).resolve().parents[2]

# Database File
DATABASE_PATH = BASE_DIR / "career_compass.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)

    connection.row_factory = sqlite3.Row

    return connection