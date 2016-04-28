import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

sender = 'sjb_yhzsk@sina.com'
receiver = ['aifjhb0815@gmail.com', 'jhb_0815@163.com']

mail_host = 'smtp.sina.com'
mail_user = 'sjb_yhzsk@sina.com'
mail_pass = 'sjb_yhzsk0'

message = MIMEText(_text='This is a test sent by python', _subtype='plain', _charset='utf-8')
message['From'] = _format_addr('Test <%s>' % sender)
message['To'] = _format_addr('Test')
message['Subject'] = Header('Test', 'utf-8').encode()

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    # smtpObj.set_debuglevel(1)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receiver, message.as_string())
    smtpObj.quit()

    print 'send success'
except smtplib.SMTPException:
    print 'send failed'