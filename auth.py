import hashlib
import json
import os

USERS_FILE = 'users.json'

# Create users file if it doesn't exist
if not os.path.exists(USERS_FILE):
    with open(USERS_FILE, 'w') as file:
        json.dump([], file)

def hash_password(password):
    #Hashes a password using SHA-256.
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    #Registers a new user with a hashed password.
    with open(USERS_FILE, 'r') as file:
        users = json.load(file)

    if any(user['username'] == username for user in users):
        return False, "Пользователь с таким именем уже существует."

    users.append({
        'username': username,
        'password': hash_password(password)
    })

    with open(USERS_FILE, 'w') as file:
        json.dump(users, file)

    return True, "Регистрация прошла успешно."

def login(username, password):
    #Authenticates a user by comparing the hashed password.
    with open(USERS_FILE, 'r') as file:
        users = json.load(file)

    for user in users:
        if user['username'] == username and user['password'] == hash_password(password):
            return True, "Успешный вход."

    return False, "Неверное имя пользователя или пароль."
