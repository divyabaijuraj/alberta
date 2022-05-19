import logging


# class LogGen:
#     @staticmethod
#     def loggen():
#         logging.basicConfig(filename=".\\Logs\\automation.log", format='%(asctime)s: %(levelname)s: %(message)s',
#                             force=True, datefmt='%m%d%Y %I:%M:%S %p')
#
#         logger = logging.getLogger()
#         logger.setLevel(logging.INFO)
#
#         return logger

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="C:\\Users\\Dell\\PycharmProjects\\pythonProject\\alberta\Logs\\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            force=True, datefmt='%m%d%Y %I:%M:%S %p')

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        return logger
