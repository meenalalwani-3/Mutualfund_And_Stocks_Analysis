import os
import logging.config
import yaml

def setup_logger():
    config_path = os.path.join(os.path.dirname(__file__), '../configs/logging_config.yaml')
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
        logging.config.dictConfig(config)
    return logging.getLogger('my_app')

logger = setup_logger()
