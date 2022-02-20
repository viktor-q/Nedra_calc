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
            return f'fuck, bad start symbol'

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

    first = op[operator](float(first), float(second)) #make_end

    return first, second, operator


x = "5.55+5.45*2"  # =12
print(calculation_from_string(x))

