import streamlit as st
import psycopg2 as pg2


st.title('KWIK-BUY')
st.header('User Details')

u_name = st.text_input('Name: ')
u_email = st.text_input('Email: ')
u_gender = st.radio(
    label = 'Gender: ',
    options = ['Male', 'Female']
)
u_age = st.radio(
    label = 'Age: ',
    options = ['18-30', '30-50', '50+']
)

st.header('Buy a product')

o_category = st.selectbox(
    label = 'Product category: ',
    options = ['Food Supplies', 'Medical Supplies', 'Office Supplies'],
    index = 0
)

products_in_category = []

#----------------------------
if o_category == 'Food Supplies':
    products_in_category = ['Oil 1 lit', 'Wheat 0.5 kg', 'Rice 0.5 kg', 'Maggie 1 pack', 'Milk 0.5 lit']
    
elif o_category == 'Medical Supplies':
    products_in_category = ['Bandaid 10 strips', 'Betadine 50 ml', 'Cyclopalm 1 strip', 'Paracetamol 1 strip', 'Dettol 100 ml']
    
elif o_category == 'Office Supplies':
    products_in_category = ['Pen 1 unit', 'Permanent Marker 1 unit', 'Record Book 1 book', 'Observation Book 1 book', 'Rough Book 1 book']
#----------------------------

o_product = st.selectbox(
    label = 'Product name: ',
    options = products_in_category
)

o_quantity = st.slider(
    label = 'Quantity: ',
    min_value = 1,
    max_value = 5,
    value = 1
)

unit_prices = {
    'Oil 1 lit':50,
    'Wheat 0.5 kg':50,
    'Rice 0.5 kg':50,
    'Maggie 1 pack':20,
    'Milk 0.5 lit':20,
    'Bandaid 10 strips':10,
    'Betadine 50 ml':30,
    'Cyclopalm 1 strip':10,
    'Paracetamol 1 strip':10,
    'Dettol 100 ml':20,
    'Pen 1 unit':5,
    'Permanent Marker 1 unit':20,
    'Record Book 1 book':10,
    'Observation Book 1 book':10,
    'Rough Book 1 book':10
}

o_amount = unit_prices[o_product] * o_quantity

st.text_input(
    label = 'Amount: ',
    value = '₹ '+str(o_amount),
    disabled = True
)

if st.button('Place Order'):
    st.write('Establishing connection...')
    cxn = pg2.connect(
        dbname = "xvrkpedt",
        user = "xvrkpedt",
        password = "fvRfE3Cyv3RUX3fLhdkVJboWIu_2wSuk",
        host = "kiouni.db.elephantsql.com",
        port = "5432"
    )
    cur = cxn.cursor()
    st.write('Connection successful ✅')
    cur.execute(f"INSERT INTO ORDERS(name, email, gender, age, product, units, amount) VALUES ('{u_name}', '{u_email}', '{u_gender}', '{u_age}', '{o_product}', {o_quantity}, {o_amount});")
    cur.execute(f"UPDATE warehouse SET units = units - {o_quantity} WHERE product='{o_product}';")
    cur.execute('COMMIT;')
    st.write('Order placed ✅')
    cur.close()
    cxn.close()
    st.write('Connection closed gracefully ✅')