import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import datetime

email_user = 'adityakumar@thb.co.in'
email_send = 'aditya.varshneya@gmail.com'
email_copy = 'adityakumar@thb.co.in'
password = 'aditya061287'

message = MIMEMultipart()
message['From'] = email_user
message['To'] = email_send
message['Cc'] = email_copy
message['Subject'] = "Automation Testing Report "
body = "Hi All Please find attached Automation report"
message.attach(MIMEText(body, 'plain'))
#attachment
filename = "Automation_report.html"
attachment = open("C:\webdrivers\Automation_report.html", "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment;filename= %s' % filename)
message.attach(part)

server = smtplib.SMTP('smtp.gmail.com', port=587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(email_user, password)
text = message.as_string()
server.sendmail(email_user, email_send, text)
server.quit()
