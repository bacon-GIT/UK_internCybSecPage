# FLASK_APP=mainflask.py
# Developed by Josh Bacon


from flask import Flask, render_template
import uscertparse
import datetime

app = Flask(__name__)


@app.route('/')
def table():
    timedate = ("{}\t|\t{}".format(datetime.time(), datetime.date.today()))
    return render_template("homepage.html",
                           vuln1=uscertparse.parseAlerts(0),
                           vuln2=uscertparse.parseAlerts(1),
                           vuln3=uscertparse.parseAlerts(2),
                           vuln4=uscertparse.parseAlerts(3),
                           vuln5=uscertparse.parseAlerts(4),
                           vuln6=uscertparse.parseAlerts(5),
                           timeAndDate=timedate,
                           header_img="/static/title.png")  # Expandable, just change the parameter


@app.route('/wereworkingonthat/')
def wereworkingonthat():
    return render_template("wereworkingonthat.html",
                           header_img="/static/title.png")


@app.route('/policy/')
def policy():
    return render_template("policy.html",
                           header_img="/static/title.png")
