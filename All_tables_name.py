import psycopg2
from psycopg2 import Error



connection = psycopg2.connect(user = "monk",
                                  password = "monk12",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "postgres")
cursor = connection.cursor()

cursor.execute("""SELECT table_name FROM information_schema.tables
                  WHERE table_schema = 'public'""")
                  
for table in cursor.fetchall():
    print(table)
