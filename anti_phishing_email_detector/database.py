import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "data", "detector.db")
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS emails (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender TEXT,
            subject TEXT,
            risk_score REAL,
            verdict TEXT,
            analyzed_at TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_email_history(sender, subject, risk_score, verdict):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO emails (sender, subject, risk_score, verdict, analyzed_at) VALUES (?, ?, ?, ?, ?)",
        (sender, subject, risk_score, verdict, datetime.now().isoformat())
    )
    conn.commit()
    conn.close()

def get_email_history(limit=50):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "SELECT id, sender, subject, risk_score, verdict FROM emails ORDER BY analyzed_at DESC LIMIT ?",
        (limit,)
    )
    rows = cur.fetchall()
    conn.close()
    return rows
