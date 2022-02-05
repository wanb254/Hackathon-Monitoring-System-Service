import schedule
import time
import nmap, socket
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

HOSTNAME = ['www.mwandishi.co.ke','www.nhif.co.ke','www.maseno.ac.ke','www.google.com','www.github.com',]
ports = [8080,80,70,100,200,300,400,8041]

services = [
    {"port": "80",
     "description":"Notifiy service"
     },
    {"port": "8080",
     "description":"Database service"
     },
    {"port": "8041",
     "description":"Messaging service"
     },
    {"port": "8082",
     "description":"Triage service"
     },
    {"port": "8083",
     "description":"Reports service"
     },
    {"port": "8084",
     "description":"Lab service"
     },
    
    
    ]

res = [sub['port']for sub in services]
res1 = [sub['description']for sub in services]
  
def func():

    
    
    hostname = HOSTNAME
    for host in hostname:
        host = str(host)
        print(host)
        response = os.system("ping " + host)
        # and then check the response...
        if response == 0:
            
            pingstatus = "Network Active"
            print(pingstatus)
        else:
            pingstatus = "Network Error"
            print(pingstatus)
            mail_content = host + ' Server is Down'
            #The mail addresses and password
            sender_address = 'pkagwe07@gmail.com'
            sender_pass = 'kagwepeter07@gmail.com'
            receiver_address = 'kagwepeter07@gmail.com'
            #Setup the MIME
            message = MIMEMultipart()
            message['From'] = sender_address
            message['To'] = receiver_address
            message['Subject'] = 'Alert!'   #The subject line
            #The body and the attachments for the mail
            message.attach(MIMEText(mail_content, 'plain'))
            #Create SMTP session for sending the mail
            session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
            session.starttls() #enable security
            session.login(sender_address, sender_pass) #login with mail_id and password
            text = message.as_string()
            session.sendmail(sender_address, receiver_address, text)
            session.quit()
            print('Mail Sent')

    for element in res:
        new_element = int(element)
        ind = res.index(element)
        des = res1[ind]
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('mwandishi.co.ke', new_element))
        if result == 0:
            print(des + ' port is working')
            
        else:

            print(des + ' not working')
  
schedule.every(5).minutes.do(func)
  
while True:
    schedule.run_pending()
    time.sleep(5)
