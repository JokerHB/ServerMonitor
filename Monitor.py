import psutil
import SystemInfo
import logging
import Alert
import time

# log file
logger=logging.getLogger()
handler=logging.FileHandler("SystemInfo.log")
logger.addHandler(handler)
logger.setLevel(logging.NOTSET)


# system info get
systemInfo = SystemInfo.SystemInfo(pids=None, processName=None)
# alert center
alertcenter = Alert.Alert()

# process names
processNames = ['python', 'zsh', 'java']

# alert limit define
# region

# alert limit configure
cpuAlertCount = int(systemInfo.cpu_wait_time)
cpuAlertCounter = 0

memAlertCount = int(systemInfo.mem_wait_time)
memAlertCounter = 0

netAlertCount = int(systemInfo.net_wait_time)
netAlertCounter = 0

# endregion

def cpuInfoCheck(cpuInfo) :
    count = 0
    for rate in cpuInfo :
        if rate > systemInfo.cpu_upper_limit or rate < systemInfo.cpu_lower_limit :
            count += 1
    if count == len(cpuInfo) :
        return True
    return False

def memInfoCheck(memInfo) :
    if memInfo.percent > systemInfo.mem_upper_limit or memInfo.percent < systemInfo.mem_lower_limit :
        return True
    return False

def diskInfoCheck(diskInfo) :
    if diskInfo.percent > systemInfo.disk_alert_limit :
        return True
    return False

def netInfoCheck(netInfo, interface) :
    try :
        speed = netInfo[interface]
    except :
        return True
    if (speed[0] > systemInfo.net_upload_upper_limit or speed[0] < systemInfo.net_upload_lower_limit) and (speed[1] < systemInfo.net_down_lower_limit or speed[1] > systemInfo.net_down_upper_limit) :
        return True
    return False

def deBugOutPut():
    pids = psutil.pids()
    systemInfo.getMemInfo(pids)
    print systemInfo.processInfo_mem

while True :
    alertcenter.alertInfos = ''
    # check cpu usage rate
    systemInfo.getCpuInfo()
    if cpuAlertCounter > cpuAlertCount :
        # call the alert moduel
        print 'cpu alert'
        alertcenter.cpuAlert(systemInfo.sysInfo_cpu)
        cpuAlertCounter = 0
    if cpuInfoCheck(systemInfo.sysInfo_cpu[1]) :
        cpuAlertCounter += 1
    else :
        cpuAlertCounter = 0

    # check mem usage rate
    systemInfo.getMemInfo()
    if memAlertCounter > memAlertCount :
        # calthe alert moduel
        # report the top 10 process
        print 'mem alert'
        alertcenter.memAlert(systemInfo.sysInfo_mem)
        memAlertCounter = 0
    if memInfoCheck(systemInfo.sysInfo_mem[0]) :
        memAlertCounter += 1
    else :
        memAlertCounter = 0

    # check disk usage rate
    systemInfo.getDiskInfo()
    if diskInfoCheck(systemInfo.sysInfo_disk[0]) :
        # call alert moduel
        # report the detail usage
        print 'disk alert'
        alertcenter.diskAlert(systemInfo.sysInfo_disk)

    # check net usage rate
    systemInfo.getNetInfo()
    if netAlertCounter > netAlertCount :
        # call alert moduel
        # report the up/download speed
        print 'net alert'
        alertcenter.netAlert(interface='lo', netInfo=systemInfo.sysInfo_net)
    if netInfoCheck(systemInfo.sysInfo_net, 'lo') :
        netAlertCounter += 1
    else :
        netAlertCounter = 0

    # check process info
    notExist = systemInfo.getPidByProcessName(processName=processNames)
    if notExist != None and len(notExist) > 0:
        alertcenter.procAlert(notExist)

    alertcenter.alert()

    time.sleep(60.0)

    # deBugOutPut()
