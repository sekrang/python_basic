#chapter06-1
#파이썬 클래스(Class)
#OOP( 객체 지향 프로그래밍 )ㅡ self, 인스턴스 메소드, 인스턴스 변수

#클래스 and 인스턴스 차이 이해
#네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
#클래스 변수 : 직접 접근 가능, 공유
#인스턴스 변수 : 객체마다 별도 존재

#ex-1
class Dog(object): #object 상속
    # 클래스 속성
    species = 'firstdog'
    #초기화 / 인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 클래스 정보
print(Dog)

# 인스턴스화
a = Dog("mikky", 2)
b = Dog("baby", 3)
c = Dog("loxy", 3)
d = Dog("lucy", 1)
a1 = Dog("mikky", 2)

# 비교
print(a == b, id(a), id(b), id(a1)) # 인스턴스화 한것은 모두 다름

# 네임스페이스
print('dog1', a.__dict__)
print('dog2', b.__dict__)

# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.species))

print(Dog.species)
print(a.species)
print(b.species)

#ex-2
#self의 이해
class SelfTest:
    def function1():
        print('Function1 called')
    def function2(self):
        print(id(self))
        print('Function2 called')

f = SelfTest()
print(id(f))
f.function2()
SelfTest.function1()
SelfTest.function2(f)

#ex-3
#클래스 변수, 인스턴스 변수
class Warehouse:
    #클래스 변수 = 0
    stock_num = 0 #재고
    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1
    
    def __del__(self):
        Warehouse.stock_num -= 1

user1 = Warehouse('Lee')
user2 = Warehouse('Cho')

print(Warehouse.stock_num)

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print('before', Warehouse.__dict__)
print(user1.stock_num)

del user1
print('after', Warehouse.__dict__)

#ex-4
class Dog(object): #object 상속
    # 클래스 속성
    species = 'firstdog'
    #초기화 / 인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return '{} is {} years old'.format(self.name, self.age)
    def speak(self, sound):
        return '{} says {}!'.format(self.name, sound)

# 인스턴스 생성
c = Dog('july', 4)
d = Dog('Marry', 10)
# 메소드 호출
print(c.info())
print(d.info())
print(c.speak('Wal Wal'))
print(d.speak('Mung Mung'))