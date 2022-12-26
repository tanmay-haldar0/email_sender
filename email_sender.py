# go over to our gmail account and setup 2 factor authentication
# generate app password
# create a function to send the email

from email.message import EmailMessage
import ssl
import smtplib


email_sender = str(input("Enter sender email address :"))
print("")
email_password = str(input("Enter sender app password :"))
print("")

email_receiver = str(input("Enter receiver email address : "))
print("")

subject = str(input("Enter email subject : "))
print("")

body =str(input("Enter your email body : "))
print("")

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)


context= ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())
