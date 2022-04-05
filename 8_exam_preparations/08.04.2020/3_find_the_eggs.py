from math import ceil


def find_strongest_eggs(*args):
    arguments = args[0]
    n = int(args[1])
    data_base = []
    for i in range(n):
        data_base.append([])
    while arguments:
        for i in range(n):
            if not arguments:
                break
            element = arguments.pop(0)
            data_base[i].append(element)
    
    strong_eggs = []
    for substring in data_base:
        mid_element = substring[len(substring) // 2]
        left_element = substring[len(substring) // 2 - 1]
        right_element = substring[len(substring) // 2 + 1]
        if left_element < mid_element > right_element > left_element:
            strong_eggs.append(mid_element)
    
    return strong_eggs


    

test = ([51, 21, 83, 52, 55], 1)
print(find_strongest_eggs(*test))









