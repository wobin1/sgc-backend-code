import smtplib
from email.message import EmailMessage

class Helperfunctions():

    def sendEmail(body, subject, sender, reciever, sender_password):

        msg = EmailMessage()

        msg.set_content(body)
        msg["subject"] = subject
        msg["From"] = sender
        msg["To"] = reciever

        print('0')
        
        driver = smtplib.SMTP('smtp.gmail.com', 587)

        print(('1'))
        driver.starttls()
        print('2')
        driver.login(sender, sender_password)
        print('3')
        driver.send_message(msg)

        return "Email succellfully sent"



