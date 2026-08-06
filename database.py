import sqlite3

DATABASE_NAME = "life_dashboard.db"

def create_database():
    with sqlite3.connect(DATABASE_NAME) as connection:
        cursor = connection.cursor()

        #Create notes table
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL
            )
            """
        )
        #Create habits table
        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS habits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )'''
        )

        #Create habits completed table
        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS completed_habits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                habit_id INTEGER,
                name TEXT NOT NULL
            )'''
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
    with sqlite3.connect(DATABASE_NAME) as connection:
        cursor = connection.cursor()

        cursor.execute(
            '''DELETE FROM notes
            WHERE id = ?''',
        (note_id,),
        )

def add_habit(name):
    with sqlite3.connect(DATABASE_NAME) as connection:
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO habits (name) VALUES (?)",
            (name,)
        )

def get_habits():
    with sqlite3.connect(DATABASE_NAME) as connection:
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM habits"
        )
        habits = cursor.fetchall()
        return habits

def complete_habit(habit_id, date):
    with sqlite3.connect(DATABASE_NAME) as connection:
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO completed_habits (habit_id, date) VALUES (?, ?)",
            (habit_id, date)
        )

def get_completed_habit_ids(date):
    with sqlite3.connect(DATABASE_NAME) as connection:
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM completed_habits"
        )
        return cursor.fetchall()

def delete_habit(habit_id):
    with sqlite3.connect(DATABASE_NAME) as connection:
        cursor = connection.cursor()

        cursor.execute(
            '''DELETE FROM habits
            WHERE id = ?''',
            (habit_id,),
        )