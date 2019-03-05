import sys
sys.stdin = open("사칙연산_input.txt")

T = 10

def uhh(x, y, z):
    if y == '-':
        return int(x) - int(z)
    elif y == '+':
        return int(x) + int(z)
    elif y == '/':
        return int(x) / int(z)
    elif y == '*':
        return int(x) * int(z)


for n in range(1, T+1):
    N = int(input())
    save = [[0, 0, 0] for i in range(N+1)]
    result = [0] * (N+1)
    for i in range(N):
        temp = input().split()
        result[int(temp[0])] = temp[1]
        save[int(temp[0])][0] = int(temp[0])
        if len(temp) > 2:
            if temp[2]:
                save[int(temp[0])][1] = int(temp[2])
            if temp[3]:
                save[int(temp[0])][2] = int(temp[3])

    for i in save[::-1]:
        if result[i[1]] and result[i[2]]:
            result[i[0]] = uhh(result[i[1]], result[i[0]], result[i[2]])


    print("#{0} {1}".format(n, int(result[1])))



