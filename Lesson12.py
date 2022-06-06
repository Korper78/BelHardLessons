import sqlite3
from collections import namedtuple


Category = namedtuple('Category', ['Name', 'Parent', 'Descr'])
categories = Category(
    ['Cat1', 'Cat2'],
    [1, 2],
    ['Category one', 'Category two']
)

Product = namedtuple('Product', ['Name', 'Descr', 'Category'])
products = Product(
    ['Prod1', 'Prod2', 'Prod3', 'Prod4'],
    ['Product one', 'Product two', 'Product three', 'Product four'],
    [1, 2, 1, 2]
)

# print(*categories)
# print(*products)

sql_db = sqlite3.connect('currency.db')
sql_db.execute("create table if not exists category (id integer primary key autoincrement, name text unique, parent int, descr text);")
sql_db.execute("create table if not exists product (id integer primary key autoincrement, name text, descr text, category int not null);")
sql_db.commit()
db_cur = sql_db.cursor()
for indx in range(2):
    db_cur.execute("insert into category (name, parent, descr) values(?,?,?);", (categories.Name[indx], categories.Parent[indx], categories.Descr[indx]))
    sql_db.commit()
db_cur.execute("select * from category where id=?;", (1,))
print(db_cur.fetchall())
db_cur.execute("select * from category where name=?;", ('Cat2',))
print(db_cur.fetchall())
for indx in range(4):
    db_cur.execute("insert into product (name, descr, category) values(?,?,?);", (products.Name[indx], products.Descr[indx], products.Category[indx]))
    sql_db.commit()
db_cur.execute("select * from product where id=?;", (3,))
print(db_cur.fetchall())
db_cur.execute("select * from product where category=?;", (1,))
print(db_cur.fetchall())

sql_db.commit()
sql_db.close()
