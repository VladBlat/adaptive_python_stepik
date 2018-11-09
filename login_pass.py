from random import randint

user_login, user_password = randint(100000, 999999), randint(100000, 999999)

login, password = tuple(map(int, input().split()))

if (login == user_login) and (password == user_password):
    print("Login success")
elif (login == user_login) and (password != user_password):
    print("Wrong password")
elif (login != user_login):
    print("No user with login {} found".format(login))
