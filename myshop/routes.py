from flask import render_template,session,request,redirect,url_for

from myshop import app,db

@app.route("/")
def home():
    return "home page of your shop"

    