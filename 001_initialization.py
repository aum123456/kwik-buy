import psycopg2 as pg2
import time

print('\n\n')
print('>>>> Establishing connection...')
cxn = pg2.connect(
    dbname = "xvrkpedt",
    user = "xvrkpedt",
    password = "fvRfE3Cyv3RUX3fLhdkVJboWIu_2wSuk",
    host = "kiouni.db.elephantsql.com",
    port = "5432"
)
cur = cxn.cursor()
print('>>>> Connection successful!')
time.sleep(2)
print('>>>> Deleting old tables...')
cur.execute("DROP TABLE IF EXISTS orders;")
cur.execute("DROP TABLE IF EXISTS warehouse;")
time.sleep(2)
print('>>>> Creating new tables...')
cur.execute("CREATE TABLE warehouse( product VARCHAR(50) PRIMARY KEY, category VARCHAR(50), units INT);")
cur.execute("CREATE TABLE orders( id SERIAL, name VARCHAR(50), email VARCHAR(50), gender VARCHAR(50), age VARCHAR(50), product VARCHAR(50), units INT, amount INT, FOREIGN KEY (product) REFERENCES warehouse(product));")
cur.execute("INSERT INTO warehouse VALUES ('Oil 1 lit', 'Food Supplies', 20), ('Wheat 0.5 kg', 'Food Supplies', 20), ('Rice 0.5 kg', 'Food Supplies', 20), ('Maggie 1 pack', 'Food Supplies', 20), ('Milk 0.5 lit', 'Food Supplies', 20), ('Bandaid 10 strips', 'Medical Supplies', 20), ('Betadine 50 ml', 'Medical Supplies', 20), ('Cyclopalm 1 strip', 'Medical Supplies', 20), ('Paracetamol 1 strip', 'Medical Supplies', 20), ('Dettol 100 ml', 'Medical Supplies', 20), ('Pen 1 unit', 'Office Supplies', 20), ('Permanent Marker 1 unit', 'Office Supplies', 20), ('Record Book 1 book', 'Office Supplies', 20), ('Observation Book 1 book', 'Office Supplies', 20), ('Rough Book 1 book', 'Office Supplies', 20) ;")
cur.execute("COMMIT;")
time.sleep(2)
print('>>>> Database clean.')
time.sleep(2)

choice = input('Would you like to populate "orders" with sample entries? [yes/no]: ')

if choice == 'yes':
    cur.execute("INSERT INTO ORDERS(name, email, gender, age, product, units, amount) VALUES ('Rakshit R', 'rakshit@gmail.com', 'Male', '18-30', 'Record Book 1 book', '1', '10');")
    cur.execute("UPDATE warehouse SET units = units - 1 WHERE product='Record Book 1 book';")
    cur.execute("INSERT INTO ORDERS(name, email, gender, age, product, units, amount) VALUES ('Rakshit R', 'rakshit@gmail.com', 'Male', '18-30', 'Observation Book 1 book', '1', '10');")
    cur.execute("UPDATE warehouse SET units = units - 1 WHERE product='Observation Book 1 book';")
    cur.execute("INSERT INTO ORDERS(name, email, gender, age, product, units, amount) VALUES ('Prashant K', 'prashant@gmail.com', 'Male', '18-30', 'Maggie 1 pack', '2', '40');")
    cur.execute("UPDATE warehouse SET units = units - 2 WHERE product='Maggie 1 pack';")
    cur.execute("INSERT INTO ORDERS(name, email, gender, age, product, units, amount) VALUES ('Aum P', 'aum@gmail.com', 'Male', '18-30', 'Oil 1 lit', '3', '150');")
    cur.execute("UPDATE warehouse SET units = units - 3 WHERE product='Oil 1 lit';")
    cur.execute("INSERT INTO ORDERS(name, email, gender, age, product, units, amount) VALUES ('Palak K', 'palak@gmail.com', 'Female', '18-30', 'Rough Book 1 book', '2', '20');")
    cur.execute("UPDATE warehouse SET units = units - 2 WHERE product='Rough Book 1 book';")
    cur.execute("INSERT INTO ORDERS(name, email, gender, age, product, units, amount) VALUES ('Almas M', 'prof_almas@dsce.edu.in', 'Female', '30-50', 'Permanent Marker 1 unit', '2', '40');")
    cur.execute("UPDATE warehouse SET units = units - 2 WHERE product='Permanent Marker 1 unit';")
    cur.execute("INSERT INTO ORDERS(name, email, gender, age, product, units, amount) VALUES ('Ramesh Babu', 'hod_cse@dsce.edu.in', 'Male', '50+', 'Rice 0.5 kg', '2', '100');")
    cur.execute("UPDATE warehouse SET units = units - 2 WHERE product='Rice 0.5 kg';")
    cur.execute('COMMIT;')

time.sleep(2)
print('>>>> Closing the connection...')
cur.close()
cxn.close()
time.sleep(2)
print('>>>> Connection closed gracefully.')
time.sleep(2)
print('\n\n')