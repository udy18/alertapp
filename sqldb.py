import sqlite3

sqlite_db_file = 'contacts.db'

def setup_database():
    try:
        conn = sqlite3.connect(sqlite_db_file)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY,
                phone TEXT NOT NULL,
                address TEXT NOT NULL
            )
        ''')
        conn.commit()
        print("Database setup completed.")
    except sqlite3.Error as e:
        print(f"An error occurred while setting up the database: {e}")
    finally:
        if conn:
            conn.close()

def populate_database():
    contacts = [
        ('+918939800035','4th seaward road, thiruvanmiyur, chennai'),
        ('+919188205857','Hindustan Institute Of technology, chennai'),
        ('+91 75989 39568','pallikaranai'),
        ('+91 97899 23414','252/236, Jutkapuram, Periyamet, Chennai, Tamil Nadu 600003')
    ]

    try:
        conn = sqlite3.connect(sqlite_db_file)
        cursor = conn.cursor()
        cursor.executemany('INSERT INTO contacts (phone, address) VALUES (?, ?)', contacts)
        conn.commit()
        print("Database population completed.")
    except sqlite3.Error as e:
        print(f"An error occurred while populating the database: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    setup_database()
    populate_database()
