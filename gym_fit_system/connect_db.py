from mysql.connector import pooling

_pool = None

def get_pool():
    global _pool
    if _pool is None:
        _pool = pooling.MySQLConnectionPool(
            pool_name="gym_pool",
            pool_size=5,
            host="localhost",
            user="root",
            password="admin",
            database="gym_fit_db"
        )
    return _pool

def get_connection():
    return get_pool().get_connection()
