import logging
from logging.config import dictConfig


def configure_logger(name="default"):
    dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "default": {
                    "format": "%(asctime)s - %(levelname)s - %(message)s",
                    "datefmt": "%Y-%m-%d %H:%M:%S",
                }
            },
            "handlers": {
                "console": {
                    "level": "DEBUG",
                    "class": "logging.StreamHandler",
                    "formatter": "default",
                    "stream": "ext://sys.stdout",
                },
                "file": {
                    "level": "DEBUG",
                    "class": "logging.handlers.TimedRotatingFileHandler",
                    "formatter": "default",
                    "filename": "app.log",
                    "when": "M",
                    "backupCount": 10,
                },
            },
            "loggers": {
                "default": {
                    "level": "DEBUG",
                    "handlers": ["console", "file"],
                    "propagate": True,
                }
            },
        }
    )
    return logging.getLogger(name)


logger = configure_logger()
