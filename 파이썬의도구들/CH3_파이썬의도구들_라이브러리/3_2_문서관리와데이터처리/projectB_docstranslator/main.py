#0 os와 docx_manager, trans_manager 모듈 가져오기
import os
from docx_manager import read_docx_files
from docx_manager import write_docx_files
from trans_manager import translate_contents

input_directory = 'docs_example'
output_directory = 'output'

#1 input_directory의 파일 순회
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
