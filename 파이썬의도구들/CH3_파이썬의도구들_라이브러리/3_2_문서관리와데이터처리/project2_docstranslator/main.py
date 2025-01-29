import os

from docx_manager import read_docx_files
from docx_manager import write_docx_files
from trans_manager import translate_contents

input_directory = 'docs_example'
output_directory = 'output'

for docx_file in os.listdir(input_directory):
    f_path = "docs_example/"
    print(f"docx_file: {docx_file}")
    f_path+=docx_file
    print(f"f_path: {f_path}")
    cur_data = read_docx_files(f_path)

    result = translate_contents(cur_data)
    print(f"result: {result}")

