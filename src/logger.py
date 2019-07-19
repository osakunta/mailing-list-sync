import sys
import logging
from pythonjsonlogger import jsonlogger
from src.config import ENV


class StackdriverJsonFormatter(jsonlogger.JsonFormatter, object):
    def __init__(self, fmt="%(levelname) %(message)", *args, **kwargs):
        jsonlogger.JsonFormatter.__init__(self, fmt=fmt, *args, **kwargs)

    def process_log_record(self, log_record):
        log_record['severity'] = log_record['levelname']
        del log_record['levelname']

        return super(StackdriverJsonFormatter, self).process_log_record(log_record)


def setup_logging():
    logging.getLogger('googleapiclient.discovery').setLevel(logging.ERROR)

    logger = logging.getLogger()

    if ENV == 'production':
        handler = logging.StreamHandler(sys.stdout)
        formatter = StackdriverJsonFormatter()

        handler.setFormatter(formatter)
        logger.addHandler(handler)
    else:
        logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

    return logger


log = setup_logging()
