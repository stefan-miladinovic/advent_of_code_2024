"""
This time, you'll need to figure out exactly how often each number from the left list appears in the right list.
Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of
times that number appears in the right list.

Here are the same example lists again:

3   4
4   3
2   5
1   3
3   9
3   3
For these example lists, here is the process of finding the similarity score:

The first number in the left list is 3. It appears in the right list three times, so the similarity score increases by 3 * 3 = 9.
The second number in the left list is 4. It appears in the right list once, so the similarity score increases by 4 * 1 = 4.
The third number in the left list is 2. It does not appear in the right list, so the similarity score does not increase (2 * 0 = 0).
The fourth number, 1, also does not appear in the right list.
The fifth number, 3, appears in the right list three times; the similarity score increases by 9.
The last number, 3, appears in the right list three times; the similarity score again increases by 9.
So, for these example lists, the similarity score at the end of this process is 31 (9 + 4 + 0 + 0 + 9 + 9).

Once again consider your left and right lists. What is their similarity score?
"""

# read the file into one list -> each line is one entry in the list
filename = "input_one"

with open(filename) as f:
    full_data = f.readlines()

left_list = list()
right_list = list()

# separate this into two lists (each number has five digits) and parse them as integers (they are string by default)
for line in full_data:
    _left_element = line[:5]
    _right_element = line[8:].strip()
    left_list.append(int(_left_element))
    right_list.append(int(_right_element))


def test_function(ex_left_list, ex_right_list):
    # sort the values, this also removes all the duplicate entries. Only needed for the left list
    sorted_ex_left_list = ex_left_list
    sorted_ex_left_list.sort()

    sorted_ex_numbers_dict = {k:v for (k,v) in zip(sorted_ex_left_list, ([0]*len(sorted_ex_left_list)))}

    # Calculate repetition info for individual numbers
    for i in sorted_ex_left_list:
        count_i = 0
        for j in ex_right_list:
            if i == j:
                count_i += 1
        sorted_ex_numbers_dict.update({i: count_i*i})

    # Calculate total similarity index
    total_sim_score = 0
    for i in ex_left_list:
        total_sim_score += sorted_ex_numbers_dict.get(i)

    print(f"Total similarity index is: {total_sim_score}")

test_function(left_list, right_list)