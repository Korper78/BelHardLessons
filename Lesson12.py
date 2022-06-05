import sqlite3
from collections import namedtuple


Category = namedtuple('Category', ['ID', 'Name', 'Parent', 'Descr'])
categories = Category(
    [1, 2],
    ['Cat1', 'Cat2'],
    [1, 2],
    ['Category one', 'Category two']
)

Product = namedtuple('Product', ['ID', 'Name', 'Descr', 'Category'])
products = Product(
    [1, 2, 3, 4],
    ['Prod1', 'Prod2', 'Prod3', 'Prod4'],
    ['Product one', 'Product two', 'Product three', 'Product four'],
    [1, 2, 1, 2]
)

# print(*categories)
# print(*products)

sql_db = sqlite3.connect('currency.db')
sql_db.execute("create table if not exists category (id int primary key, name text unique, parent int, descr text)")
sql_db.execute("create table if not exists product (id int primary key, name text, descr text, category int not null)")
db_cur = sql_db.cursor()
for indx in range(2):
    db_cur.execute("replace into category (id, name, parent, descr) values(?,?,?,?)", (categories.ID[indx], categories.Name[indx], categories.Parent[indx], categories.Descr[indx]))
for indx in range(4):
    db_cur.execute("replace into product (id, name, descr, category) values(?,?,?,?)", (products.ID[indx], products.Name[indx], products.Descr[indx], products.Category[indx]))
sql_db.commit()
sql_db.close()
