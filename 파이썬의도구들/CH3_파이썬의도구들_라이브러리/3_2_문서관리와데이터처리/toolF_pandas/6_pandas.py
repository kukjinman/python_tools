#1 pandas 라이브러리를 pd로 가져옵니다.
import pandas as pd

#2 엑셀 파일 열기
df = pd.read_excel('학생리스트.xlsx', header=1)

#3 df 결과 출력
print("df 결과")
print(type(df))
print(df)

print("-------------------------------")
#4 df.iterrows()의 각 행의 데이터 값을 출력
print("df.iterrows() 결과")
for index, row in df.iterrows():
    print(f"{index}번째")
    print(f"학생이름: {row['학생이름']}, 학년: {row['학년']}, 반: {row['반']}")

pd.read_j