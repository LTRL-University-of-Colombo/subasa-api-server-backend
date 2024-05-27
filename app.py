# from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy
# import uuid
# import hashlib
# import time
# from datetime import datetime
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///api_usage.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# db = SQLAlchemy(app)
#
#
# # Database models
# class User(db.Model):
#     id = db.Column(db.String(36), primary_key=True)
#     api_key = db.Column(db.String(64), unique=True, nullable=False)
#
#
# class ApiUsage(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
#     endpoint = db.Column(db.String(255), nullable=False)
#     timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#
#
# with app.app_context():
#     db.create_all()
#
# SECRET_KEY = 'your_secret_key'
#
#
# def generate_api_key():
#     return hashlib.sha256(uuid.uuid4().hex.encode()).hexdigest()
#
#
# def generate_access_token(api_key):
#     timestamp = str(time.time())
#     token = hashlib.sha256((api_key + timestamp + SECRET_KEY).encode()).hexdigest()
#     return token, timestamp
#
#
# @app.route('/register', methods=['POST'])
# def register():
#     user_id = str(uuid.uuid4())
#     api_key = generate_api_key()
#     new_user = User(id=user_id, api_key=api_key)
#     db.session.add(new_user)
#     db.session.commit()
#     return jsonify({'user_id': user_id, 'api_key': api_key})
#
#
# @app.route('/get_token', methods=['POST'])
# def get_token():
#     api_key = request.json.get('api_key')
#     user = User.query.filter_by(api_key=api_key).first()
#     if user:
#         token, timestamp = generate_access_token(api_key)
#         return jsonify({'access_token': f"{token}.{timestamp}"})
#     return jsonify({'error': 'Invalid API key'}), 401
#
#
# @app.route('/data', methods=['GET'])
# def get_data():
#     token = request.headers.get('Authorization')
#     if not token:
#         return jsonify({'error': 'Token required'}), 401
#
#     api_key = verify_token(token)
#     if not api_key:
#         return jsonify({'error': 'Invalid or expired token'}), 401
#
#     user = User.query.filter_by(api_key=api_key).first()
#     if user:
#         track_usage(user.id, '/data')
#         return jsonify({'data': 'Your protected data', 'user_id': user.id})
#     return jsonify({'error': 'Invalid API key'}), 401
#
#
# def verify_token(token):
#     try:
#         token_hash, timestamp = token.split('.')
#         for api_key in User.query.with_entities(User.api_key):
#             expected_token, _ = generate_access_token(api_key)
#             if expected_token == token_hash:
#                 return api_key
#     except ValueError:
#         pass
#     return None
#
#
# def track_usage(user_id, endpoint):
#     usage = ApiUsage(user_id=user_id, endpoint=endpoint)
#     db.session.add(usage)
#     db.session.commit()
#
#
# @app.route('/usage/<user_id>', methods=['GET'])
# def get_usage(user_id):
#     usage_records = ApiUsage.query.filter_by(user_id=user_id).all()
#     usage_data = [{'endpoint': u.endpoint, 'timestamp': u.timestamp} for u in usage_records]
#     return jsonify(usage_data)
#
#
# if __name__ == '__main__':
#     app.run(debug=True)


from controllers.endpoints import app

if __name__ == '__main__':
    app.run(debug=True)
