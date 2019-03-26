N = int(input())
arr = list(map(float, input().split()))
smart = 0
fool = 0
fool_max = 0
for i in range(len(arr)):
    if arr[i] >= 0:
        fool += arr[i]
    else:
        if fool + arr[i] > 0:
            fool += arr[i]
        else:
            fool = 0
    
    if fool_max < fool:
        fool_max = fool

    if arr[i] > 0:
        smart += arr[i]
if smart == 0:
    smart = max(arr)
if fool_max == 0:
    fool_max = max(arr)
print(f'{fool_max:0.0f} {smart:0.0f}')