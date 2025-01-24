
import random

def validate_input(message, start = 0, end = None):
    while True:
        user_input = input(message).strip()

        if not user_input.isdecimal():
            print('Invalid input. Try again!!')
        elif start is not None and end is not None:
            if not (start <= int(user_input) <= end):
                print('Invalid input. Try again!!')
            else:
                return int(user_input)
        else:
            return int(user_input)

def generate_id(prefix = '', is_user_name = False):
    digit = random.choice(range(100))
    if is_user_name:
        return f"{prefix}_{digit}"
    return f"{prefix}-{digit}"