class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}")

    def __str__(self):
        return f"Person(id={self.id}, name='{self.name}')"

class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}, Title: {self.title}")

    def __str__(self):
        return f"Manager(id={self.id}, name='{self.name}', title='{self.title}')"

class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}, Skill: {self.skill}")

    def __str__(self):
        return f"Employee(id={self.id}, name='{self.name}', skill='{self.skill}')"

# 테스트 코드
def test_classes():
    print("1. Person 객체 생성 및 출력")
    p = Person(1, "홍길동")
    print(p)           # 인스턴스 출력
    p.printInfo()

    print("2. Manager 객체 생성 및 출력")
    m = Manager(2, "이순신", "팀장")
    print(m)           # 인스턴스 출력
    m.printInfo()

    print("3. Employee 객체 생성 및 출력")
    e = Employee(3, "유관순", "Python")
    print(e)           # 인스턴스 출력
    e.printInfo()

    print("4. Manager의 title 확인")
    print(m.title)     # 바로 출력
    assert m.title == "팀장"

    print("5. Employee의 skill 확인")
    print(e.skill)     # 바로 출력
    assert e.skill == "Python"

    print("6. Person의 id 확인")
    print(p.id)        # 바로 출력
    assert p.id == 1

    print("7. Person의 name 확인")
    print(p.name)      # 바로 출력
    assert p.name == "홍길동"

    print("8. Manager의 상속 확인")
    print(isinstance(m, Person))  # 바로 출력
    assert isinstance(m, Person)

    print("9. Employee의 상속 확인")
    print(isinstance(e, Person))  # 바로 출력
    assert isinstance(e, Person)

    print("10. Manager와 Employee printInfo 다형성 확인")
    people = [p, m, e]
    for person in people:
        print(person)             # 인스턴스 출력
        person.printInfo()

if __name__ == "__main__":
    test_classes()