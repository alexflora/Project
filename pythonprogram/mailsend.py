# send the mail to single user;
"""import smtplib
username=input("Enter username :")
password=input("Enter the password: ")
sender=input("Enter the email: ")
receiver=input("Enter receiver password : ")
message=input("Enter the message: ")
connection =smtplib.SMTP('smtp.gmail.com',587)
connection.starttls()
connection.login(username,password)
connection.sendmail(sender,receiver,message)
connection.quit()"""
#-------------------------------------------------------------------------------
#send the mail to the multiple users(1st)
"""import smtplib 

try:
    # Set sender mail, receivers mail and messages
    sender_mail = "sender@domain.com"
    receivers_mail = ['receiver1@domain', 'receiver2@domain']
    to = ", ".join(receivers_mail)
    message = """Subject: Python testing mail

            This mail is sent using Python SMTP."""
    
    # Make SMTP connection
    obj = smtplib.SMTP('smtp.gmail.com', 587) 
  
    # secure with TLS
    obj.starttls() 
  
    # Mail Server Authentication
     obj.login(USRENAME, PASSWORD) 
  
    # sending the mail 
    obj.sendmail(sender_mail, to, message) 
    print("Mail sent successfully.")
    
    # terminating the session 
    obj.quit()
    
except Exception:
    print("Mail delivery failed.")"""
#-------------------------------------------------------------------------------
#send multiple users (2 nd example)
    
"""import smtplib
from email.mime.text import MIMEText

s = smtplib.SMTP('smtp.live.com')
s.set_debuglevel(1)
msg = MIMEText("""body""")
sender = 'me@example.com'
recipients = ['john.doe@example.com', 'john.smith@example.co.uk']
msg['Subject'] = "subject line"
msg['From'] = sender
msg['To'] = ", ".join(recipients)
s.sendmail(sender, recipients, msg.as_string())
s.quit()"""

#-------------------------------------------------------------------------------
#send multi user (3 rd example)
"""
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import smtplib

msg = MIMEMultipart()
msg["Subject"] = "Example"
msg["From"] = "me@example.com"
msg["To"] = "malcom@example.com,reynolds@example.com,firefly@example.com"
msg["Cc"] = "serenity@example.com,inara@example.com"
body = MIMEText("example email body")
msg.attach(body)
smtp = smtplib.SMTP("mailhost.example.com", 25)
smtp.sendmail(msg["From"], msg["To"].split(",") + msg["Cc"].split(","), msg.as_string())
smtp.quit()"""


    
