from docx_manager import read_docx_files
from docx_manager import write_docx_files
from trans_manager import translate_contents

def main():
    input_directory = r'C:\Users\thate\PycharmProjects\python_tools\파이썬의도구들\CH3_파이썬의도구들_라이브러리\3_2_문서관리와데이터처리\project2_docstranslator\docs_example'
    output_directory = r'C:\Users\thate\PycharmProjects\python_tools\파이썬의도구들\CH3_파이썬의도구들_라이브러리\3_2_문서관리와데이터처리\project2_docstranslator\output'

    # Read all docx files
    docx_data = read_docx_files(input_directory)

    translate_contents()


    # Write the translated content to new docx files
    write_docx_files(docx_data, output_directory)

if __name__ == "__main__":
    main()