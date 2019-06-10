import sys
sys.stdin = open("컨테이너운반_input.txt")

T = int(input())

for n in range(1, T+1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    w.sort(reverse=True)
    t.sort(reverse=True)
    sums = 0
    for i in range(len(t)):
        while w:
            v = w.pop(0)
            if t[i] >= v:
                sums += v
                break

    print("#{0} {1}".format(n, sums))