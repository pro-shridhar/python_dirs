import logging


"""Notice that the debug() and info() messages didn’t
get logged. This is because, by default, the logging
module logs the messages with a severity level of WARNING
or above. You can change that by configuring the logging
module to log events of all levels."""
# Configure logging to a file
logging.basicConfig(
    # filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logging.debug("This will get logged.")
logging.info("Application started.")
try:
    result = 10 / 0
except ZeroDivisionError as e:
    # exc_info logs traceback
    logging.error(f"An error occurred: {e}", exc_info=True)
    # Exception information can be captured if the exc_info
    # parameter is passed as True,
logging.info("Application finished.")
