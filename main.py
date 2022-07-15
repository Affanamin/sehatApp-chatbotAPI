# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from flask import Flask, render_template, request
import json
from flask import make_response
from SendEmail.sendEmail import EmailSender
from email_templates import template_reader
import os

IMG_FOLDER = os.path.join('static', 'images')
CSV_FOLDER = os.path.join('static', 'CSVs')
app = Flask(__name__)
app.config['IMG_FOLDER'] = IMG_FOLDER
app.config['CSV_FOLDER'] = CSV_FOLDER


@app.route('/webhook', methods=['POST'])
def webhook():
    # First interaction, request will drop here
    req = request.get_json(silent=True, force=True)
    # Sending our request to another function, so that we can parse
    res = processRequest(req)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def processRequest(req):
    # parsing our data, got from req
    sessionID = req.get('responseId')
    result = req.get("queryResult")
    outputContexts = result.get("outputContexts")
    params = outputContexts[0].values()

    paramsList = list(params)
    impParams = paramsList[2]

    # Got patient name, email, contact number, appointment date, day, dr nae from here.
    patientName = impParams["patientName.original"]
    patientEmail = impParams["patientEmail.original"]
    patientContactNumb = impParams["patientNumber.original"]
    
    params001 = outputContexts[1].values()
    paramsList001 = list(params001)
    impParams001 = paramsList001[2]

    drName = impParams001["drName.original"]
    dayAppointment = impParams001["date-period.original"]
    timeAppointment = impParams001["date-time.original"]
    
    # Sending Email to our patient Starts from here
    email_sender = EmailSender()
    template = template_reader.TemplateReader()
    
    email_message = template.read_course_template(patientName,patientEmail,patientContactNumb,drName,dayAppointment,timeAppointment)
    email_sender.send_email_to_student(patientEmail, email_message)

    #Sending Email to support from here
    emailMessageSupport = template.read_support_template(patientName,patientEmail,patientContactNumb,drName,dayAppointment,timeAppointment)
    email_sender.send_email_to_support(emailMessageSupport )
    
    # Sending Fulfilment text from here

    fulfillmentText = "I have sent all details regarding your appointment with " + drName + " on email: " + patientEmail+ ", Please Be on time, thanks "
    return {"fulfillmentText": fulfillmentText}

    

@app.route('/',methods=['GET'])
def homePage():
	return render_template("index.html")


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0')
    #app.run()
