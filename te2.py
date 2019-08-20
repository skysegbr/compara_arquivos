def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 

dc1 = {'a' : 1, 'b': 2}
dc2 = {'a' : 1, 'c': 2}
lst1 = [4, 'a', 1, 17, 11, 26, 28, 54, 69, {'a' : 1, 'b': 2}] 
lst2 = [9, 'a', 74, 21, 45, 11, 63, 28, 26, {'a' : 1, 'c': 2}] 

print(intersection(lst1, lst2)) 