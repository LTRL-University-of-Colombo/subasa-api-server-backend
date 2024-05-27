from flask import Flask, request

from db import query_data
from logging_config import *

app = Flask(__name__)


# Endpoint to fetch users from database
@app.route('/users')
def get_users():
    try:
        data = query_data("SELECT * FROM user where name = 'anjuna'")
        return data
    except Exception as e:
        logging.info("fetched all data from '%s' ---%s", request.remote_addr, e)


if __name__ == '__main__':
    app.run(debug=True)
