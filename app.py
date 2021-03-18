#TODO: add text fields for summary
#TODO: add upload functionality
#TODO: add bootstrap buttons to make things pretty
#TODO: add flashing
#TODO: Add user input range of pages for context (page 30 - page 150)
#TODO: General text generation

from flask import Flask,url_for,request,render_template,flash
from pipelineSummarize import aiReadingModels
from flask_bootstrap import Bootstrap
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/summaryModel",methods=['POST','GET'])
def summary_model():
    if request.method=="POST":
        text=request.form['text']
        # print(f"{text}")
        flash(text,category="success")
        return render_template("summaryModel.html")
    return render_template("summaryModel.html")

@app.route("/qaModel")
def qa_model():
    return render_template("qaModel.html")

if __name__=="__main__":
    app.run(debug=True)

