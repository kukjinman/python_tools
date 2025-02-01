#1 os와 docx_manager 모듈 가져오기
import os
from docx import Document

output_directory = 'output'

#2 수료증을 생성하는 함수입니다.
def create_certificates(list_var, template_path):

    #3 리스트를 순회하며 number, class, name 값을 추출합니다.
    for item in list_var:
        number_, class_, name_ = item

        #4 템플릿 문서를 로드합니다.
        doc = Document(template_path)

        #5 템플릿 문서의 각 문단을 순회하며 number, class, name 값을 교체합니다.
        for paragraph in doc.paragraphs:
            for run in paragraph.runs:
                if 'number' in run.text:
                    run.text = run.text.replace('number', str(number_))
                if 'class' in run.text:
                    run.text = run.text.replace('class', class_)
                if 'name' in run.text:
                    run.text = run.text.replace('name', name_)

        #6 출력 폴더가 없으면 생성합니다.
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        #7 수정된 문서를 새 파일로 저장합니다.
        output_path = output_directory + f'/certificate_{name_}.docx'
        doc.save(output_path)
