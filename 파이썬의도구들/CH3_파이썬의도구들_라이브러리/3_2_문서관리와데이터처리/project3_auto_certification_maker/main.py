from pyxl_manager import read_certification_list
from docx_manager import create_certificates

file_path = 'resource/파이썬수료증리스트.xlsx'
template_file_path = 'resource/수료증_template.docx'

#0 수료증 인원 정보 리스트를 생성
certification_list = read_certification_list(file_path)
print(certification_list)

#3 수료증 생성
create_certificates(certification_list, template_file_path)