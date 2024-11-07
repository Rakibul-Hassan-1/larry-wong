import pdfplumber
from docx import Document as DocxDocument
from django.conf import settings


# extracted text from pdf
def extract_text_from_pdf(file_path):
    text = ''
    with pdfplumber.open(file_path) as pdf:
        pages = [page.extract_text() for page in pdf.pages if page.extract_text()]
        text = '\n'.join(filter(None, pages))
    return text

# extracted text from docs
def extract_text_from_docx(file_path):
    doc = DocxDocument(file_path)
    return '\n'.join([para.text for para in doc.paragraphs if para.text])

def extract_text(file_path):
    if file_path.endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith('.docx'):
        return extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file type")


# utils.py
def replace_abbreviations_with_ipa(text):
    # Your function implementation here
    pass
