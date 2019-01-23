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

create_table_query = '''CREATE TABLE main_data_s
(SYSBP  TEXT NOT NULL ,
USUBJID  TEXT NOT NULL ,
VISIT  TEXT NOT NULL ,
SITEID TEXT NOT NULL ,
COUNTRY TEXT NOT NULL ,
SEX TEXT NOT NULL ,
AGE TEXT NOT NULL ,
RACE TEXT NOT NULL ,
DBP TEXT NOT NULL ,
HR TEXT NOT NULL ,
WEIGHT TEXT NOT NULL,
HEIGHT TEXT NOT NULL,
TEMP TEXT NOT NULL,
feed_back TEXT NOT NULL);'''

cursor.execute(create_table_query)
connection.commit()
