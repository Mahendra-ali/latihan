from user import show_user, add_user_prompt, delete_user_prompt, users, current_user, accounts
from transactions import (show_balance, withdraw_prompt, deposit_prompt,
                          transfer_prompt, show_transaction_prompt, show_transaction, transaction)

def login(current_user, user, password):
    for u in users:
        if u['user'] == user and u['password'] == password:
            current_user.update(u)
            return True
        return False

def login_process(current_user):
    while True:
        user = input('Username : ')
        password = input ('Password : ')
        if login(current_user, user, password):
            print('Login Succes')
            break
        else :
            print('Login Failed')
        
def menu(current_user):
    if current_user['role'] == 'amin':
        while True:
            print('1. Add User')
            print('1. Add User')
            print('1. Add User')
            print('1. Add User')
            print('1. Add User')
