#1 pyxl_manager와 docx_manager 모듈 가져오기
from pyxl_manager import read_certification_list
from docx_manager import create_certificates

#2 엑셀 파일 경로와 수료증 템플릿 파일 경로를 지정합니다.
file_path = 'resource/파이썬수료증리스트.xlsx'
template_file_path = 'resource/수료증_template.docx'

#3 엑셀 파일을 읽어서 수료증을 생성합니다.
certification_list = read_certification_list(file_path)
print(certification_list)
create_certificates(certification_list, template_file_path)