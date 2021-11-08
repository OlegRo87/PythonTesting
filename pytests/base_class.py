import inspect
import logging


class BaseClass:

    def get_logger(self):
        # logger = logging.getLogger(__name__) to use if using directly without inheritance
        # 2021 - 11 - 02
        # 11: 21:30, 558: INFO:pytests.base_class: Oleg
        # 2021 - 11 - 02
        # 11: 21:30, 558: INFO:pytests.base_class: oleg.rohlin @ gmail.com

        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        # 2021 - 11 - 02
        # 11: 25:17, 665: INFO:test_edit_profile: Oleg
        # 2021 - 11 - 02
        # 11: 25:17, 665: INFO:test_edit_profile: oleg.rohlin @ gmail.com
        file_handler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s:%(levelname)s :%(name)s :%(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger
