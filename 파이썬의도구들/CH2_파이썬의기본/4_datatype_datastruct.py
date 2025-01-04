# <데이터를 바로 사용하는 예>
print(10)
# <데이터를 변수에 저장하고 사용하는 예>
a = 20
print(a)
print(type(a))


# 정수
var_int = 10
print(var_int)
print(type(var_int))

#실수
var_float = 10.5
print(var_float)
print(type(var_float))

#문자열
var_string = "문자열입니다."
print(var_string)
print(type(var_string))

#불리언
var_bool = True
print(var_bool)
print(type(var_bool))

# 데이터 타입을 잘 못 사용하는 예
var_int1 = 10
var_int2 = 20
var_str1 = "test"
var_str2 = "code"

print(var_int1 + var_int2)
print(var_str1 + var_str2)

# print(var_int1 + var_str1)


#리스트
var_list = [1,2,3]
print(var_list)
print(type(var_list))

var_list2 = [1,2,3,'a',[1,2,'b']]
print(var_list2)
print(type(var_list2))

#튜플
var_tuple = (37.5665, 126.9780)
print(var_tuple)
print(type(var_tuple))
# var_tuple[0] = 1

#딕셔너리
var_dict={'철수':90,'영희':85,'민수':95}
print(var_dict)
print(type(var_dict))

#세트
var_set = {1, 2, 2, 3, 3, 4, 4}
print(var_set)