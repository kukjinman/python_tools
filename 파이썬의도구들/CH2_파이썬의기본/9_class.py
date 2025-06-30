# 클래스 기본 구조
class MyClass:
    # 클래스 변수
    class_var = 0

    # 생성자
    def __init__(self, instance_var):
        # 인스턴스 변수
        self.instance_var = instance_var
        MyClass.class_var = MyClass.class_var + instance_var

    # 클래스 함수
    def var_printer(self):
        print(f"클래스 변수: {MyClass.class_var}, 인스턴스 변수: {self.instance_var}")

# 클래스 사용 예
Class_A = MyClass(10)
Class_A.var_printer()
Class_B = MyClass(5)
Class_B.var_printer()




# 자동차 객체를 생성합니다.
car1 = {
    "brand": "현대",
    "model": "아반떼",
    "year": 2020
}

car2 = {
    "brand": "기아",
    "model": "스포티지",
    "year": 2021
}

# 자동차 정보를 출력하는 함수
def display_info(car):
    print(f"{car['year']} {car['brand']} {car['model']}")

# 자동차 정보 출력
display_info(car1)
display_info(car2)


# =========================================================
# 클래스를 사용한 예제

# 자동차 클래스를 정의합니다.
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")

# 자동차 객체를 생성합니다.
car1 = Car("현대", "아반떼", 2020)
car2 = Car("기아", "스포티지", 2021)

# 자동차 정보 출력
car1.display_info()
car2.display_info()

