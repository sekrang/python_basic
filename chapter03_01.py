#chapter03-1
#숫자형

#파이썬 지원 자료형
"""
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전
"""

#데이터 타입

str1 = "python"
bool = True
str2 = "anaconda"
float_v = 10.0
int_v = 7
list = [str1, str2]
dict = {
    "name": "Machine Learning",
    "version": 2.0
}
tuple = (7, 8 ,9)
set = {7, 8, 9}

print(type(str1))
print(type(bool))
print(type(str2))
print(type(float_v))
print(type(int_v))
print(type(dict))
print(type(tuple))
print(type(set))

#숫자형 연산자
"""
+ : 합
- : 차
* : 곱
/ : 나누기
// : 몫
% : 나머지
abs(x) : 절댓값
pow(x, y) x **y -> 2 ** 3
"""

#정수 선언 
i = 77
i2 = -14
big_int = 77777777777777777777777799999999999999

print(i)
print(i2)
print(big_int)
print()

# 실수 출력
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9

print(f)
print(f2)
print(f3)
print(f4)
print()

# 연산 실습
i1 = 39
i2 = 939
big_int1 = 7777777777777777797240723904723074023
big_int2 = 291432131231242131242
f1 = 1.234
f2 = 3.999

#+
print(">>>>>+")
print("i1 + i2 : ", i1 + i2)
print("f1 + f2 : " ,f1 + f2)
print("big_int1 + big_int2 : ", big_int1 + big_int2)

#*
print(">>>>>*")
print("i1 * i2 : ", i1 * i2)
print("f1 * f2 : ", f1 * f2)
print("big_int1 * big_int2 : ", big_int1 * big_int2)

#형 변환
a = 3.
b = 6
c = .7
d = 12.7
print(type(a), type(b), type(c), type(d))
print()

# 형 변환
print(float(b))
print(int(c))
print(int(d))
print(int(True))
print(float(False))
print(complex(3))
print(complex('3'))
print(complex(False))
print()

# 수치 연산 함수
print(abs(-7))
x, y = divmod(100, 8)
#x = 몫, y = 나머지
print(x,y)
print(pow(5,3), 5 ** 3)
print()

# 외부 모듈
import math

print(math.ceil(5.1)) # 변수 이상의 수 중에서 가장 작은 정수
print(math.pi)
