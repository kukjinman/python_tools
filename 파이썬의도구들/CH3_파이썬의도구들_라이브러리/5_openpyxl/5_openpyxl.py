import openpyxl

file_path = '파이썬수료증리스트.xlsx'

# 엑셀 파일 열기
workbook = openpyxl.load_workbook(file_path)

# 첫 번째 시트 선택
sheet = workbook.active

# 각 행을 출력
for row in sheet.iter_rows(values_only=True):
    print(row)