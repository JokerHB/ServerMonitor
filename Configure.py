import xml.dom.minidom
from collections import namedtuple

class Configure(object):
    def __init__(self, configureFilePath):
        try:
            self.xml = xml.dom.minidom.parse(configureFilePath)
        except IOError:
            print 'can not open ' + configureFilePath + ' , please check the file'
            exit(-1)
        else:
            print 'open the file success, reading the file now'

    def getEmail(self):
        EmailConfig = namedtuple('EmailConfig', ['host', 'user', 'password'])
        host = self.getElement(tagName='host', attr='host')
        user = self.getElement(tagName='user', attr='user')
        password = self.getElement(tagName='password', attr='pass')

        return EmailConfig._make([host, user, password])

    def getCpu(self):
        CpuConfig = namedtuple('CpuConfig', ['up', 'down', 'wait_time'])
        up = self.getElement(tagName='cpu_upper_limit')
        down = self.getElement(tagName='cpu_lower_limit')
        wait_time = self.getElement(tagName='cpu_wait_time')

        return CpuConfig._make([up, down, wait_time])

    def getMem(self):
        MemConfig = namedtuple('MemConfig', ['up', 'down', 'wait_time'])
        up = self.getElement(tagName='mem_upper_limit')
        down = self.getElement(tagName='mem_lower_limit')
        wait_time = self.getElement(tagName='mem_wait_time')

        return MemConfig._make([up, down, wait_time])

    def getDisk(self):
        DiskConfig = namedtuple('DiskConfig', ['limit'])
        limit = self.getElement(tagName='disk_alert_limit')

        return DiskConfig._make([limit])

    def getNet(self):
        NetConfig = namedtuple('NetConfig', ['up_up', 'up_down', 'down_up', 'down_down', 'wait_time'])
        up_up = self.getElement(tagName='net_upload_upper_limit')
        up_down = self.getElement(tagName='net_upload_lower_limit')
        down_up = self.getElement(tagName='net_down_upper_limit')
        down_down = self.getElement(tagName='net_down_lower_limit')
        wait_time = self.getElement(tagName='net_wait_time')

        return NetConfig._make([up_up, up_down, down_up, down_down, wait_time])

    def getProc(self):
        procName = []
        tags = self.getTags('proc')

        for proc in tags:
            procName.append(proc.getAttribute('name'))

        return procName

    def getTags(self, tagName):
        root = self.xml.documentElement
        tags = root.getElementsByTagName(tagName)

        return tags

    def getElement(self, tagName, attr='value'):
        tags = self.getTags(tagName)[0]

        return tags.getAttribute(attr)

