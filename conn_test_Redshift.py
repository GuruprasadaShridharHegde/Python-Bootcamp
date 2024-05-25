import psycopg2

db_host = ''
db_port = ''
db_name = ''
db_user = ''
db_password = ''

try:
    conn = psycopg2.connect(
        host=db_host,
        port=db_port,
        dbname=db_name,
        user=db_user,
        password=db_password
    )
    print("Connection successful!")
    cursor = conn.cursor()
    
    
    cursor.close()
    conn.close()
except Exception as e:
    print("Connection failed:", e)