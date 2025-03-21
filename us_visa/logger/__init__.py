import logging
import os
from datetime import datetime
from from_root import from_root

LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
log_dir = os.path.join(from_root(), "logs")
log_path = os.path.join(log_dir, LOG_FILE)
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    filename=log_path,
    format="[ %(asctime)s] %(module)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)
