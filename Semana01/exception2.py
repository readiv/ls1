"""

Домашнее задание №1

Исключения: приведение типов

Перепишите функцию discounted(price, discount, max_discount=20)из урока про функции так, 
чтобы она перехватывала исключения, когда переданы некорректные аргументы 
(например, строки вместо чисел).
    
"""

def discounted(price, discount, max_discount=20):
    err = ''
    
    try:
        price = abs(float(price))
    except:
        err = "Цена: Вы должны ввести число."   
        
    try:
        discount = abs(float(discount))
    except:
        err = "Скидка: Вы должны ввести число"  

    try:
        max_discount = abs(float(max_discount))
    except:
        err = "Максимальная скидка: Вы должны ввести число."
        
    if not err and max_discount > 99:
        err = 'Слишком большая максимальная скидка'
        
    if not err and discount >= max_discount:
        err = 'Скидка больше максимальной'
        
    if err:
        print(err)
        return price
    return price - (price * discount / 100)#давай аккуратно выведем на экран, что не так, человеческим языком, а вход принимать из инпута
    
if __name__ == "__main__":
    while True:
        price = input('Цена: ')
        discount = input('Скидка: ')
        max_discount = input('Максимальная скидка: ')
        if max_discount:
            ds = discounted(price, discount, max_discount)
        else:
            ds = discounted(price, discount)
        print(ds)
        
    #print(f'discounted(1000, 10) = {discounted(1000, 10)}')
    #print('##########################################')
    #print(f'discounted(1000, 10, 100) = {discounted(1000, 10, 100)}')
    #print('##########################################')
    #print(f'discounted(1000, 50) = {discounted(1000, 50)}')
    #print('##########################################')
    #print(f"discounted('fds2', 10) = {discounted('fds2', 10)}")
    #print('##########################################')
    #print(f"(discounted(1000, 'dddx') = {discounted(1000, 'dddx')}")

