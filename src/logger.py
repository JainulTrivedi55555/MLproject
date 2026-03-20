import logging
import os
from datetime import datetime

# 1. Create the log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 2. Define the path for the 'logs' directory
logs_dir = os.path.join(os.getcwd(), "logs")

# 3. Create the 'logs' directory if it doesn't exist
os.makedirs(logs_dir, exist_ok=True)

# 4. Create the full path for the log file
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# 5. Configure the logger
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

