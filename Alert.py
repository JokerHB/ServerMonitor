import psutil

class Alert(object):
    def __init__(self):
        print 'alert'

    # cpu alert, send top 10 process' cpu percent
    def cpuAlert(self, cpuInfo):
        alertInfo = 'CPU Number is ' + str(cpuInfo[0]) + '\n'
        alertInfo += 'Current rate in each CPU: ' + '\n'

        for i in range(int(cpuInfo[0])) :
            alertInfo += '      #' + str(i + 1) + '     ' + str(cpuInfo[0][i]) + '\n'

        procs = psutil.process_iter()
        pinfos = {}
        for p in procs:
            try:
                pinfo = p.as_dict(attrs=['name', 'cpu_percent'])
            except psutil.NoSuchProcess:
                print 'error'
            else:
                pinfos[pinfo['name']] = pinfo['cpu_percent']

        pinfos = sorted(pinfos.iteritems(), key=lambda d: d[1], reverse=True)
        pinfos = pinfos[0:10]

        for p in pinfos :
            alertInfo += str(p) + '\n'

        return alertInfo

    # mem alert, send top 10 process' mem percent

    # disk alert, send percentage of free, size of disk, free size, used size

    # net alert, send current net rate

    # process alert, send the process which is not running
