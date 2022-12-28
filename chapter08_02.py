#chapter08-2
#파이썬 외장(External) 함수
# 실제 프로그램 개발 중 자주 사용
# 종류 : sys, pickle, shutil, temfile, time, random 등

#ex-1
import sys
print(sys.argv)

#ex-2 (강제 종료)
# sys.exit()

#ex-3 (파이썬 패키지 위치)
print(sys.path)

# *pickle : 객체 파일 읽기, 쓰기
import pickle 

#ex-4 (쓰기)
f = open("test.obj", 'wb')
obj = {1: 'python', 2:'study', 3:'basic'}
pickle.dump(obj, f)
f.close
#ex-5 (읽기)
f = open('test.obj', 'rb')
data = pickle.load(f)
print(data, type(data))
f.close()

# *os : 환경 변수, 디렉토리(파일) 처리 관련, 운영체제 작업 관련
# mkdir, rmdir(비어 있으면 삭제), rename

#ex-6
import os
print(os.environ)
print(os.environ["USERNAME"])
print(os.environ["TERM_PROGRAM"])

#ex-7 (현재 경로)
print(os.getcwd())

# *time : 시간 관련 처리
import time

#ex-8
print(time.time())

#ex-9 (형태 변환)
print(time.localtime(time.time()))

#ex-10 (간단 표현)
print(time.ctime())

#ex-11 (형식 표현)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

#ex-12 (시간 간격 발생)
# for i in range(5):
#     print(i)
#     time.sleep(1)

# random : 난수 리턴
import random

#ex-13
print(random.random()) # 0 ~ 1 실수

#ex-14
print(random.randint(1, 45))
print(random.randrange(1, 45))

#ex-15 (섞기)
d = [1, 2, 3, 4, 5]
random.shuffle(d)
print(d)

#ex-16 (무작위 선택)
c = random.choice(d)
print(c)

#webbrowser : 본인 os의 웹 브라우저 실행
import webbrowser
webbrowser.open("http://google.com")
webbrowser.open_new("http://google.com")