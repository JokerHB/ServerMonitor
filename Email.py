import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'sjb_yhzsk@sina.com'
receiver = ['aifjhb0815@gmail.com', 'jhb_0815@163.com']

mail_host = 'smtp.sina.com'
mail_user = 'sjb_yhzsk@sina.com'
mail_pass = 'sjb_yhzsk0'

message = MIMEText(_text='This is a test sent by python', _subtype='plain', _charset='utf-8')

message['From'] = Header('Test Sina Email', 'utf-8')
message['To'] = Header('Test Receiver', 'utf-8')
subject = 'Test'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receiver, message.as_string())
    smtpObj.quit()

    print 'send success'
except smtplib.SMTPException:
    print 'send failed'