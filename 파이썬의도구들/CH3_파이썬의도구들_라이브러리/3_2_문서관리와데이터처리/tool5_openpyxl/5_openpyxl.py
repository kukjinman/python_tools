import openpyxl

#1 엑셀 파일 열기
workbook = openpyxl.load_workbook('파이썬수료증리스트.xlsx')
#2 엑셀 활성화 시트 선택
sheet = workbook.active
#3 각 행을 출력
for row in sheet.iter_rows(values_only=True):
    print(row)