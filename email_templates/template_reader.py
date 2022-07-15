# -*- coding: utf-8 -*-
class TemplateReader:
    def __init__(self):
        pass

    def read_course_template(self,patientName,patientEmail,patientContactNumb,drName,dayAppointment,timeAppointment):
        try:
            Appointment_day = dayAppointment.split('-')[0]
            
            myEmailString = "Hi, {0} We are pleased to inform you that your appointment with {1} has been confirmed On {2} at {3}, Thankyou for using Sehat App."
            formattedEmailString = myEmailString.format(patientName, drName, Appointment_day, timeAppointment)

            content = "<body><p>%s<p></body>" % (formattedEmailString) 
            with open('email_templates/CS_email_template.html', 'w') as newHTMLFile:
                newHTMLFile.write(content)
                newHTMLFile.close()


            email_file = open("email_templates/CS_email_template.html", "r")
            email_message = email_file.read()
            return email_message
        except Exception as e:
            print('The exception is '+str(e))


    def read_support_template(self,patientName,patientEmail,patientContactNumb,drName,dayAppointment,timeAppointment):
        try:
            Appointment_day = dayAppointment.split('-')[0]
            
            myEmailString01 = "Hi Support, We got another appointment. Please assist him according to our policies, Patient Data is: \n"
            myEmailString02 = "Patient Name: {0}\nPatient Email Address: {1}\nDoctorName: {2}\nAppointment Day: {3}\nAppointment Time: {4}"


            formattedEmailString = myEmailString02.format(patientName, patientEmail, drName, Appointment_day, timeAppointment)
            
            completeString = myEmailString01 + formattedEmailString


            content = "<body><p>%s<p></body>" % (completeString) 
            with open('email_templates/CS_email_template.html', 'w') as newHTMLFile:
                newHTMLFile.write(content)
                newHTMLFile.close()


            email_file = open("email_templates/CS_email_template.html", "r")
            email_message = email_file.read()
            return email_message
        except Exception as e:
            print('The exception is '+str(e))



