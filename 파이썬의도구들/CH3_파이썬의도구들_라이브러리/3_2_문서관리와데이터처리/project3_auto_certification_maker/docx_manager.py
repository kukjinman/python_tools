import os
from docx import Document

output_directory = 'output'

#4 create_certificates 함수
def create_certificates(list_var, template_path):

    for item in list_var:
        number_, class_, name_ = item

        #5 수료증의 number, class, name 값 교체
        doc = Document(template_path)

        for paragraph in doc.paragraphs:
            for run in paragraph.runs:
                if 'number' in run.text:
                    run.text = run.text.replace('number', str(number_))
                if 'class' in run.text:
                    run.text = run.text.replace('class', class_)
                if 'name' in run.text:
                    run.text = run.text.replace('name', name_)

        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        #6 수정된 문서를 새 파일로 저장
        output_path = output_directory + f'/certificate_{name_}.docx'
        doc.save(output_path)
