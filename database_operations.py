from flask import Flask, redirect, url_for, render_template, request
import os
import pymongo


def mongodb_contactus_insert(firstname, lastname, emailid, contact, dob, city, state, country, subject):
    connection_string = "mongodb+srv://root:root@cluster0.dhp4w.mongodb.net/emerging_final_project?retryWrites=true&w=majority"
    my_client = pymongo.MongoClient(connection_string)
    db = my_client["emerging_final_project"]
    cairlambton = db["airlambton"]
    # Insert Record
    mydict = {"First_Name": firstname, "Last_Name": lastname, "Email_ID": emailid, "Contact_Number": contact,
              "Date_Of_Birth": dob, "City": city, "State": state, "Country": country, "Subject": subject}
    x = cairlambton.insert_one(mydict)
    print(x)


def mongodb_user_register(title, firstname, lastname, name_on_card, birthdate, mothers_maiden_name, passport,
                          passport_expiry_date, password):
    connection_string = "mongodb+srv://root:root@cluster0.dhp4w.mongodb.net/emerging_final_project?retryWrites=true&w=majority"
    my_client = pymongo.MongoClient(connection_string)
    db = my_client["emerging_final_project"]
    cairlambton = db["user"]
    mydict = {"title": title, "firstname": firstname, "lastname": lastname, "name_on_card": name_on_card,
              "birthdate": birthdate,
              "mothers_maiden_name": mothers_maiden_name, "passport": passport,
              "passport_expiry_date": passport_expiry_date, "password": password}
    x = cairlambton.insert_one(mydict)
    print(x)
