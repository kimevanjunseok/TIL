def solution(n):
    def bin(x):
        if x == 1:
            return "1"
        elif x == 0:
            return ""
        return str(x%2) + bin(x//2)
    answer = bin(n).count("1")
    while True:
        n += 1
        if answer == bin(n).count("1"):
            break
    return n