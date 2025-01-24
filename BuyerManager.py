from PickleHelper import load_cart, load_users, save_cart, save_order, save_products
from Utils import generate_id

CART_DATA_FILE = 'data/cart.pkl'
ORDER_DATA_FILE = 'data/orders.pkl'

class BuyerManager:
    def __init__(self, seller_manager):
        self.SellerManager = seller_manager
        self.cart = load_cart(CART_DATA_FILE)
        self.orders = load_users(ORDER_DATA_FILE)
        self.cart_date_file = CART_DATA_FILE
    
    def view_products(self, category = None):
        for _category, products in self.SellerManager.products.items():
            if category == _category:
               print(f'Category: {category}')
               for seller, product in products.items():
                print(f'Seller Id: {seller}')
                for item in product:
                    print(item)

    def buy_products(self, buyer_id, category, bucket = {}):
        flag = 'Y'
        self.view_products(category)
        while flag == 'Y':
          selected_product = input('Select any product you want (i.e., Product ID): ')
          if category not in bucket:
             bucket[category] = []
          bucket[category] = selected_product
          flag = input("Press 'Y' to continue, else press 'N': ")
        return bucket
    
    def get_product_by_category_and_product_id(self, category, pid):
        for _category, products in self.SellerManager.products.items():
            if category == _category:
               for _, product in products.items():
                for item in product:
                    if item.product_id == pid:
                       return item
        return print(f'There is no product')


    def display_cart(self, cart):
       quantity = 0
       total_price = 0
       for category, items in cart.items():
          for item in items:
            product = self.get_product_by_category_and_product_id(category, int(item))
            if product.inventory == 0:
               print(f'Currently their is no stock available for the product with product id: {product.product_id}')
               break
            total_price += product.price
            quantity += 1
            print('*******CART ITEMS*******')
            print(product)
       print(f"TOTAL QUANTITY: {quantity}\t TOTAL AMOUNT: {total_price}")

    def view_cart(self, buyer_id):
       if buyer_id not in self.cart:
          return print(f'Cart is empty, please add some product!')
       cart = self.cart[buyer_id]
       self.display_cart(cart)

    def confirm_order(self, buyer_id):
       order_id = generate_id('ORDER')
       quantity = 0
       total_price = 0
       cart = self.cart[buyer_id]
       confirm_items = []
       for category, items in cart.items():
          for item in items:
            product = self.get_product_by_category_and_product_id(category, int(item))
            if product.inventory <= 0:
                print(f'There is no stock available {product.pname}')
                break
            product.inventory-=1
            total_price += product.price
            quantity += 1
            confirm_items.append(product)
       if buyer_id not in self.orders:
          self.orders[buyer_id] = {}
       order = {
          'confirmed_items': confirm_items,
          'total_quantities': quantity,
          'total_cost': total_price
       }
       self.orders[buyer_id][order_id] = order
       del self.cart[buyer_id]
       save_cart(CART_DATA_FILE, self.cart)
       save_order(ORDER_DATA_FILE, self.orders)
       save_products(self.SellerManager.product_data_file ,self.SellerManager.products)
       return order_id
    
    def show_orders(self, buyer_id):
        orders = self.orders.get(buyer_id)
        if not orders:
          return print(f'No orders booked yet.')
        for oid, details in orders.items():
            print(f'ORDER ID: {oid}\tTOTAL AMOUNT: {details['total_cost']}\t QUANTITIES: {details['total_quantities']}')
            for _, detail in details.items():
                if type(detail) == list:
                    for item in detail:
                      print(f'PRODUCT NAME: {item.pname}\t PRODUCT ID: {item.product_id}\t PRICE:{item.price}')
        return            

       



            

