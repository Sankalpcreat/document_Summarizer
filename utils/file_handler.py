import pdfplumber

def read_pdf_file(file_path:str)->str:

    with pdfplumber.open(file_path) as pdf:
        text=''
        for page in pdf.pages:
            text+=page.extract_text() or ''
    return text

def read_text_file(file_path:str)->str:
    with open(file_path,'r',encoding='utf-8') as file:
        return file.read()