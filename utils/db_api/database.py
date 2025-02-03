import sqlite3

connect = sqlite3.connect("tilla_somsa.db")
cursor = connect.cursor()


def create_database():
    cursor.execute('CREATE TABLE IF NOT EXISTS users_data(user_id TEXT,phone TEXT NULL,time TEXT)')
    cursor.execute("CREATE TABLE IF NOT EXISTS products(id INTEGER PRIMARY KEY AUTOINCREMENT,product_name TEXT,price INTEGER,image TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS busket_new(user_id TEXT,product_id INTEGER,count_product INTEGER,status TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS history(user_id TEXT,product_id INTEGER)")
    print("Ishladi")

create_database()

async def update_busket(user_id, product_id, count_product=1, status='disabled'):
    a = cursor.execute('SELECT count_product FROM busket_new WHERE user_id=? AND product_id=?', (user_id, product_id))
    result = a.fetchone()  # Natijani saqlab qo'yamiz

    if result:  # Agar natija mavjud bo'lsa
        new_count = result[0] + 1  # Oldingi qiymatga 1 qo'shamiz
        cursor.execute('UPDATE busket_new SET count_product=? WHERE user_id=? AND product_id=?', (new_count, user_id, product_id))
        connect.commit()
        return new_count
    else:
        cursor.execute("INSERT INTO busket_new(user_id, product_id, count_product, status) VALUES(?,?,?,?)", (user_id, product_id, count_product, status))
        connect.commit()
        return 1



async def first_register(user_id,time):
    cursor.execute("INSERT INTO users_data(user_id,time)",(user_id,time))
    connect.commit()



async def add_number(user_id,phone):
    cursor.execute(f"UPDATE users_data SET phone={phone} WHERE user_id={user_id}")
    connect.commit()

async def search_somsa(somsa_nomi):
    cursor.execute("SELECT * FROM products WHERE product_name=?",(somsa_nomi,))
    return cursor.fetchone()



# cursor.execute("INSERT INTO products(product_name,price,image) VALUES(?,?,?)" ,("QOY GO'SHTI",10000,"qoy_gosht.jpg"))
# cursor.execute('INSERT INTO products(product_name,price,image) VALUES (?,?,?)',("MOL GOSHTLI KATTA", 9000, "mol_gosh.jpg"))
# cursor.execute('INSERT INTO products(product_name,price,image) VALUES (?,?,?)',("MOL GO'SHTLI KICHIK",7000,"mol_gosht.jpg"))
# cursor.execute('INSERT INTO products(product_name,price,image) VALUES (?,?,?)',("TOVUQ SIRLI",7000,"tovuq_sir.jpg"))
# cursor.execute("INSERT INTO products(product_name,price,image) VALUES(?,?,?)" ,("AVASHNOY",7000,"tandir.jpg"))
# cursor.execute("INSERT INTO products(product_name,price,image) VALUES(?,?,?)" ,("KARTOSHKALI",5000,"kartoshka.jpg"))
# cursor.execute("INSERT INTO products(product_name,price,image) VALUES(?,?,?)" ,("KO'KATLI",5000,"kokatli.jpg"))
# cursor.execute("INSERT INTO products(product_name,price,image) VALUES(?,?,?)" ,("QOVOQLI",5000,"qovoq.jpg"))

# connect.commit()
