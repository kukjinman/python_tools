import openpyxl

#1 read_certification_list 함수
def read_certification_list_v2(file_path):

    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    data = []

    for row in sheet.iter_rows(min_row=3, values_only=True):
        number, class_name, name, email = row
        data.append([number, class_name, name, email])

    return data

