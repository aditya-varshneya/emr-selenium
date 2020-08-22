import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import datetime

email_user = 'adityakumar@thb.co.in'
email_send = "satyendra@thb.co.in,nitin@thb.co.in,rajesh@thb.co.in,kritika@thb.co.in,pushkin@thb.co.in,vaibhav@thb.co.in,parameshwar@thb.co.in,charu@thb.co.in"
email_copy = 'adityakumar@thb.co.in'
password = 'aditya061287'

message = MIMEMultipart()
message['From'] = email_user
message['To'] = email_send
message['Cc'] = email_copy
message['Subject']= "Automation Testing Report - Web Application"
filename_1 = "https://drive.google.com/file/d/1k_ug0enKx-JFHv3nlNBR6_5XG9iO68jx/view?usp=sharing"
filename_2 = "https://drive.google.com/file/d/15XPSO2GNChbl0dX5RxoNa_lh47QUtAKJ/view?usp=sharing"
body = 'Hi All, Please find below the link for Automation report, link = {} and {}'.format(filename_1,filename_2)
message.attach(MIMEText(body,'plain'))

server = smtplib.SMTP('smtp.gmail.com',port=587)
server.ehlo()
server.starttls()
server.login(email_user,password)
text = message.as_string()
server.sendmail(message["From"], message["To"].split(",") + message["Cc"].split(","),text)
server.quit()