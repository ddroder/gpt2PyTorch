#TODO: add text fields for summary
#TODO: add upload functionality
#TODO: add bootstrap buttons to make things pretty
#TODO: add flashing
#TODO: Add user input range of pages for context (page 30 - page 150)
#TODO:

from flask import Flask,url_for,request,render_template
from pipelineSummarize import aiReadingModels
from flask_bootstrap import Bootstrap
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/summaryModel")
def summary_model():
    return render_template("summaryModel.html")

@app.route("/qaModel")
def qa_model():
    return render_template("qaModel.html")

if __name__=="__main__":
    app.run(debug=True)

