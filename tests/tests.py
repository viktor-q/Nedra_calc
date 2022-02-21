from modules.simple_calc import SimpleCalculator

#x = '3 +(2-1)+3*2'  # =14
#x = "3+2-6.5"  # = -1.5

#x = "+100.1" #→ 100.1
#x = "-0" #→ 0
#x = "-7 / 34.2"  # → -0.205   СДЕЛАТЬ ОКРУГЛЕНИЕ
#x = "- 6 * 2" #→ -11.98
#x = "2. / 1." #→ 2

#x = "5 + - 4" #→ ошибка
#x = "*1 + 7" #→ ошибка

# MY TESTS
#x = "8+ (2)*3"   #30
#x = "8+2(3)"  #ошибка #Попробовать тоже перехватить


# testfoo = SimpleCalculator()
#
#
# print(testfoo.calculation_from_string(x))



from modules.logger import Logger

newclass = Logger()

#newclass.add_log_to_json("5+5", "10")
result = newclass.read_log_from_json(None, "success")
print(result)