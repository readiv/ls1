#Задание
#Создайте список словарей:
        #[
        #{'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        #{'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        #{'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    #]
#Запишите содержимое списка словарей в файл в формате csv

import csv

user_job = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
      ]

with open('export3.csv', 'w', encoding='utf-8', newline='') as f:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for user in user_job:
        writer.writerow(user)