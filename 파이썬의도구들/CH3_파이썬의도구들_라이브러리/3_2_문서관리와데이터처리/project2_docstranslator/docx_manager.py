import os
from docx import Document

def read_docx_files(directory):
    data = []
    files = os.listdir(directory)
    docx_files = [f for f in files if f.endswith('.docx')]

    for docx_file in docx_files:
        file_path = os.path.join(directory, docx_file)
        doc = Document(file_path)
        file_data = {
            'file_name': docx_file,
            'content': [paragraph.text for paragraph in doc.paragraphs]
        }
        data.append(file_data)

    return data

def write_docx_files(docx_data, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for file_data in docx_data:
        doc = Document()
        for paragraph in file_data['content']:
            doc.add_paragraph(paragraph)
        output_path = os.path.join(output_directory, file_data['file_name'])
        doc.save(output_path)