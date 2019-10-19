__author__ = "Anton Troshin"
__version__ = "1.0"
__last_update_ = "Sep 20, 2019"

import time
s = 0
m = 0
h = 0
days = 1
days_for_print = "День №" + str(days)

while True:
   print('---') 
   s += 1
   # Свойства и настройка показа секунд
   if s < 10:
       _first_ = "0"
   else:
       _first_ = ""
   ########
   if s == 60:
       s -= 60
       m += 1
   # Свойства и настройка показа минут   
   if m < 10:
       _second_ = "0"
   else:
       _second_ = ""
   ########
   if m == 60:
       m -= 60
       h += 1
   # Свойства и настройка показа часов
   if h < 10:
       _third_ = "0"
   else:
       _third_ = ""
   ########
   if h == 24:
       h -= 24
       days += 1
       
   # Вывод на экран
   print(days_for_print + "      " +
         _third_ + str(h) + ":" +
         _second_ + str(m) + ":" +
         _first_ + str(s)
         )
   time.sleep(1)    