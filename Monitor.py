import psutil
import SystemInfo
import logging

logger=logging.getLogger()
handler=logging.FileHandler("Log_test.txt")
logger.addHandler(handler)
logger.setLevel(logging.ERROR)

systemInfo = SystemInfo.SystemInfo(pids=None, processName=None)

cpuAlertCount = int(systemInfo.cpu_wait_time)
cpuAlertCounter = 0

while True :
    # check cpu usage rate
    systemInfo.getCpuInfo()
    # if cpuAlertCount > cpuAlertCount :
        # call the alert moduel
        # list top 10 process
    # print systemInfo.sysInfo_cpu
    while True:
        top = {}
        _pids = psutil.pids()
        for pid in _pids:
            try :
                p = psutil.Process(pid)
            except :
                # print 'error'
                _pids = psutil.pids()
                logger.error("This is an error message " + str(pid))
            else :
                top[p.name()] = p.cpu_percent()
            # print p.cpu_percent(),
        top = sorted(top.iteritems(), key=lambda d:d[1], reverse=True)
        logger.info(str(top))
        # top = top[0:10]
        # print 'cpu is busy'
        # print top
        break


# logger=logging.getLogger()
# handler=logging.FileHandler("Log_test.txt")
# logger.addHandler(handler)
# logger.setLevel(logging.ERROR)
# logger.error("This is an error message")
# logger.info("This is an info message")
# logger.critical("This is a critical message")

