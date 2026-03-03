import logging.config


LOGGING_CONFIG = {
    "version": 1,
    "formatters": {
        "default": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "default",
        },
        "file": {
            "class": "logging.FileHandler",
            "level": "ERROR",
            "formatter": "default",
            "filename": "app.log",
        },
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["console", "file"]
    }
}

def setup_logger() -> None:
    logging.config.dictConfig(LOGGING_CONFIG)