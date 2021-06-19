# Emerging Technologies Project
# This is the python file for main home page

from flask import Flask, redirect, url_for, render_template, request
import os

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

#http://127.0.0.1:5000/contactusdata
@app.route("/contactusdata", methods = ['POST'])
def contactus_data():
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
        '''
    return result.format(firstname, lastname, emailid, contact, dob, city, state, country, subject)

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

if __name__ == "__main__":
    app.run()