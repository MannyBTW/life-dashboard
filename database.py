import sqlite3

DATABASE_NAME = "life_dashboard.db"

def create_database():
    with sqlite3.connect(DATABASE_NAME) as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL
            )
            """
        )


def add_note(title, content):
    with sqlite3.connect(DATABASE_NAME) as connection:
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO notes (title, content) VALUES (?, ?)",
            (title, content),
        )

        return cursor.lastrowid


def get_notes():
    with sqlite3.connect(DATABASE_NAME) as connection:
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM notes"
        )
        notes = cursor.fetchall()
        return notes

def get_id(title):
    with sqlite3.connect(DATABASE_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(
            '''SELECT * FROM notes
            WHERE title = ?''',
            (title,)
        )

def update_note(note_id, title, content):
    with sqlite3.connect(DATABASE_NAME) as connection:
        cursor = connection.cursor()

        cursor.execute(
            '''UPDATE notes
            SET 
            title = ?,
            content = ?
            WHERE id = ?
            ''',
            (title, content, note_id),
        )

  

def delete_note(note_id):
    with sqlite3.connect("life_dashboard.db") as connection:
        cursor = connection.cursor()

        cursor.execute(
            '''DELETE FROM notes
            WHERE id = ?''',
        (note_id,),
        )


