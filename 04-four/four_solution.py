"""
However, because the program's memory has been corrupted, there are also many invalid characters that should be ignored,
even if they look like part of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.

For example, consider the following section of corrupted memory:

xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
Only the four highlighted sections are real mul instructions. Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).

Scan the corrupted memory for uncorrupted mul instructions. What do you get if you add up all of the results of the multiplications?
"""

import re

# get the data from file
filename = "input_four"
reg_x = r"(mul\(\d+\,\d+\))"  # needs to be declared as raw string to prevent illegal escape sequence for \d etc.

with open(filename) as f:
    input_data = f.read()

correct_muls = re.findall(reg_x, input_data)  # returns the list of all correct `mul` operators


def calculate_final_result(muls_list) -> int:
    nums_from_expr = []
    for row in muls_list:
        if row is None:
            continue
        else:
            _strip_1 = row.strip('mul(')
            _strip_2 = _strip_1.strip(')')
            for i, char in enumerate(_strip_2):
                if char == ',':
                    _num_1 = int(_strip_2[:i])
                    _num_2 = int(_strip_2[i + 1:])
                    _calc = _num_1 * _num_2
                    nums_from_expr.append(_calc)
    _final_result = 0
    for row in nums_from_expr:
        _final_result += row
    return _final_result


print(f"The final result is {calculate_final_result(correct_muls)}")

"""
PART TWO
"""

reg_x_do = r"do\(\)"
reg_x_dont = r"don\'t\(\)"

only_with_dos = []

# split into subfiles each time a do is encountered

def calculate_final_result_with_dos() -> int:
    dos_list = re.split(reg_x_do, input_data)
    only_after_dos = ""
    for i in dos_list:
        temp_split = re.split(reg_x_dont, i)
        only_after_dos += temp_split[0]

    return calculate_final_result(re.findall(reg_x, only_after_dos))

print(f"The final result, including only those with dos is: {calculate_final_result_with_dos()}")
