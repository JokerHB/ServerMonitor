import psutil
import copy
import time
import bisect
import re

class SystemInfo(object) :
    # net alert limit
    net_upload_upper_limit = 1000.0
    net_upload_lower_limit = 0.0
    net_down_upper_limit = 1000.0
    net_down_lower_limit = 0.0
    net_wait_time = 2.0

    # mem alert limit
    mem_upper_limit = 80.0
    mem_lower_limit = 0.0
    mem_wait_time = 10.0

    # disk alert limit
    disk_alert_limit = 85.0

    # cpu alert limit
    cpu_upper_limit = 80.0
    cpu_lower_limit = 0.0
    cpu_wait_time = 10.0

    def __init__(self, processName = None, pids = None) :
        # get global information
        self.sysInfo = {}
        self.pids = []
        self.processName = []

        self.globalInfo()

        if processName == None :
            self.pids = []
        else :
            self.processName = copy.deepcopy(processName)
            notExist = self.getPidByProcessName(processName=processName)
            if notExist == None or len(notExist) == 0 :
                print 'system process is all running'
            else :
                print 'WARNING : those process not running ', str(notExist)

        if (self.pids == None or len(self.pids) == 0) and pids == None:
            self.pids = []
        else :
            self.pids = copy.deepcopy(pids)

    def globalInfo(self) :
        self.getCpuInfo()
        self.sysInfo['cpu'] = self.sysInfo_cpu
        self.getMemInfo()
        self.sysInfo['mem'] = self.sysInfo_mem
        self.getDiskInfo()
        self.sysInfo['disk'] = self.sysInfo_disk
        self.getNetInfo()
        self.sysInfo['disk'] = self.sysInfo_net

    def getCpuInfo(self, pids = None) :
        if pids == None :
            # cpu_count, cpu_usage_rate
            self.sysInfo_cpu = []
            self.sysInfo_cpu.append(psutil.cpu_count())
            self.sysInfo_cpu.append(psutil.cpu_percent(interval=.1, percpu=True))
        else :
            self.processInfo_cpu = []
            for pid in pids :
                tmp = psutil.Process(pid)
                self.processInfo_cpu.append(tmp.cpu_percent(interval=.1))

    def getMemInfo(self, pids = None) :
        if pids == None:
            # mem_virtual, mem_swap
            self.sysInfo_mem = []
            self.sysInfo_mem.append(psutil.virtual_memory())
            self.sysInfo_mem.append(psutil.swap_memory())
        else :
            self.processInfo_mem = []

            for pid in pids :
                tmp = psutil.Process(pid)
                self.processInfo_mem.append(tmp.memory_percent())

    def getDiskInfo(self) :
        self.sysInfo_disk = []
        self.sysInfo_disk.append(psutil.disk_usage('/'))

    def getNetInfo(self) :
        self.sysInfo_net = {}
        counters = psutil.net_io_counters(pernic=True)

        for counter in (counters):
            tot = (counters[counter].bytes_sent, counters[counter].bytes_recv)
            t0 = time.time()
            time.sleep(.1)
            tmp_count = psutil.net_io_counters(pernic=True)[counter]
            t1 = time.time()
            last_tot = (tmp_count.bytes_sent, tmp_count.bytes_recv)
            ul, dl = [(last - now) / (t1 - t0) / 1024.0
                          for now, last in zip(tot, last_tot)]
            self.sysInfo_net[counter] = [ul, dl]

    def getPidByProcessName(self, processName):
        if processName == None :
            self.pids = []
        else :
            notExist = []
            procs = psutil.process_iter()
            for pName in processName :
                isFind = False
                for proc in procs :
                    if proc.name() == pName :
                        self.pids.append(proc.pid)
                        isFind = True
                        break
                if isFind == False :
                    notExist.append(pName)

            return notExist