import os
from docx import Document

def read_docx_files(file_path):
    doc = Document(file_path)
    doc_text = ''
    for para in doc.paragraphs:
        doc_text += para.text + '\n'

    # print(doc_text)

    return doc_text

def write_docx_files(docx_data, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for file_data in docx_data:
        doc = Document()
        for paragraph in file_data['content']:
            doc.add_paragraph(paragraph)
        output_path = os.path.join(output_directory, file_data['file_name'])
        doc.save(output_path)