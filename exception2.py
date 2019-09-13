"""

Домашнее задание №1

Исключения: приведение типов

Перепишите функцию discounted(price, discount, max_discount=20)из урока про функции так, 
чтобы она перехватывала исключения, когда переданы некорректные аргументы 
(например, строки вместо чисел).
    
"""

def discounted(price, discount, max_discount=20):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(float(max_discount))
        if max_discount > 99:
            raise ValueError('Слишком большая максимальная скидка')
        if discount >= max_discount:
            raise ValueError('Скидка больше максимальной')
        else:
            return price - (price * discount / 100)
    except (ArithmeticError,ValueError,TypeError) as e:
        print('Исключение: ',e)
        return price    
       
    
if __name__ == "__main__":
    print(f'discounted(1000, 10) = {discounted(1000, 10)}')
    print('##########################################')
    print(f'discounted(1000, 10, 100) = {discounted(1000, 10, 100)}')
    print('##########################################')
    print(f'discounted(1000, 50) = {discounted(1000, 50)}')
    print('##########################################')
    print(f"discounted('fds2', 10) = {discounted('fds2', 10)}")
    print('##########################################')
    print(f"(discounted(1000, 'dddx') = {discounted(1000, 'dddx')}")

