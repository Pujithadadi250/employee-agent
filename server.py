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
def home():
    return {"message": "Azure App Running"}

@app.get("/employees")
def employees():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM employees")

    rows = cur.fetchall()

    columns = [desc[0] for desc in cur.description]

    result = []

    for row in rows:
        result.append(dict(zip(columns, row)))

    cur.close()
    conn.close()

    return result