MIN_LENGTH = 6
users_password = input("Enter password: ")
while len(users_password) < MIN_LENGTH:
    print(f"Invalid. Please enter at least {MIN_LENGTH} character")
    users_password = input("Enter password: ")
print('*' * len(users_password))
