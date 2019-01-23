import psycopg2


table_name = 'something_else'
uniqu_name = 'pas'

connection = psycopg2.connect(user = "monk",
                                  password = "monk12",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "postgres")

first_ = 'cd2'
second_ = 'ef3'

# sql_update_query = """Update feed_back_table_s set comment_type = %s where log_id = %s and patinet_id = %s and visit = %s"""

cursor = connection.cursor()
postgreSQL_select_Query = """select * from feed_back_table_s where log_id = %s and patinet_id = %s"""
cursor.execute(postgreSQL_select_Query,(first_,second_))
model_records = cursor.fetchall()
print(model_records)

        
