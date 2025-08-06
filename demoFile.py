#demoFile.py

#파일쓰기
f= open("c:\\work\\test.txt", "wt",encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close()   

#파일읽기(raw string notation)
f= open(r"c:\work\test.txt", "rt",encoding="utf-8") # \두번쓰기 귀찮을때 사용하는 법
print(f.read())
f.close()   

#문자열처리
strA = '파이썬은 강력해'
strB = 'python is very powerful'
print(len(strA))
print(len(strB))
print(strB.capitalize())
print(strB.upper())
print('MBC2508'.isalnum()) #영어,숫자만 구성
print('2580'.isdecimal) #숫자만 구성
data = '<<< spam and ham >>>'
print(data.strip()) #양쪽 공백제거
result = data.strip('<> ')  
print(data)
print(result) #양쪽 <>와 공백제거

result2 = result.replace('spam', 'spam eggs') #문자열 치환
print(result2)
#리스트로 리턴
lst = result2.split() #공백으로 분리
print(lst)
#하나의 문자열로 합치기
print(':)'.join(lst)) #리스트를 하나의 문자열로 합치기

#정규표현식
import re

result = re.search('[0-9]*th', '  35th')
print(result)
print(result.group()) #검색된 문자열 출력

# result = re.match('[0-9]*th', '  35th')
# print(result)
# print(result.group()) #검색된 문자열 출력

result = re.search('apple', 'this is an apple')
print(result.group())

result = re.search(r'\d{3}-\d{4}-\d{4}', '전화번호는 010-1234-5678입니다.')
print(result.group())  # '010-1234-5678'