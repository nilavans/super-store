
from Utils import generate_id
from PickleHelper import load_users, save_user
from User import *

USER_DATA_FILE = "data/users.pkl"

class UserManager:
    def __init__(self):
        self.users = load_users(USER_DATA_FILE)
    
    def add_user(self, user_input):
        for user in self.users:
            if self.users[user].email == user_input['email']:
                return print(f"User with {user.email} already exist !")
            
        if user_input['type'] == '1': 
            buyer_id = generate_id(user_input['name'].lower(), True)
            new_user = User(buyer_id, user_input['name'], user_input['email'], user_input['phone'], user_input['type'], user_input['password'])
            self.users[buyer_id] = new_user
            save_user(USER_DATA_FILE, self.users)
            print(f'User created successfully!, and your username is {buyer_id}')
        else:
            seller_id = generate_id(user_input['name'].lower(), True)
            new_user = User(seller_id, user_input['name'], user_input['email'], user_input['phone'], user_input['type'], user_input['password'])
            self.users[seller_id] = new_user
            save_user(USER_DATA_FILE, self.users)
            print(f'User created successfully!, and your username is {seller_id}')

    def verify_user(self, username, password):
        if username in self.users and self.users[username].password == password:
            print(f"Welcome back!, {username}")
            return (username, self.users[username].type)
        return False

    # for dev purpose only.   
    def view_users(self):
        for user in self.users:
            print(self.users[user])
            print('*****')
            
