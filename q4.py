#4.Compute the intersection of two lists
def intersect(lst1,lst2):
    res, lst2_copy = [],lst2[:]
    for el in lst1:
        if el in lst2_copy:
            res.append(el)
            lst2_copy.remove(el)
    return res

l1 = [1,2,3,5,9]
l2 = [0,1,5,7,9]
print(intersect(l1,l2)) #1,5,9

