import logging

# Configure basic logging to the console
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s- %(levelname)s - %(message)s",
)

# Log messages at different levels
logging.debug("This is a debug message.")
logging.info("This is an info message.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")
logging.critical("This is a critical message.")
