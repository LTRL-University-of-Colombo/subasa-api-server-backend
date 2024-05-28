from flask import Flask
import logging
from blueprints.user_blueprint import bp as user_blueprints

# initialize app
app = Flask(__name__)

# logger config
app.logger.setLevel(logging.INFO)
handler = logging.FileHandler('app.log')
app.logger.addHandler(handler)


# add blueprints
app.register_blueprint(user_blueprints)



if __name__ == '__main__':
    app.run(debug=True)
