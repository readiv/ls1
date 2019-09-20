#Скачайте файл по ссылке
#Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
#Подсчитайте количество слов в тексте
#Замените точки в тексте на восклицательные знаки
#Сохраните результат в файл referat2.txt

with open('referat.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    
print(f"Длинна файла {len(content)} байт")
print(f"Число слов {len(content.split(' '))}")

content = content.replace('.','!')

with open('referat2.txt', 'w', encoding='utf-8') as f:
    f.write(content)


