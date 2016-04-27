import psutil
import SystemInfo
import logging

# log file
logger=logging.getLogger()
handler=logging.FileHandler("SystemInfo.log")
logger.addHandler(handler)
logger.setLevel(logging.NOTSET)

# system info get
systemInfo = SystemInfo.SystemInfo(pids=None, processName=None)

# alert limit configure
cpuAlertCount = int(systemInfo.cpu_wait_time)
cpuAlertCounter = 0

memAlertCount = int(systemInfo.mem_wait_time)
memAlertCounter = 0

def cpuInfoCheck(cpuInfo) :
    count = 0
    for rate in cpuInfo :
        if rate > systemInfo.cpu_upper_limit or rate < systemInfo.cpu_lower_limit :\
            count += 1
    if count == len(cpuInfo) :
        return True
    return False

def memInfoCheck(memInfo) :
    if memInfo.percent > systemInfo.mem_upper_limit or memInfo.percent < systemInfo.mem_upper_limit:
        return True
    return False

def deBugOutPut():
    pids = psutil.pids()
    systemInfo.getMemInfo(pids)
    print systemInfo.processInfo_mem

while True :
    # check cpu usage rate
    systemInfo.getCpuInfo()
    if cpuAlertCounter > cpuAlertCount :
        # call the alert moduel
        print 'cpu alert'
        cpuAlertCounter = 0

    if cpuInfoCheck(systemInfo.sysInfo_cpu[1]) :
        cpuAlertCounter += 1
    else :
        cpuAlertCounter = 0

    # check mem usage rate
    systemInfo.getMemInfo()
    if memAlertCounter > memAlertCount :
        # calthe alert moduel
        print 'mem alert'
        memAlertCounter = 0

    if memInfoCheck(systemInfo.sysInfo_mem[0]) :
        memAlertCounter += 1
    else :
        memAlertCounter = 0

    deBugOutPut()

    break
