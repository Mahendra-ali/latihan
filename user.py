user = [
    {
    'user': 'aliademahendra@gmail.com',
    'password': '1234',
    'role': 'admin'
    }
]
accounts = []

current_user = []

def add_user(users, user, password, role):
    for u in users:
        if u['user'] == user:
            print('User already exist')
            return False
    else:
        users.append({
            'user': user,
            'password': password,
            'role':role
        })
        print('user asses')
        return True