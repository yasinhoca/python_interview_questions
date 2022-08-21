#3.Find dublicate number in integer list
def find_duplicates(elements):
    duplicates, seen = set(), set()
    for element in elements:
        if element in seen:
            duplicates.add(element)
        seen.add(element)
    return list(duplicates)

l=[2,5,2,4,5,1,3,9]
print(find_duplicates(l)) #2, 5

