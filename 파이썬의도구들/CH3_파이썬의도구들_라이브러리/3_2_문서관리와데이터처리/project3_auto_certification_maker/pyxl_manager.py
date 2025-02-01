# openpyxl 모듈을 불러옵니다.
import openpyxl

# read_certification_list 함수를 정의합니다.
def read_certification_list(file_path):
    # Load the workbook and select the active sheet
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    # Initialize an empty list to store the data
    data = []

    # Iterate over the rows in the sheet, starting from the second row
    for row in sheet.iter_rows(min_row=3, values_only=True):
        number, class_name, name = row
        data.append([number, class_name, name])

    return data

