#TODO: add text fields for summary
#TODO: add upload functionality
#TODO: add bootstrap buttons to make things pretty
#TODO: add flashing
#TODO: Add user input range of pages for context (page 30 - page 150)
#TODO: General text generation

from flask import Flask,url_for,request,render_template,flash
from pipelineSummarize import aiReadingModels
from flask_bootstrap import Bootstrap
import os
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['MAX_CONTENT_LENGTH'] = 5024 * 5024

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/summaryModel",methods=['POST','GET'])
def summary_model():
    if request.method=="POST":
        text=request.form['text']
        model=aiReadingModels()
        summaryGeneration=model.summaryGeneration(text)
        flash(summaryGeneration,category="success")
        return render_template("summaryModel.html")
    return render_template("summaryModel.html")

@app.route("/qaModel",methods=['GET','POST'])
def qa_model():
    if request.method=='POST':
        context=request.form['context']
        question=request.form['question']
        model=aiReadingModels()
        aGeneration=model.qaModelGeneration(question=question,context=context)
        flash(aGeneration,category="success")
        return render_template("qaModel.html")
    return render_template("qaModel.html")

@app.route("/textGen",methods=['GET','POST'])
def text_gen():
    if request.method=="POST":
        # start_text="A new breed of unicorns has been discovered in the andes mountains!"
        start_text=request.form['text']
        max_length=int(request.form['max_length'])
        num_return_sequences=int(request.form['num_return_sequences'])
        model=aiReadingModels()
        textGen=model.textGen(startText=start_text,max_length=max_length,num_return_sequences=num_return_sequences)
        # print(textGen)
        flash(textGen,category="success")
        return render_template("text_gen.html")
    return render_template("text_gen.html")

@app.route("/summaryUpload",methods=['GET','POST'])
def summary_upload():
    summary_upload_html="uploadFileSummaryModel.html"
    if request.method=="POST":
        uploaded_file=request.files['file']
        uploaded_file.save(uploaded_file.filename)
        if uploaded_file!= "":
            with open(uploaded_file.filename,"r") as user_file:
                txt_to_summarize=user_file.read()
                model=aiReadingModels()
                summary_gen=model.summaryGeneration(txt_to_summarize)
                flash(summary_gen,category="success")
                os.remove(uploaded_file.filename)
                return render_template(summary_upload_html)
        return render_template(summary_upload_html)
    return render_template(summary_upload_html)
if __name__=="__main__":
    app.run(debug=True)

