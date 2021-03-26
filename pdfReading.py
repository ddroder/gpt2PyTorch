from docx import Document
import PyPDF2
class reader():
    def __init__(self):
        #just empty
        pass
    def read_pdf_file(self,filepath,pageToExtract):
        pdfFileObj=open(filepath,'rb')
        pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
        print(pdfReader.numPages)
        pageText=pdfReader.getPage(pageToExtract)
        print(pageText)
        pageText2=pageText.extractText()
        print(pageText2)
        pdfFileObj.close()
        return pageText2
    def read_txt_file(self,filepath):
        with open(filepath.filename,"r") as file:
            data=file.read()
            return data
    def read_doc_file(self,filepath):
        doc=Document(filepath)
        # print(document)
        full_text=[]
        for para in doc.paragraphs:
            full_text.append(para.text)
        return '\n'.join(full_text)


# i=reader()
# c=i.read_doc_file("/nvme_ssd/edClass/hwWeek6.docx")
# print(c)