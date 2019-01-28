def my_strrev(ary):
    str1 = list(ary)
    for i in range(len(str1)//2):
        t = ary[i]
        str1[i] = str1[len(str1)-1-i]
        str1[len(ary)-1-i] = t
    ary = "".join(str1)
    return ary
ary = "abcde"
ary = my_strrev(ary)
print(ary)

# Reverse this strings
s = ary[-1::-1]
print(s)