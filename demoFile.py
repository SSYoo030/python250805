#demoFile.py

#파일쓰기
f= open("c:\\work\\test.txt", "wt",encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close()   

#파일읽기(raw string notation)
f= open(r"c:\work\test.txt", "rt",encoding="utf-8") # \두번쓰기 귀찮을때 사용하는 법
print(f.read())
f.close()   

