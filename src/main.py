'''
Created on May 13, 2013

@author: jacob
'''

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from random import choice
import time

me = "lyraj@lavabit.com"

username = "lyraj"
password = input('Enter password:')

text1 = "Witaj!\nWybraliśmy Twojego partnera korespondencyjnego, jest nim "
text2 = "\nW razie jakichkolwiek problemów piszcie na ten mail. Bawcie się dobrze!\n\nLyra"

html1 = """\
<html>
  <head></head>
  <body>
    <p>Witaj!<br>
     Wybraliśmy Twojego partnera korespondencyjnego, jest nim 
"""
html2 = """\
<br> W razie jakichkolwiek problemów piszcie na ten mail. Bawcie się dobrze! <br>
<br> Lyra
    </p>
  </body>
</html>
"""

conn = smtplib.SMTP('lavabit.com')
conn.login(username, password)


plik = open("/home/jacob/maile", "r")
maile = []
for line in plik:
    maile.append(line[:-1])
    
print(maile)

msg = MIMEMultipart('alternative')
msg['Subject'] = "Twój partner korespondencyjny"
msg['From'] = "lyraj@lavabit.com"

while maile: 
    user1 = ''
    user2 = ''
    while (user1 == user2 or (user1.split(sep=' ')[1] == user2.split(sep=' ')[1])):
        user1 = choice(maile)
        user2 = choice(maile)
    
    maile.remove(user1)
    maile.remove(user2)
    
    user1 = user1.split(sep=' ')[0]
    user2 = user2.split(sep=' ')[0]

    
    print("%s <-> %s" %(user1, user2))
    
    msg['To'] = user1
    part1a = MIMEText(text1 + user2 + text2, 'plain')
    part2a = MIMEText(html1 + user2 + " " + html2, 'html')
    msg.attach(part1a)
    msg.attach(part2a)
    try: 
        conn.sendmail(me, user1, msg.as_string())
        pass
    finally: 
        print("%s sent" %user1)
    time.sleep(5)
    
        
    msg['To'] = user2
    part1b = MIMEText(text1 + user1 + text2, 'plain')
    part2b = MIMEText(html1 + user1 + " " + html2, 'html')
    msg.attach(part1b)
    msg.attach(part2b)
    try:
        conn.sendmail(me, user2, msg.as_string())
        pass
    finally: 
        print("%s sent" %user2)
    time.sleep(5)
    


conn.quit()
print("done")