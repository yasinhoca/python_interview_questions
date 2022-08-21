#14.Find all permutations of string
def get_permutations(s):
    if len(s)<=1:
        return set(s)
    smaller = get_permutations(s[1:])
    perms = set()
    for x in smaller:
        for pos in range(0,len(x)+1):
            perm = x[:pos] + s[0] + x[pos:]
            perms.add(perm)
    return perms

print(get_permutations("say"))
#{'ysa', 'ays', 'yas', 'say', 'sya', 'asy'}

