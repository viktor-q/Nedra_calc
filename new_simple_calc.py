def calculation_from_string(input_string):
    first = ""
    second = ""
    operator = ""

    nums = "0123456789"
    operators = "+-/*"

    op = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }

    for element in input_string:
        if (element in nums) and (first == ""):
            first += element
        elif element in operators:
            operator += element
        elif (element in nums) and (first != ""):
            second += element
            first = op[operator](float(first), float(second))
            second = ""
            operator = ""

    return first


x = "5+3-2" # =6
print(calculation_from_string(x))

