time = 0
for _ in range(5):
    N, M = map(float, input().split())
    if M - N - 1 > 0:
        if M - N - 1 >= 4:
            time += 4
        else:
            time += M - N - 1
money = int((time * 5000) * 2)
if 5 < time < 15:
    print(money)
else:
    if time <= 5:
        print(int(money*1.05)) 
    else: 
        print(int(money*0.95))