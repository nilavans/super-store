from PickleHelper import load_product, save_products
from Product import *

PRODUCT_DATA_FILE = 'data/products.pkl'

class SellerManager:
    def __init__(self):
        self.products = load_product(PRODUCT_DATA_FILE)
        self.product_data_file = PRODUCT_DATA_FILE

    def add_product(self, user_id, product):
        if product['category'] not in self.products:
            self.products[product['category']] = {}
        new_product = Product(len(self.products[product['category']])+1, user_id, product['pname'], product['category'], product['price'], product['inventory'])
        if user_id not in self.products[product['category']]:
            self.products[product['category']][user_id] = []

        self.products[product['category']][user_id].append(new_product)
        save_products(PRODUCT_DATA_FILE, self.products)
        print(f'Product added successfully.')

    def seller_products(self, seller_id):
        seller_products = {}
        for category, sellers in self.products.items():
            if seller_id in sellers:
                seller_products[category] = sellers[seller_id]

        if not seller_products:
            return print(f'No products listed by {seller_id} yet..')
        return seller_products

    def view_products(self, seller_id):
        products = self.seller_products(seller_id)
        if products:
            for category, items in products.items():
                print(f'Category: {category}')
                for item in items:
                    print(item, end='')
        return
    
    def set_inventory(self, seller_id, pid, quantity):
        products = self.seller_products(seller_id)
        if products:
            for _, product in products.items():
                for item in product:
                   if item.product_id == pid:
                    item.inventory = quantity
                    save_products(PRODUCT_DATA_FILE, self.products)
                    print(f'Inventory updated successfully for product id: {pid}')
                    return     
            return print(f'There is no product with this id {pid}')
    
    def delete_product(self, seller_id, pid):
        products = self.seller_products(seller_id)
        if products:
            for category, product in products.items():
                for item in product:
                   if item.product_id == pid:
                    product.remove(item)
                    if not products:
                        del self.products[category][seller_id]
                    save_products(PRODUCT_DATA_FILE, self.products)
                    print(f'Deleted a product successfully with product id: {pid}')
                    return     
            return print(f'There is no product with this id {pid} to be deleted.')
    