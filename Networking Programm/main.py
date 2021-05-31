import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.world4you.com', 25)

server.ehlo()

with open('password.txt', 'r') as f:
    password = f.read()
#Enter you mail id
server.login('xyzg@gmail.com', password)

msg = MIMEMultipart()
msg['From'] = 'NeuralNine'
msg['To'] = 'testmail@spam1.de'
msg['Subject'] = 'Just a text'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'coding.jfif'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
#Enter the mail id from you the mail has to be send
server.sendmail('mailtesting@neuraline.com', 'testmails@spaml.de', text)