import re

from modules.round_upper import round_up


class SimpleCalculator:
    @round_up
    def arithmetic(self, string_with_formula: str) -> float:
        operators = re.findall(r"[/,*,+,-]+", string_with_formula)  # [operators]
        nums = re.findall(r"([\d.]*\d+)", string_with_formula)  # [operands]
        starts = ("+", "-")

        if len(nums) == len(operators):
            if string_with_formula[0].isdigit():
                return f"ggggg"
            elif operators[0] in starts:
                nums[0] = str(operators[0]) + str(nums[0])
                operators = operators[1:]
            elif operators[0] not in starts:
                return f"fffff"  # выбрать, как кидать исключения Exception('ошибка')

        index_num = 0
        index_num2 = 1
        result = float(nums[0])

        try:
            if len(nums) == 1:
                if nums[0][0] == "+" or nums[0][1] == "0":
                    return nums[0][1:]
                if nums[0][0] == "-":
                    return nums[0]

            for t in range(len(operators)):
                op = {
                    "+": lambda x, y: x + y,
                    "-": lambda x, y: x - y,
                    "*": lambda x, y: x * y,
                    "/": lambda x, y: x / y,
                }

                num2 = float(nums[index_num2])
                num_operator = operators[index_num]
                result = op[num_operator](result, num2)

                index_num += 1
                index_num2 += 1

            return result
        except KeyError:
            return "неизвестная операция"
