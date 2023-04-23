

# TODO - Модули и пакеты
# TODO - Сторонние пакеты

# import my_module

# my_module.foo()

import funcations as fnc
# import pandas as pd
 
print(fnc.foo(), fnc.var, sep='\n')
 
# Что такое файл инициализации?
print(__name__)  # __main__
print(fnc.__name__)  # my_module
 
 
if __name__ == '__main__':  # файл который сейчас запущен
    print('Запуск скрипта/бота/сайта')
    # app.run()
    # bot.polling(token)
   

