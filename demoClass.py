# demoClass.py
# 1) 클래스 정의

class Person:
    #초기화 매서드
    def __init__(self):
        self.name = 'default name'
    def print(self):
        #print('My name is {0}'.format(self.name))
        print(f'My name is {self.name}') #변수 명을 바로 선언

# 2) 인스턴스 생성
p1 = Person() # __init__을 부름
p2 = Person()
p1.name = '전우치'

# 3) 매서드 호출
p1.print()
p2.print()


