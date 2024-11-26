# -*- coding: utf-8 -*-
"""
=@author: sucre
"""

from email.message import EmailMessage
import smtplib, ssl
import ssl

sender = "beroberts@slcolibrary.org"
recipient = "beroberts@slcolibrary.org"
p = 'Hypn0sis!slcls'
message = "Hello world!"
port = 587
#port = 465  # For SSL

email = EmailMessage()
email["From"] = sender
email["To"] = recipient
email["Subject"] = "Test Email"
email.set_content(message)


#print(ssl.OPENSSL_VERSION)

#"""

print(1)

#password = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()
print(2)

with smtplib.SMTP_SSL("smtp-mail.outlook.com", port) as server:
    print(3)
    server.ehlo()
    print(4)
    server.starttls(context=context)
    print(5)
    server.ehlo()
    print(6)
    server.login(sender, p)
    print(7)
    server.sendmail(sender, recipient, email.as_string())
    print(8)
    server.quit()
    print(9)

# smtp = smtplib.SMTP("smtp-mail.outlook.com", port)
# smtp.starttls()
# smtp.login(sender, p)
# smtp.sendmail(sender, recipient, email.as_string())
# smtp.quit()

print('email sent')

#"""