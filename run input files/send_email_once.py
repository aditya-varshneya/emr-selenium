import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import datetime
import os
import pdfkit
import time
from PyPDF2 import PdfFileMerger


if os.path.exists("Automation_report_input.pdf"):
  os.remove("Automation_report_input.pdf")
else:
  print("The file does not exist")

time.sleep(2)
config = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")
pdfkit.from_file("Automation_report_input.html", "Automation_report_input.pdf", configuration=config)


time.sleep(3)

email_user = 'adityakumar@thb.co.in'
email_send = "satyendra@thb.co.in,nitin@thb.co.in,rajesh@thb.co.in," \
             "vaibhav@thb.co.in,rakesh@thb.co.in,amitkumar@thb.co.in,vikassingh@thb.co.in"
email_copy = 'adityakumar@thb.co.in'
password = 'aditya061287'

message = MIMEMultipart()
message['From'] = email_user
message['To'] = email_send
message['Cc'] = email_copy
message['Subject'] = "Automation Testing Report - Web Application ( Video)"
body = "Hi All Please find attached Automation report"
message.attach(MIMEText(body, 'plain'))
#attachment
filename = "Automation_report_input.pdf"
files = [filename]
dir_path = "C:/Users/Lenovo/Documents/GitHub/emr-selenium-automation/run_input_files"
for f in files:
    file_path = os.path.join (dir_path,f)
    attachment = open(file_path, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment;filename= %s' % f)
    message.attach(part)

# mail connect
server = smtplib.SMTP('smtp.gmail.com', port=587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(email_user, password)
text = message.as_string()
server.sendmail(message["From"], message["To"].split(",") + message["Cc"].split(","),text)
server.quit()
