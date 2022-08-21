#9.Find pairs of integers in list
#so that their sum is equal to x
def find_pairs(l,x):
    pairs=[]
    for (i,el_1) in enumerate(l):
        for (j, el_2) in enumerate(l[i+1:]):
            if el_1+el_2==x:
                pairs.append((el_1,el_2))
    return pairs

l = [12, 15, 19, 11, 24, 30]
print(find_pairs(l,26)) #15,11
print(find_pairs(l,31)) #12,19

