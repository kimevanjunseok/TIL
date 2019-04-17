def solution(n):
    def three(x):
        if x == 0:
            return ""

        if x % 3 == 0:
            x = x // 3 - 1
            return three(x) + "4"
        elif x % 3 == 1:
            x = x // 3
            return three(x) + "1"
        elif x % 3 == 2:
            x = x // 3
            return three(x) + "2"

    a = three(n)
    return a