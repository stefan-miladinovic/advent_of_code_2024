"""
The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate
levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both
of the following are true:

The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.
"""

# get the report from file
filename = "input_three"
no_newlines = []
problem_dampener_input = []

with open(filename) as f:
    read_file = f.readlines()

for i in read_file:
    no_newlines.append(i.strip())


# parse and format the data appropriately
def data_preparation(input_data):
    input_data_ints = []
    for row in input_data:
        row_split = row.split()
        _i = 0
        for e in row_split:
            row_split[_i] = int(e)
            _i += 1
        input_data_ints.append(row_split)
    return input_data_ints


def condition_one(input_data) -> bool:
    """
    Tests if the levels are all increasing or decreasing
    :param input_data:
    :return: boolean - True if the first condition is fulfilled
    """
    increasing = False
    decreasing = False

    # check whether the array is increasing
    pos = 0
    while pos < len(input_data) - 1:
        if input_data[pos] < input_data[pos + 1]:
            increasing = True
            pos += 1
        else:
            increasing = False
            break

    # check whether the array is decreasing, only if it's not increasing
    if not increasing:
        pos = 0
        while pos < len(input_data) - 1:
            if input_data[pos] > input_data[pos + 1]:
                decreasing = True
                pos += 1
            else:
                decreasing = False
                break

    if increasing or decreasing:
        return True
    else:
        return False


def condition_two(input_data) -> bool:
    """
    Tests if the two adjacent levels differ by at least one and at most three
    :param input_data:
    :return:
    """
    diff_cond = False

    pos = 0
    while pos < len(input_data) - 1:
        diff = abs(input_data[pos] - input_data[pos + 1])
        if 1 <= diff <= 3:
            diff_cond = True
            pos += 1
        else:
            diff_cond = False
            break

    return diff_cond


def problem_dampener_processing(input_data) -> bool:
    """
    Applies the Problem Dampener rules to the data that doesn't pass scrutiny.
    :param input_data: data that has been marked as `doesn't fit original conditions`
    :return: boolean, True if the results can be damped
    """

    pos = 0
    dampened = False
    while pos < len(input_data):
        _temp_row = input_data[
                    :]  # this assignment is important in Python, as standard equality only references the address
        _temp_row.pop(pos)
        pos += 1
        if condition_one(_temp_row) and condition_two(_temp_row):
            dampened = True
            break
        else:
            dampened = False

    return dampened


# method to calculate the safety
def calculate_report_safety_counts(input_data) -> int:
    safe_reports = 0
    for row in input_data:
        cond_one = condition_one(row)
        cond_two = condition_two(row)
        if cond_one and cond_two:
            safe_reports += 1
        else:
            problem_dampener_input.append(row)
    return safe_reports


# method to calculate the dampened data
def calculate_dampened_safety_counts(input_data) -> int:
    dampened_reports = 0
    for row in input_data:
        if problem_dampener_processing(row):
            dampened_reports += 1
    return dampened_reports


# final working
final_data = data_preparation(no_newlines)

total_safe = calculate_report_safety_counts(final_data)
print(f"Total number of safe reports: {total_safe}\n")

total_dampened = calculate_dampened_safety_counts(problem_dampener_input)
print(f"Total number of dampened reports: {total_dampened}\n")

print(f"Grand total of safe reports: {total_safe + total_dampened}")
