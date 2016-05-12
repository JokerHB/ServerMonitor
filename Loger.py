import logging

class Loger(object):
    def __init__(self, logFilePath = './Monitor_log.log'):
        self.logger = logging.getLogger()
        self.logfileName = logFilePath
        self.logformattor = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        self.logHandle = logging.FileHandler(self.logfileName)
        self.logHandle.setFormatter(self.logformattor)
        self.logger.addHandler(self.logHandle)
        self.logger.setLevel(logging.NOTSET)

    def log_Info(self, log_info):
        self.logger.info(log_info)

    def log_Error(self, log_error):
        self.logger.error(log_error)

    def log_Debug(self, log_debug):
        self.logger.debug(log_debug)

    def splitByWeek(self):
        self.logSplitHandle = logging.handlers.TimedRotatingFileHandler(self.logfileName, when='W', interval=0, backupCount=40)

