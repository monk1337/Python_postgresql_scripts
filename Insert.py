import psycopg2
from psycopg2 import Error

table_name = 'something_else'

connection = psycopg2.connect(user = "monk",
                                  password = "monk12",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "postgres")
cursor = connection.cursor()

insert = ()
insert = ('first','second','third','forth','hi5','gh6','rt7','es8','rf9')
postgres_insert_query = """INSERT INTO feed_back_table_s (feedback_id,log_id,patinet_id,visit,suggestion,comments,created_by,created_on,comment_type) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
cursor.execute(postgres_insert_query, insert)
connection.commit()
