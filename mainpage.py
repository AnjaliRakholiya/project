# Emerging Technologies Project
# This is the python file for main home page

from flask import Flask, redirect, url_for, render_template, request
import os
from database_operations import mongodb_contactus_insert

import pymongo

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/managebooking")
#@app.route("/")
def managebooking():
    return render_template("managebooking.html")

@app.route("/contactus")
#@app.route("/")
def contactus():
    return render_template("contactus.html")

@app.route("/register")
#@app.route("/")
def register():
    return render_template("register.html")

@app.route("/login")
#@app.route("/")
def login():
    return render_template("login.html")

#http://127.0.0.1:5000/registerdata
@app.route("/registerdata", methods = ['POST','GET'])
def registerdata():
    from database_operations import mongodb_user_register
    title = "MISS"
    firstname = "Anjali"
    lastname = "Rakholiya"
    name_on_card = "AR"
    birthdate = "06-20-1998"
    mothers_maiden_name = "Bavisiya"
    passport = "S7585236"
    passport_expiry_date = "20/06/1998"
    password = "123"

    result = ''
    mongodb_user_register(title, firstname, lastname, name_on_card, birthdate, mothers_maiden_name, passport,
                          passport_expiry_date, password)
    return render_template("home.html")


#http://127.0.0.1:5000/contactusdata
@app.route("/contactusdata", methods = ['POST'])
def contactus_data():
    from database_operations import mongodb_contactus_insert
    if request.method == "POST":
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        emailid = request.form.get('emailid')
        contact = request.form.get('contact')
        dob = request.form.get('dob')
        city = request.form.get('city')
        state = request.form.get('state')
        country = request.form.get('country')
        subject = request.form.get('subject')

        result = '''
        <body bgcolor="lightblue">
        <h1>Data has been inserted!!</h1>
        <h1>Entered Information :</h1>
        <p>First Name : {}</p>
        <p>Last Name : {}</p>
        <p>Email ID : {}</p>
        <p>Contact : {}</p>
        <p>DOB : {}</p>
        <p>City : {}</p>
        <p>State : {}</p>
        <p>Country : {}</p>
        <p>Subject : {}</p>
        <h3>Please give us 24hours, our team would be surely get back to you!!</h3>
        <h3>Note: Hours of operation: Monday to Friday 10AM to 5PM</h3>
        </body>
        '''
        mongodb_contactus_insert(firstname, lastname, emailid, contact, dob, city, state, country, subject)
    return result.format(firstname, lastname, emailid, contact, dob, city, state, country, subject)

#http://127.0.0.1:5000/contactusfilleddata
@app.route("/contactusfilleddata")
def contactus_filled_data():
    connection_string = "mongodb+srv://root:root@cluster0.dhp4w.mongodb.net/emerging_final_project?retryWrites=true&w=majority"
    #connection_string = "mongodb+srv://dbUser:admin@cluster0.irwc3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    my_client = pymongo.MongoClient(connection_string)
    db = my_client["emerging_final_project"]
    cairlambton = db["airlambton"]
    columns = {"First_Name", "Last_Name", "Email_ID", "Contact_Number", "Date_Of_Birth", "City", "State", "Country", "Subject"}
    result = cairlambton.find({}, columns)
    fetched_first_name = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fetched_last_name = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fetched_email_id = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fetched_contact_number = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fetched_date_of_birth = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fetched_city = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fetched_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fetched_country = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fetched_subject = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    i = 0
    count = 0
    for row in result:
        fetched_first_name[i] = row['First_Name']
        fetched_last_name[i] = row['Last_Name']
        fetched_email_id[i] = row['Email_ID']
        fetched_contact_number[i] = row['Contact_Number']
        fetched_date_of_birth[i] = row['Date_Of_Birth']
        fetched_city[i] = row['City']
        fetched_state[i] = row['State']
        fetched_country[i] = row['Country']
        fetched_subject[i] = row['Subject']
        i = i + 1
        print(row)

    resultdisplay = '''
            <html lang="en">
            <head>
            <link rel="stylesheet" href="static/style.css">
            </head>
            <body bgcolor=#f7eaea>
            <div class="contactusdisplay">
                <hr/><hr/><h1>Hi Admin! Here is your data!!</h1><hr/><hr/>
                <h3>Contact Us Information :</h3><hr/>
                <h3>Query 1 : </h3><h4>Name : {} {} <br/> Email ID : {} <br/> Contact Number : {} <br/> Date Of Birth : {} <br/> City : {} <br/> State : {} <br/> Country : {} <br/> Query : {}</h4><hr/>
                <h3>Query 2 : </h3><h4>Name : {} {} <br/> Email ID : {} <br/> Contact Number : {} <br/> Date Of Birth : {} <br/> City : {} <br/> State : {} <br/> Country : {} <br/> Query : {}</h4><hr/>
                <h3>Query 3 : </h3><h4>Name : {} {} <br/> Email ID : {} <br/> Contact Number : {} <br/> Date Of Birth : {} <br/> City : {} <br/> State : {} <br/> Country : {} <br/> Query : {}</h4><hr/>
                <h3>Query 4 : </h3><h4>Name : {} {} <br/> Email ID : {} <br/> Contact Number : {} <br/> Date Of Birth : {} <br/> City : {} <br/> State : {} <br/> Country : {} <br/> Query : {}</h4><hr/>
                <h3>Query 5 : </h3><h4>Name : {} {} <br/> Email ID : {} <br/> Contact Number : {} <br/> Date Of Birth : {} <br/> City : {} <br/> State : {} <br/> Country : {} <br/> Query : {}</h4><hr/>
            </div>
            </body>
            </html>
                        '''
    return resultdisplay.format(fetched_first_name[0], fetched_last_name[0], fetched_email_id[0], fetched_contact_number[0], fetched_date_of_birth[0], fetched_city[0], fetched_state[0], fetched_country[0], fetched_subject[0],
                                fetched_first_name[1], fetched_last_name[1], fetched_email_id[1], fetched_contact_number[1], fetched_date_of_birth[1], fetched_city[1], fetched_state[1], fetched_country[1], fetched_subject[1],
                                fetched_first_name[2], fetched_last_name[2], fetched_email_id[2], fetched_contact_number[2], fetched_date_of_birth[2], fetched_city[2], fetched_state[2], fetched_country[2], fetched_subject[2],
                                fetched_first_name[3], fetched_last_name[3], fetched_email_id[3], fetched_contact_number[3], fetched_date_of_birth[3], fetched_city[3], fetched_state[3], fetched_country[3], fetched_subject[3],
                                fetched_first_name[4], fetched_last_name[4], fetched_email_id[4], fetched_contact_number[4], fetched_date_of_birth[4], fetched_city[4], fetched_state[4], fetched_country[4], fetched_subject[4])

@app.route("/faq")
#@app.route("/")
def faq():
    return render_template("faq.html")

@app.route("/covidupdate")
#@app.route("/")
def covidupdate():
    return render_template("covidupdate.html")

@app.route("/luggage")
#@app.route("/")
def luggage():
    return render_template("luggage.html")

@app.route("/admin")
#@app.route("/")
def admin():
    return render_template("admin.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
    #connect_to_mongodb()