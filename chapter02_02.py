#chapter02-2
#파이썬 변수

# 기본 선언
n = 700
print( n * 700)
print(type(n))
print()

#동시 선언
x = y = z = 700
print(x, y, z)

var = 75
var = "Change Value"

print(var)
print(type(var))
print()

# Object Refernces
#변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

#ex1)
print(300)
print(int(300))

#ex2)
#n -> 777
n = 777
print(n, type(n))
m = n
# m -> 777 <- n
print(m, n)
print(type(m), type(n))
m = 400
print(m, n)
print(type(m), type(n))
print()

# id(identity)확인 객체의 고유값 확인
m = 800
n = 655
print(id(m))
print(id(n))
print(id(m)==id(n))

# 같은 오브젝트 참조
m = 800
n = 800
print(id(m))
print(id(n))
print(id(m)==id(n))

# 다양한 변수 선언 
# Camel Case : numverOfCollegeGraduates -> Method
# Pascal Case : NumverOfCollegeGraduates -> class
# Snake Case : numver_of_college_graduates

# 허용하는 변수 선언 법(_, $) 
# 숫자 및 다양한 특수문자, 예약어(for, as, if, class...) 허용 x
# google에 python reserved word 검색하면 안되는 단어 나옴
age = 1
Age = 2 
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8