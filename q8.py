#8.Reverse string using recursion
def reverse_string(s):
    if len(s)<=1:
        return s
    return reverse_string(s[1:])+s[0]

print(reverse_string("codecube")) #ebucedoc

