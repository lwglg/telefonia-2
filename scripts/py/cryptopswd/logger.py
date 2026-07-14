import sys
import logging

__all__ = ["create_logger_instance"]


def create_logger_instance(label: str = "cryptpswd_logger", logfile_name: str = "cryptpswd.log") -> logging.Logger:
    logger = logging.getLogger(label)
    logger.setLevel(logging.DEBUG)  # Set the lowest level to capture all events

    # Avoid duplicate logs if this configuration is run multiple times
    if not logger.handlers:
        console_handler = logging.StreamHandler(sys.stderr)
        console_handler.setLevel(logging.INFO)

        file_handler = logging.FileHandler(logfile_name, mode="a", encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)

        log_format = logging.Formatter(
            fmt="%(asctime)s [%(levelname)s] (%(filename)s:%(lineno)d) - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        console_handler.setFormatter(log_format)
        file_handler.setFormatter(log_format)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger
