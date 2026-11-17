import logging
from Logging.logger import setup_logging

logger = logging.getLogger(__name__)
import Tools.command as commander


setup_logging()
commander.test()

logger.info("Hello from server.py")