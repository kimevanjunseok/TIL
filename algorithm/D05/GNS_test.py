import sys
sys.stdin = open("GNS_test_input.txt")

def dict_input(data):
    L_dict = {"ZRO": 0,
              "ONE": 0,
              "TWO": 0,
              "THR": 0,
              "FOR": 0,
              "FIV": 0,
              "SIX": 0,
              "SVN": 0,
              "EGT": 0,
              "NIN": 0}
    for i in data:
        L_dict[i] += 1

    return L_dict


T = int(input())

for N in range(1, T+1):
    result = ""
    temp = input()
    data = list(map(str, input().split()))
    data = dict_input(data)
    for key, value in data.items():
        result += f"{key} " * value
    print(f"#{N} {result.rstrip()}")