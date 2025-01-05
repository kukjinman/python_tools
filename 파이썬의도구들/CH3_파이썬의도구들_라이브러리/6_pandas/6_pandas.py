import pandas as pd

# 엑셀 파일 경로
file_path = '학생리스트.xlsx'

# 엑셀 파일 읽기
# df = pd.read_excel(file_path, header=1)
df = pd.read (file_path, con='sqlite:///example.db')
print(df)
# 각 행을 출력
for index, row in df.iterrows():
    print(f"{index}번째")
    print(f"학생이름: {row['학생이름']}, 학년: {row['학년']}, 반: {row['반']}")


