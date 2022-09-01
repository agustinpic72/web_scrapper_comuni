import smtplib
import ssl
from email.message import EmailMessage
from time import sleep

ctx = ssl.create_default_context()
password='' #Password from gmail external apps 
sender = "example@example.com"    # Your e-mail address
receiver = "example@example.com"  # Recipient's address
message = EmailMessage()
message.set_content(f"""\
    insert your email content here
    """)
message['Subject'] = 'Subject here'
message['From'] = 'Name of the sender here'
archivo = open('mail.txt','r') #feel free to change the .txt name
archivo = archivo.read().split('\n')
x=0
server = smtplib.SMTP_SSL('smtp.gmail.com',465) #Connects to gmail smtp server, feel free to use whatever service you want

for correo in archivo:
    if x%30 == 0: #This is to have a more humane behavior, every 30 emails it'll wait 1 minute
        server.quit()
        sleep(60)
        server = smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.login(sender,password)
    if correo:
        server.login(sender,password)   
        print(x,correo)
        message['To'] = correo
        server.send_message(message)
        del message['To']
        x+=1
    else:
        print('error')
        x+=1
server.quit()
