#demoFunction.py

#1) 함수를 정의
def setValue(newValue):
    #지역변수 _ 안에 있는 변수
    x = newValue
    print('함수 내부:', x)
    #return x

#2) 함수를 호출
reValue = setValue(5) #이건 전역변수(밖에 있는 변수)임 -> def setValue에서 return x 를 하지 않으면 None이 나옴
print(reValue)

#1) 함수를 정의
def swap(x,y):
    return y, x

#호출
result = swap(3,4)
print(result)


print('---함수 이름 해석---')
x=5
def func(a) :
    return a+x
#호출
print(func(1))

def func2(a) :
    x = 10
    return a+x
#호출
print(func2(1))

print('---기본값---')
def times(a=10, b=20) :
    return a*b
#호출
print(times())
print(times((5)))
print(times(5,6))

#키워드인자
def connectURI(server, port):
    strURL = 'https://' + server + ':' + port
    return strURL
#호출
print(connectURI('multi.com', '80'))
print(connectURI(port='80', server = 'test.com')) #순서 달라도 상관없음
