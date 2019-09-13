# -*- coding: utf-8 -*-
"""

Домашнее задание №1

Цикл while: ask_user

Напишите функцию ask_user(), которая с помощью input() спрашивает пользователя “Как дела?”, пока он не ответит “Хорошо”

   
"""


def ask_user():
    """
    Замените pass на ваш код
    """
    
    flag = False
    while not flag:
        kak_dela = input("Как ваши дела? ").lower()
        flag=kak_dela=='хорошо'
        if not flag:
            print('Неужели всё так плохо? Может всё же хорошо?')
            
    print('Вот и прекрасно!')
          
   
    
if __name__ == "__main__":
    ask_user()
