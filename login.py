def login(username, password):
    if username == "admin" and password == "password123":
        return "Login Successful"
    return "Invalid Username or Password"


if __name__ == "__main__":
    username = input("Enter username: ")
    password = input("Enter password: ")
    print(login(username, password))
