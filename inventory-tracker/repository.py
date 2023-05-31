import sqlite3
from model import Inventory

db_connection = sqlite3.connect("inventories.db")
cursor = db_connection.cursor()


def create_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS inventories(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name text,
        category text,
        quantity integer,
        created_at text,
        updated_at text
    )""")

create_table()

def get_all_stocks():
    cursor.execute('select * from inventories')
    all_inventories = cursor.fetchall()
    inventories = []
    for inv in all_inventories:
        inventories.append(
            Inventory(inv[1], inv[2], inv[3], inv[4], inv[5], inv[0]))
    return inventories

def insert_stock(stock: Inventory):
    cursor.execute("SELECT * FROM inventories WHERE LOWER(name) = ?", (stock.name.lower(),))
    results = cursor.fetchall()
    if len(results):
        existing_stock = results[0]
        new_quantity = existing_stock[3] + stock.quantity
        id = existing_stock[0]
        with db_connection:
            cursor.execute("UPDATE inventories SET quantity=:quantity WHERE id=:id", {'id': id, 'quantity': new_quantity})
    else:
        with db_connection:
            cursor.execute(
                'INSERT INTO inventories(name, category, created_at, updated_at, quantity) VALUES (?, ?, ?, ?, ?)', 
                (stock.name, stock.category, stock.created_at, stock.updated_at, stock.quantity))

def reduce_stock_quantity(id: int, quantity: int):
    cursor.execute("SELECT * FROM inventories WHERE id=:id", {"id": id})
    stock = cursor.fetchone()
    if not stock:
        print("stock not valid")
        return
    else:
        new_stock_quantity = stock[3] - quantity
        if new_stock_quantity < 0:
            print("Insuffiecient stock")
            return
        else:
            with db_connection:
                cursor.execute("UPDATE inventories SET quantity=:quantity WHERE id=:id", {'id': id, 'quantity': new_stock_quantity})

def increase_stock_quantity(id: int, quantity: str):
    cursor.execute("SELECT * FROM inventories WHERE id=:id", {'id': id})
    stock = cursor.fetchone()
    if not stock:
        print("Stock not valid")
        return
    else:
        new_stock_quantity = stock[3] + quantity
        with db_connection:
                cursor.execute("UPDATE inventories SET quantity=:quantity WHERE id=:id", {'id': id, 'quantity': new_stock_quantity})

def delete_stock(id):
    with db_connection:
        cursor.execute("DELETE from inventories WHERE id=:id", {'id': id})