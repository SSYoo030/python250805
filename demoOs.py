#demoOs.py

from os.path import * # * 의미: 모든걸 가져온다.
from os import * # * 의미: 모든걸 가져온다.
import glob # glob: 파일 경로를 다루는 모듈

fNmame = 'sample.txt' 
print(abspath(fNmame))  # 절대경로
print(basename(r'c:\work\text.txt'))  # 파일명

if (exists(r'c:\python310\python.exe')): 
    print(getsize(r'c:\python310\python.exe'))  # 파일 크기
else:
    print('파일이 존재하지 않습니다.')

print('운영체제명:', name)
print('환경변수:', environ)
system('notepad.exe')  # 메모장 실행

print(glob.glob('*.py'))  # 현재 디렉토리의 모든 파이썬 파일 목록
for item in glob.glob('*.py'): 
    print(item)  # 각 파이썬 파일 이름 출력

    
