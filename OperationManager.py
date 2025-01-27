from Utils import validate_input, print_menu
from UserManager import *
from SellerManager import *
from BuyerManager import *
from PickleHelper import save_cart

MENU = {
        'user': [
            '1. Register / Login', 
            '2. End the program'
           ],
        'buyer': [
              '1. Buy product(s)', 
              '2. View cart and confirm order',
              '3. View your recent orders', 
              '4. End the program'
            ],
        'seller': [
            '1. Set inventory for a product',
            '2. Add a new product',
            '3. Delete a product',
            '4. View all products',
            '5. End the program'
          ]
        }
class OperationManager:
    def __init__(self):
        self.UserManager = UserManager()
        self.SellerManager = SellerManager()
        self.BuyerManager = BuyerManager(self.SellerManager)

    def user_menu(self):
        while True:
          choice = print_menu(MENU['user'])
          if choice == 1:
            self.user()
          elif choice == 3:
            self.UserManager.view_users()
          else:
            break
    
    def buyer_menu(self, user_id):
        while True:
          choice = print_menu(MENU['buyer'], 'BUYER')
          if choice == 1:
              self.buy_products(user_id)
          elif choice == 2:
              self.view_cart(user_id)
          elif choice == 3:
              self.show_orders(user_id)
          else:
              break
          
    def seller_menu(self, user_id):
        while True:
          choice = print_menu(MENU['seller'], 'SELLER')
          if choice == 1:
            self.set_inventory(user_id)
          elif choice == 2:
            self.add_product(user_id)
          elif choice == 3:
            self.delete_product(user_id)
          elif choice == 4:
            self.view_products(user_id)
          else:
            break
    
    def show_orders(self, user_id):
        print(f'***** Hey {user_id}, YOUR RECENT ORDERS *****')
        self.BuyerManager.show_orders(user_id)

    def view_cart(self, user_id):
        self.BuyerManager.view_cart(user_id)
        confirm = input('Do you want proceed with placing order right now (press Y/N): ')
        if confirm == 'Y':
            order_id = self.confirm_order(user_id)
            print(f'Order placed successfully and your order id:{order_id}')
        else: 
            self.buyer_menu(user_id)

    def confirm_order(self, user_id):
        return self.BuyerManager.confirm_order(user_id)

    def buy_products(self, user_id):
        flag = 'Y'
        bucket = {}
        while flag == 'Y':
          category_choice = input('Choose a category (1. Electronics 2. Home Appliants 3. Others): ')
          self.BuyerManager.buy_products(user_id, category_choice, bucket)
          flag = input('Do you want to continue with other categories (press Y/N): ')
        
        if user_id not in self.BuyerManager.cart:
            self.BuyerManager.cart[user_id] = {}     
        self.BuyerManager.cart[user_id] = bucket
        save_cart(self.BuyerManager.cart_date_file, self.BuyerManager.cart)
        confirm = input('Do you want confirm order right now (press Y/N): ')
        if confirm == 'Y':
            order_id = self.confirm_order(user_id)
            print(f'Order placed successfully and your order id:{order_id}')
        else: 
            self.buyer_menu(user_id)

    def delete_product(self, user_id):
         product_id = validate_input('Enter the product id you wise to delete: ')
         self.SellerManager.delete_product(user_id, product_id)

    def set_inventory(self, user_id):
        product_id = validate_input('Enter the product id: ')
        quantity = input('Enter available quantity: ')
        self.SellerManager.set_inventory(user_id, product_id, quantity)

    def view_products(self, user_id):
        self.SellerManager.view_products(user_id)

    def add_product(self, user_id):
        product = {}
        product['pname'] = input('Enter product name: ')
        product['category'] = input('Choose product category (1. Electronics 2. Home Appliants 3. Others): ')
        product['price'] = validate_input('Enter price for product: ')
        product['inventory'] = validate_input('Enter available quantity (i.e., 1, 2,..): ')
        self.SellerManager.add_product(user_id, product)

    def add_user(self):
        user_input = {}
        user_input['name'] = input('Enter your name: ')
        user_input['email'] = input('Enter your email: ')
        user_input['phone'] = input('Enter your phone number: ')
        user_input['type'] = input('Select your choice (1. Buyer / 2. Seller): ')
        user_input['password'] = input('Enter password: ')
        self.UserManager.add_user(user_input)
    
    def verify_user(self):
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        verify = self.UserManager.verify_user(username, password)

        if not verify:
            return print(f'username or password is wrong, please check and try again!')
        
        user_id, user_type = verify
        if user_type == '1':
            self.buyer_menu(user_id)
        else:
            self.seller_menu(user_id)

    def user(self):
        user = input('Are you a new user (type, Y/N): ').strip()
        if user == 'Y':
            self.add_user()
        else:
            self.verify_user()

    def run(self):
        self.user_menu()