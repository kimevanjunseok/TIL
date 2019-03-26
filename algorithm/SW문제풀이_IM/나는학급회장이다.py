N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

saram_1 = []
saram_2 = []
saram_3 = []
for i in arr:
    saram_1.append(i[0])
    saram_2.append(i[1])
    saram_3.append(i[2])

if sum(saram_1) > sum(saram_2) and sum(saram_1) > sum(saram_3):
    print(f'1 {sum(saram_1)}')
elif sum(saram_2) > sum(saram_1) and sum(saram_2) > sum(saram_3):
    print(f'2 {sum(saram_2)}')
elif sum(saram_3) > sum(saram_1) and sum(saram_3) > sum(saram_2):
        print(f'3 {sum(saram_3)}')
elif sum(saram_1) == sum(saram_2) and sum(saram_1) == sum(saram_3):
    if saram_1.count(3) > saram_2.count(3) and saram_1.count(3) > saram_3.count(3):
        print(f'1 {sum(saram_1)}')
    elif saram_2.count(3) > saram_1.count(3) and saram_2.count(3) > saram_3.count(3):
        print(f'2 {sum(saram_2)}')
    elif saram_3.count(3) > saram_1.count(3) and saram_3.count(3) > saram_2.count(3):
        print(f'3 {sum(saram_3)}')
    elif saram_1.count(3) == saram_2.count(3) and saram_1.count(3) == saram_3.count(3):
        if saram_1.count(2) > saram_2.count(2) and saram_1.count(2) > saram_3.count(2):
            print(f'1 {sum(saram_1)}')
        elif saram_2.count(2) > saram_1.count(2) and saram_2.count(2) > saram_3.count(2):
            print(f'2 {sum(saram_2)}')
        elif saram_3.count(2) > saram_1.count(2) and saram_3.count(2) > saram_2.count(2):
            print(f'3 {sum(saram_3)}')
        elif saram_1.count(2) == saram_2.count(2) and saram_1.count(2) == saram_3.count(2):
            if saram_1.count(1) > saram_2.count(1) and saram_1.count(1) > saram_3.count(1):
                print(f'1 {sum(saram_1)}')
            elif saram_2.count(1) > saram_1.count(1) and saram_2.count(1) > saram_3.count(1):
                print(f'2 {sum(saram_2)}')
            elif saram_3.count(1) > saram_1.count(1) and saram_3.count(1) > saram_2.count(1):
                print(f'3 {sum(saram_3)}')
            else:
                print(f'0 {sum(saram_1)}')
        elif saram_1.count(2) == saram_2.count(2):
            if saram_1.count(1) > saram_2.count(1):
                print(f'1 {sum(saram_1)}')
            elif saram_1.count(1) < saram_2.count(1):
                print(f'2 {sum(saram_2)}')
            else:
                print(f'0 {sum(saram_1)}')
        elif saram_1.count(2) == saram_3.count(2):
            if saram_1.count(1) > saram_3.count(1):
                print(f'1 {sum(saram_1)}')
            elif saram_1.count(1) < saram_3.count(1):
                print(f'3 {sum(saram_3)}')
            else:
                print(f'0 {sum(saram_1)}')
        elif saram_2.count(2) == saram_3.count(2):
            if saram_2.count(1) > saram_3.count(1):
                print(f'2 {sum(saram_2)}')
            elif saram_2.count(1) < saram_3.count(1):
                print(f'3 {sum(saram_3)}')
            else:
                print(f'0 {sum(saram_2)}')
elif sum(saram_1) == sum(saram_2):
    if saram_1.count(3) > saram_2.count(3):
        print(f'1 {sum(saram_1)}')
    elif saram_1.count(3) < saram_2.count(3):
        print(f'2 {sum(saram_2)}')
    else:
        if saram_1.count(2) > saram_2.count(2):
            print(f'1 {sum(saram_1)}')
        elif saram_1.count(2) < saram_2.count(2):
            print(f'2 {sum(saram_2)}')
        else:
            if saram_1.count(1) > saram_2.count(1):
                print(f'1 {sum(saram_1)}')
            elif saram_1.count(1) < saram_2.count(1):
                print(f'2 {sum(saram_2)}')
            else:
                print(f'0 {sum(saram_1)}')
elif sum(saram_1) == sum(saram_3):
    if saram_1.count(3) > saram_3.count(3):
        print(f'1 {sum(saram_1)}')
    elif saram_1.count(3) < saram_3.count(3):
        print(f'3 {sum(saram_3)}')
    else:
        if saram_1.count(2) > saram_3.count(2):
            print(f'1 {sum(saram_1)}')
        elif saram_1.count(2) < saram_3.count(2):
            print(f'3 {sum(saram_3)}')
        else:
            if saram_1.count(1) > saram_3.count(1):
                print(f'1 {sum(saram_1)}')
            elif saram_1.count(1) < saram_3.count(1):
                print(f'3 {sum(saram_3)}')
            else:
                print(f'0 {sum(saram_1)}')
elif sum(saram_2) == sum(saram_3):
    if saram_2.count(3) > saram_3.count(3):
        print(f'2 {sum(saram_2)}')
    elif saram_2.count(3) < saram_3.count(3):
        print(f'3 {sum(saram_3)}')
    else:
        if saram_2.count(2) > saram_3.count(2):
            print(f'2 {sum(saram_2)}')
        elif saram_2.count(2) < saram_3.count(2):
            print(f'3 {sum(saram_3)}')
        else:
            if saram_2.count(1) > saram_3.count(1):
                print(f'2 {sum(saram_2)}')
            elif saram_2.count(1) < saram_3.count(1):
                print(f'3 {sum(saram_3)}')
            else:
                print(f'0 {sum(saram_2)}')
            