
from pyxl_manager import read_certification_list
from docx_manager import create_certificates

# Example usage
file_path = 'resource/파이썬수료증리스트.xlsx'
template_file_path = 'resource/수료증_template.docx'
certification_list = read_certification_list(file_path)
print(certification_list)
create_certificates(certification_list, template_file_path)