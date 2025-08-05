#부모 클래스
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))

#자식 클래스
class Student(Person):
    #덮어쓰기(Overriding)
    def __init__(self, name, phoneNumber, subject, studentID):
        #부모 클래스의 초기화 메서드 호출      
        super().__init__(name, phoneNumber)
        #자식 클래스의 속성 추가
        self.subject = subject
        self.studentID = studentID
    #덮어쓰기(Overriding)
        def printInfo(self):
            print("Info(Name:{0}, Phone Number: {1}, Subject: {2}, Student ID: {3})".format(self.name, self.phoneNumber, self.subject, self.studentID))
   
p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")
print(p.__dict__)
print(s.__dict__) #그냥 dic값임

p.printInfo()
s.printInfo()   # 부모 클래스의 메서드를 호출
s.subject = "컴퓨터공학"    # 자식 클래스의 속성 추가
s.studentID = "20220001"   # 자식 클래스의 속성 추가                
