#1 openpyxl 모듈을 불러옵니다.
import openpyxl

#2 엑셀에서 수료증 정보를 읽어오는 함수입니다.
def read_certification_list(file_path):

    #3 엑셀 파일을 불러옵니다.
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    #4 엑셀파일 안의 데이터를 저장할 리스트를 생성합니다.
    data = []

    #5 엑셀 파일의 각 행을 읽어서 리스트에 저장합니다.
    for row in sheet.iter_rows(min_row=3, values_only=True):
        number, class_name, name = row
        data.append([number, class_name, name])

    return data

