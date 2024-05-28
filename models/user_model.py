from config.db_config import query_data

# select all users 
def select_all_users():
    try:
        data = query_data("SELECT * FROM users")
        return data
    except Exception as e:
        return e
