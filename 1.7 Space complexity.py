input1 = [3, 7, 3, 5, 2, 5, 9, 2]
input2 = [-1, 2, -1, 3, 2, -2]
input3 = [1000000, 999999, 1000000]

for input_list in [input1, input2, input3]:
    unique_list = list(set(input_list))
    print(unique_list)
