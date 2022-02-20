def calculation_from_string(input_string):
    first = ""
    second = ""
    operator = ""

    nums = "0123456789."
    operators = "+-/*"

    op = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }


    for element in input_string:
        if (first == "") and (element in "+-0123456789"):  # make first
            first += element
        elif (first == "") and (element not in "+-01234567890"):
            return f'custom EX: bad first symbol'

        elif (element in nums) and (operator == ""):
            first += element
        elif (element in operators) and (operator == ""):
            operator += element
        elif (element in nums) and (operator != ""):
            second += element
        elif (element in operators) and (operator != ""):
            first = op[operator](float(first), float(second))
            second = ""
            operator = element

    if (operator == "") and (second == ""):
        return first
    else:
        first = op[operator](float(first), float(second)) #make_end

    return first


x = '3 +(2-1)+3*2'  # =14
##x = "3+2-6.5"  # = -1.5

##x = "+100.1" #→ 100.1
##x = "-0" #→ 0
##x = "-7 / 34.2"  # → -0.205   СДЕЛАТЬ ОКРУГЛЕНИЕ
##x = "- 6 * 2" #→ -11.98
##x = "2. / 1." #→ 2

##x = "5 + - 4" #→ ошибка
##x = "*1 + 7" #→ ошибка

# MY TESTS
# x = "8+ (2)*3"   #30
# x = "8+2(3)"  #ошибка #Попробовать тоже перехватить
print(calculation_from_string(x))

