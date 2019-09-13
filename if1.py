"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def chto_dolgen_delat(age:int):
    """
    по возрасту определит, чем должен заниматься пользователь: 
    учиться в детском саду, школе, ВУЗе или работать
    """    
    if age<6:
        return "Вам самое место в детском саду"
    elif age<17:
        return "Должно быть Вы учитесь в школе"
    elif age<22:
        return "Если не в армии, то только ВУЗ"
    else: 
        return "Детство кончилось! Добро пожаловать во взрослую жизнь"
       

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    age = 0
    while not age:
        age = input("Введите ваш возвраст: ")
        try:
            age = int(age)
            if age < 1:
                raise ValueError('Введено отрицательное или 0')
        except:
            print('Что то пошло не так. Вы должны ввести целое положительное число')
            age = 0       
    chto_delaet = chto_dolgen_delat(age)
    print(chto_delaet)

if __name__ == "__main__":
    main()
