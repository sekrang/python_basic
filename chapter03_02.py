#chapter03-2
# 파이썬 문자형

# 문자열 생성

str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4))

# 빈 문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

# 이스케이프 문자 사용 
# Escape 코드 
"""
\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
"""
# I'm Boy

print("I'm Boy")
print("I\'m Boy")

print('a \t b')
print('a \"\" b')

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)

# 탭, 줄 바꿈
t_s1 = "Click \t Start!"
t_s2 = "New :imme \n Cheak"

print(t_s1)
print(t_s2)
print()

# Raw String
raw_s1 = r'D:\python\test'
print(raw_s1)
print()