#2.Get missing number in [1..100]
def get_missing(lst):
    return set(range(lst[len(lst)-1])[1:]) - set(l)

l = list(range(1,100))
l.remove(63)
print(get_missing(l)) #63

