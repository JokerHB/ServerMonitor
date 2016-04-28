import smtplib
import copy
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr

class Email(object):
    sender = ''
    mail_host = ''
    mail_user = ''
    mail_pass = ''

    def __init__(self, receiver = None):
        if receiver == None:
            self.receivers = []
        else:
            self.receivers = copy.deepcopy(receiver)

    def sendBaseMail(self, content, receiver):
        msg = MIMEText(_text=content, _subtype='plain', _charset='utf-8')
        msg['From'] = self.addressFormat('Server <%s>' % self.sender)
        msg['To'] = self.addressFormat('Admin <%s>' % receiver)
        msg['Subject'] = Header('Server Alert', 'utf-8').encode()

        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.mail_host, 25)
            # smtpObj.set_debuglevel(1)
            smtpObj.login(self.mail_user, self.mail_pass)
            smtpObj.sendmail(self.sender, receiver, msg.as_string())
            smtpObj.quit()
        except:
            print 'send %s failed' % receiver

    def sendMails(self, content, receviers):
        for recv in receviers:
            self.sendBaseMail(content, recv)

    def addressFormat(addr):
        name, addr = parseaddr(addr)
        return formataddr((Header(name, 'utf-8').encode(), addr))


