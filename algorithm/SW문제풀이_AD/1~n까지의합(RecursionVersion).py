def sums(x):
    if x == 1:
        return 1
    return x + sums(x - 1)

N = int(input())
print(sums(N))