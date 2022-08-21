#12.Sort list with Quicksort Algorithm
def qsort(l):
    if l==[]:
        return []
    return qsort([x for x in l[1:] if x<l[0]])+l[0:1]+ \
           qsort([x for x in l[1:] if x>=l[0]])

l = [12,34,2,6,9,11,9]
print(qsort(l)) #[2, 6, 9, 9, 11, 12, 34]

