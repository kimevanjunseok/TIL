def copy(L):
    T = ["0"] * len(L)
    for i in range(len(L)):
        T[i] = L[i]
    return T


def solution(numbers):
    x = int("".join(sorted(list(numbers), reverse=True)))
    T = [True] * (x + 1)
    save = 0
    for i in range(2, int((x) ** 0.5) + 1):
        if T[i]:
            for j in range(i + i, x + 1, i):
                T[j] = False
    for i in range(2, x + 1):
        if T[i]:
            L = copy(numbers)
            C = list(str(i))
            cnt = 0
            for i in C:
                if i in L:
                    L.remove(i)
                    cnt += 1
            if cnt == len(C):
                save += 1

    return save