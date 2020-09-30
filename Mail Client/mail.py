import os
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

smtplib.SMTP_SSL()
smtplib.SMTP()
smtplib.SMTP('smtp.gmail.com', 587)
server = smtplib.SMTP('smtp.gmail.com', 25)
server.connect('smtp.gmail.com',465)
server.ehlo()



with open('password.txt', 'r') as f:
    password = f.read()

server.login('donaberius@gmail.com', password)

msg = MIMEMultipart
msg['from'] = donaberius
msg['To'] = 'jose@alvaka.net'
msg['Subject'] = 'Just a Message'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename ='coding.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachement: filename={filename}')
msg.attach(p)

text = msg.as_string
server.sendmail('donaberius@gmail.com', 'jose@alvaka.net', text)
