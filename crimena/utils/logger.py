import logging
import logging.config

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)-8s] %(message)s',
            'datefmt': '%H:%M:%S',
        },
        'debug': {
            'format': '[%(filename)s#%(lineno)s] %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level':'INFO',
            'class':'logging.StreamHandler',
            'formatter': 'standard'
        },
        'debug': {
            'level': 'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'debug'
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'debug': {
            'handlers': ['debug'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}


def setup_logger():
    logging.config.dictConfig(LOGGING)
    logger = logging.getLogger('mylogger')

    logger.debug('A debug message')