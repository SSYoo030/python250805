import sqlite3
import random

class ElectronicsDB:
    def __init__(self, db_name="electronics.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        self.conn.commit()

    def insert_product(self, product_id, name, price):
        self.cursor.execute('''
            INSERT INTO products (id, name, price) VALUES (?, ?, ?)
        ''', (product_id, name, price))
        self.conn.commit()

    def update_product(self, product_id, name=None, price=None):
        if name:
            self.cursor.execute('''
                UPDATE products SET name = ? WHERE id = ?
            ''', (name, product_id))
        if price:
            self.cursor.execute('''
                UPDATE products SET price = ? WHERE id = ?
            ''', (price, product_id))
        self.conn.commit()

    def delete_product(self, product_id):
        self.cursor.execute('''
            DELETE FROM products WHERE id = ?
        ''', (product_id,))
        self.conn.commit()

    def select_products(self):
        self.cursor.execute('SELECT * FROM products')
        rows = self.cursor.fetchall()
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Price: {row[2]}")

    def close(self):
        self.conn.close()


# 샘플 데이터 100개 삽입
if __name__ == "__main__":
    db = ElectronicsDB()

    # 샘플 제품명 리스트
    product_names = ["Smartphone", "Laptop", "Tablet", "Smartwatch", "TV", "Refrigerator", "Microwave", "Headphones", "Camera", "Speaker"]

    # 제품 ID 1~100, 랜덤 제품명과 가격 생성 후 삽입
    for product_id in range(1, 101):
        name = random.choice(product_names) + f" {product_id}"
        price = round(random.uniform(50.0, 2000.0), 2)
        db.insert_product(product_id, name, price)

    print("=== 전체 제품 목록 ===")
    db.select_products()

    print("\n=== ID 10번 제품명 업데이트 ===")
    db.update_product(10, name="Updated Laptop 10")
    db.select_products()

    print("\n=== ID 20번 제품 삭제 ===")
    db.delete_product(20)
    db.select_products()

    db.close()
