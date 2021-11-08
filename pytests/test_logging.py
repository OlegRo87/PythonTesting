import logging


def test_log():
    logger = logging.getLogger(__name__)

    file_handler = logging.FileHandler("logfile.log")

    logger.addHandler(file_handler)  # filehandler object
    formatter = logging.Formatter("%(asctime)s:%(levelname)s :%(name)s :%(message)s")
    file_handler.setFormatter(formatter)

    logger.setLevel(logging.INFO)
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("Something is in warning mode")
    logger.error("SA major error has happened")
    logger.critical("Critical issue")
