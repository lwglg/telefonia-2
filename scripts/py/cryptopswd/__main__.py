import sys

from .main import generate_hash_salt_for_password
from .logger import create_logger_instance
from .inputs import get_safe_int, get_safe_str


if __name__ == "__main__":
    logger = create_logger_instance()

    try:
        password = get_safe_str(logger, prompt="Enter desired password: ", min_length=6, max_length=8)
        iterations = get_safe_int(logger, prompt="Enter number of iterations: ", min_value=1000, max_value=27500)
        hash, salt = generate_hash_salt_for_password(password, iterations)

        logger.info(f"salt: {salt}")
        logger.info(f"hash: {hash}")
        logger.warning("My work here is done!")
    except (KeyboardInterrupt, EOFError) as intexc:
        logger.info(f"{intexc.__class__.__name__}: Operation cancelled by user.")
        sys.exit(0)
    except Exception as exc:
        logger.error(f"Some error occurred: {exc.__class__.__name__}: {str(exc)}")
        sys.exit(-1)
