import sys
sys.stdin = open("정식이의은행업무_input.txt")

T = int(input())

for n in range(1, T+1):
    num_2 = list(input())
    num_3 = list(input())
    num = []
    result = 0
    for i in range(len(num_2)):
        if num_2[i] == "1":
            num_2[i] = "0"
            num.append(int("".join(num_2), 2))
            num_2[i] = "1"

        else:
            num_2[i] = "1"
            num.append(int("".join(num_2), 2))
            num_2[i] = "0"

    for i in range(len(num_3)):
        if num_3[i] == "0":
            num_3[i] = "1"
            if int("".join(num_3), 3) in num:
                result = int("".join(num_3), 3)
                break
            else:
                num_3[i] = "0"
                num_3[i] = "2"
                if int("".join(num_3), 3) in num:
                    result = int("".join(num_3), 3)
                    break
                else:
                    num_3[i] = "0"

        elif num_3[i] == "1":
            num_3[i] = "0"
            if int("".join(num_3), 3) in num:
                result = int("".join(num_3), 3)
                break
            else:
                num_3[i] = "1"
                num_3[i] = "2"
                if int("".join(num_3), 3) in num:
                    result = int("".join(num_3), 3)
                    break
                else:
                    num_3[i] = "1"
        elif num_3[i] == "2":
            num_3[i] = "0"
            if int("".join(num_3), 3) in num:
                result = int("".join(num_3), 3)
                break
            else:
                num_3[i] = "2"
                num_3[i] = "1"
                if int("".join(num_3), 3) in num:
                    result = int("".join(num_3), 3)
                    break
                else:
                    num_3[i] = "2"

    print("#{0} {1}".format(n, result))
