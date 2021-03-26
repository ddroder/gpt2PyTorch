from flask import Flask,url_for,request,render_template,flash
from pipelineSummarize import aiReadingModels
from flask_bootstrap import Bootstrap
from pdfReading import reader
import os
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['MAX_CONTENT_LENGTH'] = 5024 * 5024
def text_display(file,ext,method,summary_upload_html,page_to_extract=0,question=0):
    read=reader()
    if ext=="pdf":
        data=read.read_pdf_file(file,pageToExtract=page_to_extract)
    elif ext=="txt":
        data=read.read_txt_file(file)
    model=aiReadingModels()
    if method=="summary":
        generator=model.summaryGeneration(data)
    elif method=="qa":
        context=data
        generator=model.qaModelGeneration(context=context,question=question)
    flash(generator,category="success")
    if ext=="pdf":
        os.remove(file)
    else:
        os.remove(file.filename)
    return render_template(summary_upload_html)
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
            if uploaded_file.filename.endswith(".txt"):
                text_display(uploaded_file,ext="txt",method="summary",summary_upload_html=summary_upload_html) # summary for txt
            elif uploaded_file.filename.endswith(".pdf"):
                text_display(uploaded_file.filename,ext="pdf",method="summary",summary_upload_html=summary_upload_html) # summary for pdf
            elif uploaded_file.filename.endswith(".docx"):
                text_display(uploaded_file.filename,ext="docx",method="summary",summary_upload_html=summary_upload_html) #return summary for docx
        return render_template(summary_upload_html) #this means a file was uploaded that was allowed but was not found in any of the conditions
    return render_template(summary_upload_html) #default return when the user logs onto the webpage

@app.route("/qaUpload",methods=["GET","POST"])
def qa_upload():
    if request.method=="POST":
        qa_upload_html="qaUpload.html"
        question=request.form['question']
        context=request.files['file']
        context.save(context.filename)
        if context!="":
            if context.filename.endswith(".txt"):
                text_display(file=context,question=question,ext="txt",method="qa",summary_upload_html=qa_upload_html) # summary for txt
            return render_template(qa_upload_html)
        return render_template(qa_upload_html)

        # model=aiReadingModels()
        # qaGen=model.qaModelGeneration()

    return render_template("qaUpload.html")

if __name__=="__main__":
    app.run(debug=True)

