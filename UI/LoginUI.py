from Models.Login import Login


def LoginUI():
    return Login(input("Enter your username: "), input("Enter your password: "))