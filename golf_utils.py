import sqlite3
import pandas as pd

DB_PATH = 'open_scores.db'

def connect_db():
    return sqlite3.connect(DB_PATH)

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY,
            player TEXT,
            course TEXT,
            year INTEGER,
            round INTEGER,
            score INTEGER,
            weather TEXT,
            wind_kph REAL,
            hole_difficulty TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_score(player, course, year, round_num, score, weather, wind_kph, difficulty):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO scores (player, course, year, round, score, weather, wind_kph, hole_difficulty)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (player, course, year, round_num, score, weather, wind_kph, difficulty))
    conn.commit()
    conn.close()

def import_csv(filepath):
    df = pd.read_csv(filepath)
    conn = connect_db()
    df.to_sql('scores', conn, if_exists='append', index=False)
    conn.close()

def export_csv(filepath):
    conn = connect_db()
    df = pd.read_sql_query('SELECT * FROM scores', conn)
    df.to_csv(filepath, index=False)
    conn.close()

def get_all_scores():
    conn = connect_db()
    df = pd.read_sql_query("SELECT * FROM scores", conn)
    conn.close()
    return df
