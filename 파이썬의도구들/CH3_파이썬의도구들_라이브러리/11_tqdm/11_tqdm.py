#1 준비단계
from tqdm import tqdm
import time

#2 200개의 아이템을 가진 리스트 생성
total_number = 200
items = []
for index in range(total_number):
    items.append(f"Item {index}")

#3 tqdm을 사용하여 리스트의 아이템을 출력
with tqdm(total=total_number, desc="Processing item count") as pbar:
    for item in items:
        # print(item)  # 아이템 출력
        time.sleep(0.05)  # 하나의 item이 처리되는 것을 시각적으로 보기 위한 delay
        pbar.update(1)