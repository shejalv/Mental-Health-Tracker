import sqlite3

# Create the database and table if not exists
def init_database():
    conn = sqlite3.connect('emotions.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS emotion_log (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    emotion TEXT)''')
    conn.commit()
    conn.close()

# Log emotion to the database
def log_emotion(emotion):
    conn = sqlite3.connect('emotions.db')
    c = conn.cursor()
    c.execute("INSERT INTO emotion_log (timestamp, emotion) VALUES (datetime('now'), ?)", (emotion,))
    conn.commit()
    conn.close()

# Initialize database on import
init_database()
