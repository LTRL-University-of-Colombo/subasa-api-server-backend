from flask import Blueprint,request, jsonify
from config.db_config import query_data
from config.loggin_config import logger
from models.user_model import select_all_users

bp = Blueprint('admin_route', __name__, url_prefix="/admin")


# Endpoint to fetch users from database
@bp.route('/users')
def get_users():
    try:
        data = select_all_users()
        logger.info('All users selected')
        return data
    except:
        return jsonify({'error': 'internal server error'}), 500

