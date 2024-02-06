import os
from PyPDF2 import PdfReader
from pdf2docx import Converter

def is_pdf_file(filepath):
    return filepath.endswith(".pdf")

def get_output_filepath(filepath):
    return filepath.replace(".pdf", ".docx")

def get_num_pages(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    return len(pdf_reader.pages)

def convert_pdf_to_docx(filepath, output_filepath):
    with open(filepath, "rb") as pdf_file, open(output_filepath, "wb") as docx_file:
        num_pages = get_num_pages(pdf_file)
        converter = Converter(pdf_file)
        converter.convert(docx_file, start=0, end=num_pages)
        converter.close()
        
def show_convertion_message():
    print("PDF converted to DOCX.")

def convert_pdf_to_docx(filepath):
    output_filepath = get_output_filepath(filepath)
    convert_pdf_to_docx(filepath, output_filepath)
    return output_filepath
    
def open_file(filepath):
    os.system(f"start {filepath}")
    
def is_file_exist(filepath):
    return os.path.exists(filepath)
    
def convert_pdf_to_docx_and_open():
    filepath = input("Enter the file path: ")

    if not is_file_exist(filepath):
        print("The file does not exist.")
        return
    
    if not is_pdf_file(filepath):
        print("The file is not in PDF format.")
        return
    
    output_filepath = convert_pdf_to_docx(filepath)
    show_convertion_message()
    open_file(output_filepath)

if __name__ == "__main__":
    convert_pdf_to_docx_and_open()
