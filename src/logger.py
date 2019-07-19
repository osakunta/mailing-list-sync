import sys
import logging
from pythonjsonlogger import jsonlogger


class StackdriverJsonFormatter(jsonlogger.JsonFormatter, object):
    def __init__(self, fmt="%(levelname) %(message)", *args, **kwargs):
        jsonlogger.JsonFormatter.__init__(self, fmt=fmt, *args, **kwargs)

    def process_log_record(self, log_record):
        log_record['severity'] = log_record['levelname']
        del log_record['levelname']

        return super(StackdriverJsonFormatter, self).process_log_record(log_record)


def setup_logging():
    logging.getLogger('googleapiclient.discovery').setLevel(logging.ERROR)
    logging.basicConfig(level=logging.INFO)

    logger = logging.getLogger()
    handler = logging.StreamHandler(sys.stdout)
    formatter = StackdriverJsonFormatter()

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


log = setup_logging()
