#chapter05-2
# 파이썬 사용자 입력
# Input 사용법
# 기본 타임 (str)

#ex-1
"""
name = input("Enter Your Name : ")
grade = input("Enter Your Grade : ")
company = input("Enter Your Company name : ")

print(name, grade, company)
print()
"""
#ex-2
"""
number = input("Enter number : ")
name = input("Enter name : ")

print("type of number", type(number), number * 3)
print("type of name", type(number))
"""
#ex-3
"""
first_number = int(input("Enter number1 : "))
second_number = int(input("Enter number2 : "))

total = first_number + second_number
print("first_number + second_number : ", total)
"""
#ex-4
"""
float_number = float(input("Enter a float number : "))
print("input float : ", float_number)
print("input type : ", type(float_number))
"""

#ex-5
print("FirstName - {0}, LastName - {1}".format(input("Enter first name : "), input("Enter second name : ")))
