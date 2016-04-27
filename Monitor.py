import psutil
import SystemInfo
import logging

logger=logging.getLogger()
handler=logging.FileHandler("Log_test.txt")
logger.addHandler(handler)
logger.setLevel(logging.NOTSET)

systemInfo = SystemInfo.SystemInfo(pids=None, processName=None)

cpuAlertCount = int(systemInfo.cpu_wait_time)
cpuAlertCounter = 0

print systemInfo.sysInfo_cpu

while True :
    # check cpu usage rate
    systemInfo.getCpuInfo()
    if cpuAlertCount > cpuAlertCount :
        # call the alert moduel
        print 'alert'

    break
