from flask import Flask, render_template, request
from urllib.request import urlopen
import json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        condition = request.form.get("condition")
        search_url = "https://ClinicalTrials.gov/api/query/study_fields?fmt=JSON&expr=%s&max_rnk=100&fields=EnrollmentCount,OutcomeAnalysisPValue,Condition,BriefTitle,EligibilityCriteria" % (condition)
        response=urlopen(search_url)
        data_json = json.loads(response.read())
        return render_template("results.html", x = data_json)