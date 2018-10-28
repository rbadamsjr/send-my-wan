#!/usr/bin/env python
import requests
import email
import smtplib
import re

# Note: hotmail.com / outlook.com requires the from address match that
# 		of the account email address
toAddress = '';
fromAddress = '';
emailSubject = 'Your public ip'
smtpLogin = '';
smtpPasswd = '';


url = 'https://www.ipchicken.com/';

# Getting IP address
print('Getting IP')
requestContent = requests.get(url) 
data = requestContent.text
ipPattern = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')

findIP = re.findall(ipPattern,data)

print(findIP);

# Sent email
msg = email.message_from_string("IP = {}".format(findIP))
msg['From'] = fromAddress
msg['To'] = toAddress
msg['Subject'] = emailSubject

s = smtplib.SMTP("smtp-mail.outlook.com",587)
s.ehlo() # Hostname to send for this command defaults to the fully qualified domain name of the local host.
s.starttls() #Puts connection to SMTP server in TLS mode
#s.ehlo()
s.login(smtpLogin, smtpPasswd)

s.sendmail(fromAddress, toAddress, msg.as_string())

s.quit()
