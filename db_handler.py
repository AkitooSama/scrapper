import sqlite3
import config

def initialize_db():
    conn = sqlite3.connect(config.DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS images (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hashtag TEXT,
            image_url TEXT UNIQUE
        )
    """)
    conn.commit()
    conn.close()

def save_image_url(hashtag, url):
    conn = sqlite3.connect(config.DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO images (hashtag, image_url) VALUES (?, ?)", (hashtag, url))
    conn.commit()
    conn.close()
