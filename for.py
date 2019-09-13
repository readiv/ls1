"""
Домашнее задание №1 

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

import random

def get_averege_and_sum(scores):
    """ На входе список [3,4,4,5,2]
        На выходе среднее и сумма
    """
    sum = 0
    for i in scores:
        sum +=i
    return sum/len(scores),sum    

def main():
    print('*Создать список из десяти целых чисел.\n*Вывести на экран каждое число, увеличенное на 1.')
    integer10 = [10,15,27,388,466,5444,62,73,85,97]
    s=''
    for n in integer10:
        s+=str(n+1)+' '
    print(s+'\n')
    
    print('*Ввести с клавиатуры строку.\n*Вывести эту же строку вертикально: по одному символу на строку консоли.')
    s = input('Введите строку:')
    for char in s:
        print(char)
        
        #Создать список из словарей с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
        #Посчитать и вывести средний балл по всей школе.
        #Посчитать и вывести средний балл по каждому классу.  
    
    #Скучно просто забивать данные. Сформирую случайно    
    nclas = random.randint(1, 10) #число классов
    if nclas > 280:
        nclas = 280 #Выплывает из ограниений наименований класов
    rating_school = []
    for iclas in range(nclas):
        clas = {}
        while True:
            s = 'абвгдежзийклмнопрстуфхцчшщ'
            s = str(random.randint(1,11)) + s[random.randint(0, len(s)-1)] #Всего примерно 280  вариантов
            #Проверка на уникальность
            if len(rating_school) == 0: #Ещё не с чем сравнивать
                break
            else:
                flag = True #считаем что уникально
                for clas_one in rating_school:
                    if clas_one['school_class'] == s:
                        flag = False #Печалька. Не уникально
                        break
                if flag:                     
                    break
        clas['school_class'] = s
        rating_school.append(clas)
        scores = []
        for i in range(random.randint(5,20)): 
            scores.append(random.randint(1,5))
        clas['scores'] = scores   
        
    print('Данные сформированы')    
    print(rating_school) 
    
    len_global_school=0
    sum_global_school=0
    
    for clas in rating_school:
        print('#####################################################')
        print(f"Класс: {clas['school_class']}")
        print(f"Оценки: {clas['scores']}")
        avg_clas,sum_clas = get_averege_and_sum(clas['scores'])
        len_global_school += len(clas['scores'])
        sum_global_school += sum_clas
        print(f"Средний бал: {avg_clas}")
        
    print('#####################################################')
    print(f"Средний бал по школе: {sum_global_school/len_global_school}")
                    
if __name__ == "__main__":
    random.seed()
    main()        
    input("Press Any Enter :-) ")
