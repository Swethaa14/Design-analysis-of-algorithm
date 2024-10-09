test1 = []  
test2 = [5]  
test3 = [3, 3, 3, 3, 3]  

for test in [test1, test2, test3]:
    if len(test) == 0:
        print("List is empty")
    else:
        sorted_list = sorted(test)
        print(sorted_list[-1])
