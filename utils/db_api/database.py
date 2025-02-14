import sqlite3

connect = sqlite3.connect("tilla_somsa.db")
cursor = connect.cursor()


def create_database():
    cursor.execute('CREATE TABLE IF NOT EXISTS users_data(user_id TEXT,phone TEXT NULL,time TEXT)')
    cursor.execute("CREATE TABLE IF NOT EXISTS products(id INTEGER PRIMARY KEY AUTOINCREMENT,product_name TEXT,price INTEGER,image TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS busket_new(user_id TEXT,product_id INTEGER,count_product INTEGER,status TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS history_new(user_id TEXT,product_id INTEGER,count INTEGER)")

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


async def update_busket1(user_id, product_id, count_product=1, status='disabled'):
    b = cursor.execute('SELECT count_product FROM busket_new WHERE user_id=? AND product_id=?', (user_id, product_id))
    result = b.fetchone()  # Natijani saqlab qo'yamiz

    if result and result[0] > 0:  # Natijani to'g'ri tekshirish
        yangi_count = result[0] - 1  # Oldingi qiymatga 1 qo'shamiz
        cursor.execute('UPDATE busket_new SET count_product=? WHERE user_id=? AND product_id=?', (yangi_count, user_id, product_id))
        connect.commit()
        return yangi_count
    else:
        cursor.execute("INSERT INTO busket_new(user_id, product_id, count_product, status) VALUES(?,?,?,?)", (user_id, product_id, count_product, status))
        connect.commit()
        return yangi_count




async def first_register(user_id,time):
    cursor.execute("INSERT INTO users_data(user_id,time)",(user_id,time))
    connect.commit()



async def add_number(user_id,phone):
    cursor.execute(f"UPDATE users_data SET phone={phone} WHERE user_id={user_id}")
    connect.commit()

async def search_somsa(somsa_nomi):
    cursor.execute("SELECT * FROM products WHERE product_name=?",(somsa_nomi,))
    return cursor.fetchone()



async def update_product_status(user_id,product_id,status='enabled'):
    try: 
        cursor.execute("UPDATE busket_new SET status=? WHERE user_id=? AND product_id=?", (status, user_id, product_id))
        connect.commit()
        return True
    except:
        return False
async def savat_choiser(user_id,status='enabled'):
    cursor.execute("SELECT * FROM busket_new WHERE user_id=? AND status=?", (user_id, status))
    return cursor.fetchall()


async def somsa_nomi_qidir(id):
    cursor.execute("SELECT product_name,price FROM products WHERE id=?", (id,))
    return cursor.fetchone()

async def buyurtma_tarixi_tozalash(id,status='enabled'):
    cursor.execute("DELETE FROM busket_new WHERE user_id=? AND status=?", (id,status))
    connect.commit()
    return 'Tozalandi'

async def savat_tozalish(user_id, product_id):
    cursor.execute("DELETE FROM busket_new WHERE user_id=? AND product_id=?", (user_id, product_id))
    return cursor.fetchone()



# cursor.execute("DELETE FROM busket_new WHERE status=?",('disabled',))
# connect.commit()