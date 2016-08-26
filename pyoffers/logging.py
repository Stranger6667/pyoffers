# coding: utf-8
import logging
import sys


DEFAULT_LOGGING_LEVEL = logging.CRITICAL


def get_logger(verbosity):
    """
    Returns simple console logger.
    """
    logger = logging.getLogger(__name__)
    logger.setLevel({
        0: DEFAULT_LOGGING_LEVEL,
        1: logging.INFO,
        2: logging.DEBUG
    }.get(min(2, verbosity), DEFAULT_LOGGING_LEVEL))
    logger.handlers = []
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(handler)
    return logger
