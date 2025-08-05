#개발자 클래스를 정의
class Developer:
    def __init__(self, name, language):
        self.name = name
        self.language = language
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)    
    def __str__(self):
        return f"Developer(name={self.name}, language={self.language}, projects={self.projects})"



#개발자 클래스의 인스턴스를 2개 생성    
dev1 = Developer("Alice", "Python")
dev2 = Developer("Bob", "Java")     

#프로젝트를 추가
dev1.add_project("Project A")
dev1.add_project("Project B")
dev2.add_project("Project C")

#개발자 정보 출력
print(dev1)
print(dev2)     
import random