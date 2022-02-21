from modules.round_upper import round_up


class SimpleCalculator:
    @round_up
    def calculation_from_string(self, input_string: str):
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

        if (operator == "") and (second == ""):  # make end
            return first
        else:
            first = op[operator](float(first), float(second))

        return first

