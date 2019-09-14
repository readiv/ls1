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
    update.message.reply_text('Привет! Я ephem bot') #давай ещё здороваться по имени или юзернейму
    update.message.reply_text('Хотите узнать, в каком созвездии находится Ваша планета сегодня? Введите /planet название планеты на английском')

def planet(bot, update):
    edata = datetime.date.today()
    edata = str(edata.year)+'/'+str(edata.month)+'/'+str(edata.day) #посмотри “datetime tostring” 
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
    try:
        if update == None or update.message == None:
            return #Периоди́чески возникает такая хрень
        text = update.message.text.split(' ')
        if len(text)<2:
            raise ValueError('Ошибка. Вы не ввели название планеты')
        text = text[1].lower() #Получили название планеты
        ephem_one = ephem_dic.get(text) 
        if ephem_one==None:
            raise ValueError('Ошибка. Я не знаю такой планеты')
        const = ephem.constellation(ephem_one)
        if len(const) != 2: #На всякий случай
            raise ValueError('Ошибка. Я не знаю такой планеты')
            
        update.message.reply_text(f'Планета {text.upper()} сегодня находится в созвездии "{const[1].upper()}"')  
    except ValueError as e: # у тебя по смыслу тут ловится только ошибка «отсутствие в словаре» давай тогда только эту операцию транс и обернём, будет правильней
        update.message.reply_text(str(e))
        update.message.reply_text('Вы должны набрать /planet планета')
        update.message.reply_text('Сейчас я знаю такие планеты: '+str(list(ephem_dic))[1:-1]) #давай с большой буквы выведем планеты

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
