# My solution

def solution(s):
    s = s + " "
    String = ""
    buho = 1
    L = []
    for i in range(len(s)):
        if s[i] == "-":
            buho = -1
        elif s[i] == " ":
            L.append(buho*int(String))
            String = ""
            buho = 1
        else:
            String += s[i]

    return f"{min(L)} {max(L)}"