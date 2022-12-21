#chapter04-3
#파이썬 제어문
# while 문 실습

# while (expression):
#    <statement(s)>

#ex-1
n = 5
while n > 0:
    print(n)
    n = n-1

#ex-2
a = ['foo', 'bar', 'baz']
while a:
    print(a.pop())

#ex-3
#break, continue
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop Ended.')

#ex-4
m = 5
while m > 0:
    m -= 1
    if m == 2:
        continue
    print(m)
print('Loop Ended.')

#ex-5
#if 중첩
i = 1
while i <= 10:
    print('i:', i)
    if i ==6:
        break
    i += 1

# while - else 구문
#ex-6
n = 10
while n > 0:
    n -=1
    print(n)
    if n == 5:
        break
else:
    print('else out.') # 마지막까지 올경우 1번 실행돰

#ex-7
a = ['foo', 'bar', 'baz', 'qux']
s = 'qux'

i = 0

while i < len(a):
    if a[i] == s:
        break
    i += 1
else:
    print(s, 'is not found in list.') 

# 무한 반복
#while True:
#    print('5')

#ex-8
a = ['foo', 'bar', 'baz']

while True:
    if not a:
        break
    print(a.pop())
