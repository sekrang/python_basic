#chapter09-1
#파일 읽기 및 쓰기

# 읽기 모드 : r, 쓰기모드 w, 추가모드 a, 텍스트 모드 t, 바이너리 모드 b
# 상대경로('../, ./'), 절대 경로('C:\django\example..')

# 파일 읽기(Read)
#ex-1
f = open('C:\\python_basic\\resource\\it_news.txt', 'rt', encoding='UTF-8') # == ./resource/it_news.tst
# 속성 확인
print(dir(f))
# 인코딩 확인
print(f.encoding)
# 파일 이름
print(f.name)
# 모드 확인
print(f.mode)
cts = f.read()
print(cts)
# 반드시 close
f.close()

#ex-2 
with open('C:\\python_basic\\resource\\it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read()
    print(c)
    print(iter(c))
    print(list(c))

print()

#ex-3
# reda() : 전체 읽기, read(10) :10Byte
with open('C:\\python_basic\\resource\\it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read(20)
    print(c)
    c = f.read(20)
    print(c)
    c = f.read(20)
    print(c)
    f.seek(0,0)
    c = f.read(20)
    print(c)

print()

#ex-4
# readline : 한줄씩 읽기
with open('C:\\python_basic\\resource\\it_news.txt', 'r', encoding='UTF-8') as f:
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)

#ex-5
# readline : 전체를 읽은 후 라인 단위 리스트로 저장 
with open('C:\\python_basic\\resource\\it_news.txt', 'r', encoding='UTF-8') as f:
    cts = f.readlines()
    print(cts)
    print()
    for c in cts:
        print(c, end='')
    
print()

# 파일 쓰기(write)

#ex-1
with open('./resource/contents1.txt', 'w') as f:
    f.write('I love python\n')

#ex-2
with open('./resource/contents1.txt', 'at') as f:
    f.write('I love python2\n')

#ex-3
#writelines : 리스트 -> 파일
with open('./resource/contents2.txt', 'w') as f:
    list = ['Orange\n', 'Apple\n', 'Banana\n', 'Melon\n']
    f.writelines(list)

#ex-4
with open('./resource/contents3.txt', 'w') as f:
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)