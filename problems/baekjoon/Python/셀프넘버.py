def func(n):
    if n == 0:
        return 0
    return n % 10 + func(n // 10)

L = []
for i in range(1, 10000):
    L.append(i + func(i))
    if i not in L:
        print(i)
