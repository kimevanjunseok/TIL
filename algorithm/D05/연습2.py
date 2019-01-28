# def itoa(N):
#     result = ""
#     while N != 0:
#         s = N % 10
#         result = chr(48+s) + result
#         N = N // 10
#     return result
# a = 12313213485498
# print(itoa(a))
# b = itoa(a)
# print(type(b))

##################################################
def itoa(x):
    str = list()

    i, y = 0, 0
    while True:
        y = x % 10
        str.append(chr(y + ord("0")))
        x //= 10
        if x == 0:
            break
    str.reverse()
    str = "".join(str)
    return str

x = 123
print(x, type(x))
str1 = itoa(x)
print(str1, type(str1))