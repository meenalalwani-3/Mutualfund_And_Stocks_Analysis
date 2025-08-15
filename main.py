import os
import time
from utilities.logger import logger
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Ensure logs directory exists
log_dir = os.getenv("LOG_DIR", "logs")
os.makedirs(log_dir, exist_ok=True)

# Cleanup old logs
def cleanup_old_logs(directory, days=7):
    now = time.time()
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_age = now - os.path.getmtime(file_path)
            if file_age > days * 86400:
                os.remove(file_path)
                logger.info(f"Deleted old log file: {file_path}")

retention_days = int(os.getenv("LOG_RETENTION_DAYS", "7"))
cleanup_old_logs(log_dir, retention_days)

# Sample data science task
def data_science_task():
    logger.info("Starting data science task...")
    try:
        logger.debug("Loading data...")
        data = [i for i in range(10)]
        logger.debug(f"Data loaded: {data[:5]}...")

        logger.debug("Processing data...")
        processed_data = [x**2 for x in data]
        logger.debug(f"Processed data sample: {processed_data[:5]}...")

        logger.info("Training model...")
        model_accuracy = 0.95
        logger.info(f"Model trained with accuracy: {model_accuracy}")

    except Exception as e:
        logger.error("An error occurred during the data science task", exc_info=True)

    logger.info("Data science task completed.")

if __name__ == "__main__":
    data_science_task()
