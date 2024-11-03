import pandas as pd

# 엑셀 파일 경로
file_path = '미술대회시상인원리스트.xlsx'  # 실제 파일 이름으로 변경하세요

# 엑셀 파일 읽기
df = pd.read_excel(file_path, header=1)
print(df)
# 각 행을 출력
for index, row in df.iterrows():
    print(f"{index}번째")
    print(f"학생이름: {row['학생이름']}, 상명: {row['상명']}, 학년: {row['학년']}, 반: {row['반']}")