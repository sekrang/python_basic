#chapter05-1
# 파이썬 함수 및 중요성
# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법
# def functuin_name(parameter):
#    code

#ex-1
def first_function(w):
    print("Hello,", w)

word = "Goodboy"
first_function(word)
print()

#ex-2
def return_function(w):
    value = "Hello, " + str(w)
    return value

x = return_function('Goodboy2')
print(x)
print()

#ex-3(다중반환)
def function_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3

x, y, z = function_mul(10)
print(x, y, z)
print()

#ex-5 튜플 리턴
def function_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3

q = function_mul2(20)
print(type(q), q)

print(type(q), q, list(q))

#ex-6 리스트 리턴
def function_mul3(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3

p = function_mul3(30)
print(type(p), p, set(p))

#ex-7 딕셔너리 리턴
def function_mul4(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'v1': y1, 'v2': y2, 'v3': y3}

d = function_mul4(30)
print(type(d), d, d.get('v2'), d.items(), d.keys())

# 중요
# *args, **kwargs

#ex-8 *args(언팩킹)
def args_function(*args):
    for i, v in enumerate(args):
        print('Resilt : {}'.format(i), v)
    print('-----')

args_function('Lee')
args_function('Lee', 'Park')
args_function('Lee', 'Park', 'Kim')

# **kwargs(언팩킹)
def kwargs_function(**kwargs):
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print('-----')

kwargs_function(name1='Lee')
kwargs_function(name1='Lee', name2='Park')
kwargs_function(name1='Lee', name2='Park', name3='Cho')

# 전체 혼합
def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)

example(10, 20, 'Lee', 'Kim', 'Park','Cho', age1=20, age2=30, age3=40)
print()

# 중첩 함수
def nested_fuction(num):
    def function_in_function(num):
        print(num)
    print("In function")
    function_in_function(num + 100)

nested_fuction(100)
# function_in_function(1000) - not difine
print()

# 람다식 예제
# 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행 되는 함수(Heap 초기화) -> 메모리 초기화
# 너무 남발시 가독성 오히려 감소
#def mul_function(x, y):
#    return x * y

#lambda x, y: x * y

# 일반적함수 -> 변수
def mul_function(x, y):
    return x * y

print(mul_function(10, 50))

# 람다 함수  -> 할당
lambda_mul_function = lambda x,y:x*y
print(lambda_mul_function(50, 50))

def function_final(x, y, function):
    print('>>>>', x * y * function(100, 100))

function_final(10, 20, lambda x,y:x * y)