# chapter06-2-2
# 모듈 사용 실습
import sys

print(sys.path)
print(type(sys.path))

sys.path.append('c:/PYTHON_BASIC')
print(sys.path)
import chapter06_02

print(chapter06_02.power(10, 3))

print(chapter06_02.add(5, 3))