import psycopg2
from psycopg2 import Error

table_name = 'something_else'
uniqu_name = 'pas'

connection = psycopg2.connect(user = "monk",
                                  password = "monk12",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "postgres")
cursor = connection.cursor()
cursor.execute("Select * FROM model_result")
colnames = [desc[0] for desc in cursor.description]
print(colnames)
