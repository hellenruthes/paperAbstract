import PyPDF2
from PyPDF2 import PdfFileWriter, PdfFileReader


def pdf_file_obj(dir, file_name):
    pdffileobj=open(dir+'/'+file_name,'rb')
    pdfreader=PyPDF2.PdfFileReader(pdffileobj)
    x=pdfreader.numPages
    pageobj=pdfreader.getPage(0)
    text=pageobj.extractText()
    #print(text)
    return text

def get_piece_of_text(s, first, last):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""