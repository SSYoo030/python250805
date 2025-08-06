#db1.py
import sqlite3

#연결 객체를 리턴
con = sqlite3.connect(r'c:\work\sample.db')  # 메모리 내 데이터베이스 사용    
#커서 객체를 리턴
cur = con.cursor()
#테이블 생성
cur.execute("create table phonebook(name text, phone text);")
#데이터 삽입
cur.execute("insert into phonebook values('홍길동', '010-1234-5678');")
#입력 parameter 처리
name = '박길동'
phone = '010-2345-6789'
cur.execute("insert into phonebook values(?, ?);", (name, phone))

#여러건 입력
datalist = (('김길동','010-2345-6789'), ('이길동','010-3456-7890'))
cur.executemany("insert into phonebook values(?, ?);", datalist)


#데이터 조회
cur.execute("select * from phonebook;")
for row in cur:
    print(row)  # ('홍길동', '010-1234-5678')

#작업을 정상적 종료
con.commit()
