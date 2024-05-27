import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = RotatingFileHandler('logs/app.log', maxBytes=20*1024*1024, backupCount=5)  # Max size: 1 MB, 5 backup files
formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

