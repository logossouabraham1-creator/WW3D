import sqlite3
DATABASE_PATH = "data/ww3d.db"
def get_connection(Da):
    connection = sqlite3.connect(DATABASE_PATH)
    return connection