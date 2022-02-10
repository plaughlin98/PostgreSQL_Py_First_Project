import psycopg2
from psycopg2 import Error
from config import PASS

try:
    # Connect to the DB
    connection = psycopg2.connect(
                host = "localhost",
                user = "postgres",
                password = PASS,
                database = "laughlindb",
    )

    cur = connection.cursor()

    create_table_query = '''CREATE TABLE mobile
                (ID INT PRIMARY KEY     NOT NULL,
                MODEL           TEXT    NOT NULL,
                PRICE           REAL);'''

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cur.close()
        connection.close()
        print("PostgreSQL connection is closed")


#close
conn.close()