from app.database.connection import get_connection


# GET ALL SUBJECTS
def get_all_subjects():
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM subjects")
        subjects = cursor.fetchall()
        return subjects
    finally:
        connection.close()


# CREATE A NEW SUBJECT
def create_subject(name, category):
    connection = get_connection()

    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO subjects (name, category) VALUES (?, ?)",
            (name, category)
        )
        connection.commit()
        subject_id = cursor.lastrowid
        return subject_id
    finally:
        connection.close()


# GET A SINGLE SUBJECT BY ID
def get_subject_by_id(subject_id):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM subjects WHERE id = ?",
            (subject_id,)
        )
        subject = cursor.fetchone()
        return subject
    finally:
        connection.close()


# UPDATE AN EXISTING SUBJECT
def update_subject(subject_id, name, category):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE subjects SET name = ?, category = ? WHERE id = ?",
            (name, category, subject_id)
        )
        connection.commit()
        updated = cursor.rowcount > 0
        return updated
    finally:
        connection.close()


# DELETE A SUBJECT BY ID
def delete_subject(subject_id):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            "DELETE FROM subjects WHERE id = ?",
            (subject_id,)
        )
        connection.commit()
        deleted = cursor.rowcount > 0
        return deleted
    finally:
        connection.close()
