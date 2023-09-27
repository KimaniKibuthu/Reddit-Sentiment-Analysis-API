"""
This script is used to get the logger object for logging the information
"""

# library imports
import os
import logging
import sys
from pathlib import Path


# Define logging format and where to store the logs
logging_str = "[%(asctime)s]: %(levelname)s: %(module)s: %(message)s]"
log_dir = os.path.join(Path(__file__).parent.parent, "logs")
log_filepath = os.path.join(log_dir, "logs.log")
os.makedirs(log_dir, exist_ok=True)

# Configure the logger
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[logging.FileHandler(log_filepath), logging.StreamHandler(sys.stdout)],
)

logger = logging.getLogger(__name__)
