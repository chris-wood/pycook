def trim_lists_at_index(lists, index):
    nl = []
    length = len(lists)

    for i in range(index):
        nl.append(lists[i])
    nl.append(lists[index][1:])
    for i in range(index + 1, length):
        nl.append(lists[i])

    return nl

def collect_arguments(*args):
    lists = []
    index = 0
    for l in args:
        if type(l) != list:
            raise Exception("Invalid argument type for parameter " + str(index) + ": " + repr(type(l)))
        index += 1
        lists.append(l)
    return lists

def combinations(*args):
    lists = collect_arguments(*args)
    instance = map(lambda l : l[0], lists)
    combs = [instance]
    for i, l in enumerate(lists):
        if len(l) > 1:
            params = trim_lists_at_index(lists, i)
            combination_results = filter(lambda l : l not in combs, combinations(*params))
            for result in combination_results:
                combs.append(result)
    return combs

def combinations_1(l1, l2):
    result = [l1[0], l2[0]]
    
    children = [result]
    if len(l1) > 1:
        combination = combinations_1(l1[1:], l2)
        for c in combination:
            if c not in children:
                children.append(c)
    if len(l2) > 1:
        combination = combinations_1(l1, l2[1:])
        for c in combination:
            if c not in children:
               children.append(c)
    
    return children


l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']
l3 = [7, 8, 9]
print combinations_1(l1, l2)
print combinations(l1, l2)


