"""
This script is used to load the config file.

"""
# library imports
import json
import os
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

from src.scripts.get_logger import logger


# Define function to load config file
def load_config(
    file_path=os.path.join(Path(__file__).parent.parent.parent, "config.json")
):
    try:
        logger.info("Loading config file...")
        with open(file_path) as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Failed to load config file: {e}")
        raise e
