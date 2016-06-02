import logging

class Loger(object):
    def __init__(self, logFilePath = './Monitor_log.log'):
        # get the logger
        self.logger = logging.getLogger()
        self.logfileName = logFilePath
        self.logformattor = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

        # add formattor to the logger
        self.logHandle = logging.FileHandler(self.logfileName)
        self.logHandle.setFormatter(self.logformattor)
        self.logger.addHandler(self.logHandle)
        self.logger.setLevel(logging.NOTSET)

    # log the info
    def log_Info(self, log_info):
        self.logger.info(log_info)

    # log the error
    def log_Error(self, log_error):
        self.logger.error(log_error)

    # log the debug
    def log_Debug(self, log_debug):
        self.logger.debug(log_debug)

    # split the log in every week
    def splitByWeek(self):
        self.logSplitHandle = logging.handlers.TimedRotatingFileHandler(self.logfileName, when='W', interval=0, backupCount=40)

