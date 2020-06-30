import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
host_address = "g.di*******@gmail.com" ##add your email 
host_pass = "********" ## add your password
guest_address = "anuraj********@gmail.com" ## add developer email
subject = "Regarding failure of Web Application deployed"
content = '''Hello Developer, 
This is an email with respect to the webpage you deployed . It seems that there is some error with the file as it is not working correctly. Kindly rectify the errors and deploy again.

THANK YOU'''

message = MIMEMultipart()
message['From'] = host_address
message['To'] = guest_address
message['Subject'] = subject
message.attach(MIMEText(content, 'plain'))
session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(host_address, host_pass)
text = message.as_string()
session.sendmail(host_address, guest_address  , text)
session.quit()
print('Successfully sent your mail')
