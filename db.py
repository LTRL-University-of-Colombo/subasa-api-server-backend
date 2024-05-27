import mysql.connector
from dbutils.pooled_db import PooledDB
from flask import jsonify
import logging


class ConnectionPool:
    __pool = None

    @classmethod
    def get_connection(cls):
        if cls.__pool is None:
            cls.__pool = PooledDB(
                creator=mysql.connector,
                mincached=1,
                maxcached=10,
                host='localhost',
                user='subasaAdmin',
                password='ucsc@123',
                database='subasaApi',
                autocommit=True
            )
        return cls.__pool.connection()


# generalized function to query data and convert them to json objects
def query_data(query):
    try:
        conn = ConnectionPool.get_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]
        cursor.close()
        conn.close()

        data = [serialize_row(row, column_names) for row in rows]
        return jsonify(data)

    except mysql.connector.Error as e:
        error_message = 'Internal server error'.format(str(e))
        logging.error("Database error %s", query)
        return jsonify({'error': error_message}), 500


def serialize_row(row, column_names):
    return {column_names[i]: row[i] for i in range(len(row))}
