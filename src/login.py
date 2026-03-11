# login.py

def login(user):
    if user == "admin":
        return "Welcome"
    else:
        return "Access denied"

# пример использования функции
print(login("admin"))
print(login("user"))