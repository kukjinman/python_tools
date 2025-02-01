#1 os와 docx_manager, trans_manager 모듈 가져오기
import os
from docx_manager import read_docx_files
from docx_manager import write_docx_files
from trans_manager import translate_contents

#2 번역할 문서가 있는 폴더와 번역된 문서를 저장할 폴더를 지정합니다.
input_directory = 'docs_example'
output_directory = 'output'

#3 번역할 문서를 읽어서 번역하고 번역된 문서를 저장합니다.
for docx_file in os.listdir(input_directory):
    f_path = "docs_example/"
    print(f"docx_file: {docx_file}")
    f_path+=docx_file
    print(f"f_path: {f_path}")
    cur_data = read_docx_files(f_path)
    print(f"cur_data: {cur_data}")
    result = translate_contents(cur_data)
    print(f"result: {result}")
    write_docx_files(result, output_directory, docx_file)
