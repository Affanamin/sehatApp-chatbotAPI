# -*- coding: utf-8 -*-
import smtplib as smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from config_reader import ConfigReader

class EmailSender:

    def send_email_to_student(self, recepient_email, message):
        try:
            
            EMAIL_ADDRESS = 'universityservice81@gmail.com'
            EMAIL_PASSWORD = 'qlporlssfsqwndba'
            
            self.config_reader=ConfigReader()
            self.configuration=self.config_reader.read_config()

            # instance of MIMEMultipart
            self.msg = MIMEMultipart()

            # storing the senders email address
            self.msg['From'] = self.configuration['SENDER_EMAIL']

            # storing the receivers email address
            self.msg['To'] = recepient_email
            
            # storing the subject
            self.msg['Subject'] = self.configuration['EMAIL_SUBJECT']

            # string to store the body of the mail
            #body = "This will contain attachment"
            body=message

            # attach the body with the msg instance
            self.msg.attach(MIMEText(body, 'html'))


            # instance of MIMEBase and named as p
            self.p = MIMEBase('application', 'octet-stream')
        
            # creates SMTP session
            #self.smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            #self.smtp = smtplib.SMTP_SSL('smtp.gmail.com')
            
            msg = "Hello Everyone, This is our Test email"
            self.text = self.msg.as_string()


            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                #smtp.login(self.msg['SENDER_EMAIL'], self.configuration['PASSWORD'])
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                #smtp.send_message(msg)
                smtp.sendmail(self.msg['From'] , recepient_email, self.text)

        except Exception as e:
            print('the exception is '+str(e))

    def send_email_to_support(self,body):
            try:
                
                EMAIL_ADDRESS = 'universityservice81@gmail.com'
                EMAIL_PASSWORD = 'qlporlssfsqwndba'
                
                self.config_reader = ConfigReader()
                self.configuration = self.config_reader.read_config()

                # instance of MIMEMultipart
                self.msg = MIMEMultipart()

                # storing the senders email address
                self.msg['From'] = self.configuration['SENDER_EMAIL']
               


                # storing the subject
                self.msg['Subject'] = self.configuration['SALES_TEAM_EMAIL_SUBJECT']
                
            
                # attach the body with the msg instance
                self.msg.attach(MIMEText(body, 'html'))

                # instance of MIMEBase and named as p
                self.p = MIMEBase('application', 'octet-stream')
                
                support_team_email = 'universityservice81@gmail.com'
                ##################################################
                self.text = self.msg.as_string()
                self.text2 = "Working in this"
                print("This is the diff.\n")

                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    
                    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                    
                    smtp.sendmail(self.msg['From'], support_team_email, self.text)

            except Exception as e:
                print('the exception is ' + str(e))
