import smtplib
import copy
import time
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr

class Email(object):
    sender = 'sjb_yhzsk@sina.com'
    mail_host = 'smtp.sina.com'
    mail_user = 'sjb_yhzsk@sina.com'
    mail_pass = 'sjb_yhzsk0'

    def __init__(self, receiver = None):
        if receiver == None:
            self.receivers = []
        else:
            self.receivers = copy.deepcopy(receiver)

    def sendBaseMail(self, content, receiver):
        msg = MIMEText(_text=content, _subtype='plain', _charset='utf-8')
        msg['From'] = self.addressFormat('Test <%s>' % self.sender)
        msg['To'] = self.addressFormat('Admin <%s>' % receiver)
        msg['Subject'] = Header('Server Alert', 'utf-8').encode()
        msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')

        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.mail_host, 25)
            smtpObj.set_debuglevel(1)
            smtpObj.login(self.mail_user, self.mail_pass)
            smtpObj.sendmail(self.sender, receiver, msg.as_string())
            smtpObj.quit()
        except:
            print 'send %s failed' % receiver

    def sendMails(self, content, receviers):
        for recv in receviers:
            self.sendBaseMail(content, recv)

    def addressFormat(self, add):
        name, address = parseaddr(add)
        return formataddr((Header(name, 'utf-8').encode(), address))

email = Email()

email.sendMails('hello world', ['aifjhb0815@gmail.com', 'jhb_0815@icloud.com'])