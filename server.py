from fastapi import FastAPI
import psycopg2

app = FastAPI()

def get_connection():
    return psycopg2.connect(
        host="agentpostgres241.postgres.database.azure.com",
        database="postgres",
        user="pujitha",
        password="bahubali@1",
        port=5432,
        sslmode="require"
    )

@app.get("/")
def root():
    return {"message": "MCP Server Running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/tables")
def list_tables():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema='public'
    """)

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [row[0] for row in rows]