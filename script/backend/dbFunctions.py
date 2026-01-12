from psycopg2 import (
    connect, 
    DatabaseError)
from config import load_config

def insertExceptions(exception: str):
    try:
        with connect(**config) as conn:
            conn.autocommit = True
            cursor = conn.cursor()
            sql = '''INSERT INTO error_logs (id, timestamp, exception) VALUES ("%s"); ''', str(exception)
            cursor.execute(sql)
            conn.commit()
            conn.close()
    except (DatabaseError, Exception) as dbError:
        return dbError

if __name__ == "__main__":
    config = load_config()
    connect(config)
    