from mcp.server.fastmcp import FastMCP
import psycopg2

mcp = FastMCP("postgres-agent")

def get_connection():
    return psycopg2.connect(
        host="agentpostgres241.postgres.database.azure.com",
        database="postgres",
        user="pujitha",
        password="bahubali@1",
        port=5432,
        sslmode="require"
    )

@mcp.tool()
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

@mcp.tool()
def run_query(query: str):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(query)

    rows = cur.fetchall()

    columns = [desc[0] for desc in cur.description]

    result = []

    for row in rows:
        result.append(dict(zip(columns, row)))

    cur.close()
    conn.close()

    return result

if __name__ == "__main__":
    mcp.run()