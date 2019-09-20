"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging, ephem, datetime, my_settings

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)


def greet_user(bot, update):
    if update == None or update.message == None:
        return #Периоди́чески возникает такая хрень    #смог проследить, когда? Это лучше на уровне хэндлеров разруливать, а не внутри функции
               #Нет. Повторяемость проследить не удалось. Пару раз вылезла - добавил. Немного непонятно как разрулить по хэндлерам. 
               #Если хэндлер сработал, по логике update должен быть заполнен, а он пуст... 
               #Как вмешаться в работу хэндлера? Не лезть же библиотеку править. 
               #Прокси у меня нет, т.к. тут телегу не блочат. Возможно какой то глюк телеги был.
    update.message.reply_text(f"Привет {update.message.chat['first_name']}\n Я Ephem Bot") #давай ещё здороваться по имени или юзернейму #Сделал
    update.message.reply_text('Хотите узнать, в каком созвездии находится Ваша планета сегодня? Введите /planet название планеты на английском')

def planet(bot, update):
    if update == None or update.message == None:
            return #Периоди́чески возникает такая хрень
        
    edata = f"{datetime.datetime.today():%Y/%m/%d}" #посмотри “datetime tostring” #Думаю так будет лучше 

    ephem_dic = {'mars':ephem.Mars(edata),
                 'moon':ephem.Moon(edata),
                 'mercury':ephem.Mercury(edata),
                 'venus':ephem.Venus(edata),
                 'jupiter':ephem.Jupiter(edata),
                 'saturn':ephem.Saturn(edata),
                 'uranus':ephem.Uranus(edata),
                 'neptune':ephem.Neptune(edata),
                 'pluto':ephem.Pluto(edata),
                 } 

    text = update.message.text.split(' ')
    try:        
        text = text[1].lower() #Получили название планеты
        ephem_one = ephem_dic[text]
        const = ephem.constellation(ephem_one)            
        update.message.reply_text(f'Планета {text.upper()} сегодня находится в созвездии "{const[1].upper()}"')  
    except: # у тебя по смыслу тут ловится только ошибка «отсутствие в словаре» давай тогда только эту операцию транс и обернём, будет правильней
        update.message.reply_text('Я вас не понял. Вы должны набрать /planet планета')
        update.message.reply_text('Сейчас я знаю такие планеты: '+str([x.capitalize() for x in list(ephem_dic)])[1:-1]) #давай с большой буквы выведем планеты
        

def talk_to_me(bot, update): 
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)
 

def main():
    mybot = Updater(my_settings.token_telegram)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
