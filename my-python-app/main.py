from fastapi import FastAPI
import psycopg2
import os
import time

app = FastAPI()

# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST", "postgres-0.postgres-db")
DB_NAME = os.getenv("DB_NAME", "postgres")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "mypassword")

def get_db_connection():
    while True:
        try:
            conn = psycopg2.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASS
            )
            return conn
        except Exception as e:
            print(f"Database not ready yet... {e}")
            time.sleep(2)

@app.get("/")
def read_root():
    return {"message": "Hello Haifa! FastAPI is connected to PostgreSQL on your Homelab."}

@app.get("/db-version")
def get_version():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT version();')
    db_version = cur.fetchone()
    cur.close()
    conn.close()
    return {"postgresql_version": db_version[0]}
