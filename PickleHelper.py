import pickle
from pathlib import Path

def save_user(file_name, user_data):
    with open(file_name, 'wb') as users:
        pickle.dump(user_data, users)

def load_users(file_name):
    file_path = Path(file_name)
    if file_path.exists():
        with open(file_name, 'rb') as users:
            return pickle.load(users)
    return {}

def load_product(file_name):
    file_path = Path(file_name)
    if file_path.exists():
        with open(file_name, 'rb') as products:
            return pickle.load(products)
    return {}

def save_products(file_name, products_data):
     with open(file_name, 'wb') as products:
        pickle.dump(products_data, products)

def save_cart(file_name, cart_data):
    with open(file_name, 'wb') as cart:
        pickle.dump(cart_data, cart)

def load_cart(file_name):
    file_path = Path(file_name)
    if file_path.exists():
        with open(file_name, 'rb') as cart:
            return pickle.load(cart)
    return {}

def save_order(file_name, order_data):
    with open(file_name, 'wb') as orders:
        pickle.dump(order_data, orders)

def load_cart(file_name):
    file_path = Path(file_name)
    if file_path.exists():
        with open(file_name, 'rb') as orders:
            return pickle.load(orders)
    return {}