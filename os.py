#PonosOS v1 by govnocoder1337
import os
import time

def calculator():
    zapros = input("запрос:")
    otvet = eval(zapros)
    print("ответ:", otvet)
    time.sleep(1)
    return main()

def name():
   name = os.getlogin()
   print("Ваше имя:", name)
   time.sleep(1)
   return main()

def user():
    user = os.getlogin()
    print("Добро пожаловать,", user)
    time.sleep(1.5)

def main():
    print("[1] Калькулятор")
    print("[2] Ваше имя")
    print("[3] Завершить работу")
    otvet = input("Ваш ответ:")
    if otvet == "1":
        calculator()
    if otvet == "2":
        name()
    if otvet == "3":
        exit()

    else:
        print("Я вас не понимаю, повторите запрос.")
        time.sleep(1)
        main()

user()
if __name__ == '__main__':
    main()
