import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def sent():
    f = open("receiver_list.txt", "r")
    my_file_data = f.read()
    print(my_file_data)


fromaddr = "anime12mang@gmail.com"
toaddr = sent
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Final_Project"
 
body = "Berhasil"
 
msg.attach(MIMEText(body, 'plain'))
# Lampiran, sesuaikan nama filename dengan nama di attachment
filename = "receiver_list.txt"
attachment = open("receiver_list.txt", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "naufalrahman96")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
