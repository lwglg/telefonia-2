import sys
import re
from logging import Logger

__all__ = ["get_safe_int", "get_safe_str"]


def get_safe_int(
    logger: Logger,
    prompt: str = "Enter an integer: ", 
    min_value: int | None = None, 
    max_value: int | None = None,
) -> int:
    """Safely prompts the user for an integer within an optional range.
    
    Guarantees returning an int, or exits cleanly on user interrupt.
    """
    while True:
        try:
            # Step 1: Get raw string input
            raw_input = input(prompt).strip()
            
            # Step 2: Attempt to cast to int
            value = int(raw_input)
            
            # Step 3: Range validation (Optional)
            if min_value is not None and value < min_value:
                logger.error(f"Error: Value must be at least {min_value}.")
                continue
            if max_value is not None and value > max_value:
                logger.error(f"Error: Value must be at most {max_value}.")
                continue
                
            return value
            
        except ValueError:
            logger.error("Error: Invalid input. Please enter a whole number.")
        except (KeyboardInterrupt, EOFError):
            # Gracefully handle Ctrl+C or Ctrl+D instead of dumping a stack trace
            logger.info("\nOperation cancelled by user.")
    
            sys.exit(0)


def get_safe_str(
    logger: Logger,
    prompt: str = "Enter text: ",
    allow_empty: bool = False,
    min_length: int | None = None,
    max_length: int | None = None,
    pattern: str | None = None,
    pattern_error_msg: str = "Input does not match the required format."
) -> str:
    """Safely prompts the user for a string with robust validations.
    
    Guarantees returning a valid string, or exits cleanly on user interrupt.
    """
    while True:
        try:
            # Step 1: Get raw input and strip leading/trailing whitespace
            value = input(prompt).strip()
            
            # Step 2: Validate empty strings
            if not value and not allow_empty:
                logger.error("Error: Input cannot be empty. Please enter some text.")
                continue
                
            # If empty is allowed and they entered nothing, return it early
            if not value and allow_empty:
                return value

            # Step 3: Validate length constraints
            if min_length is not None and len(value) < min_length:
                logger.error(f"Error: Input must be at least {min_length} characters long.")
                continue
            if max_length is not None and len(value) > max_length:
                logger.error(f"Error: Input cannot exceed {max_length} characters.")
                continue

            # Step 4: Validate Regex pattern (if provided)
            if pattern is not None:
                if not re.match(pattern, value):
                    logger.error(f"Error: {pattern_error_msg}")
                    continue

            return value

        except (KeyboardInterrupt, EOFError):
            # Gracefully handle Ctrl+C or Ctrl+D
            logger.info("\nOperation cancelled by user.")
            sys.exit(0)
    