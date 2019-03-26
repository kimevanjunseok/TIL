N = int(input())
arr = [list(map(int, input().split())) for _ in range(6)]
number = [i[1] for i in arr]
max_length = max(number)
rounded = sum(number)
max_length_diff = (rounded - max_length*2)//2
arr = arr + arr
for i in range(3, len(arr)-3):
    if arr[i][1] == max_length:
        if arr[i+1][1] == max_length_diff:
            a = max_length - arr[i+2][1]
            b = max_length_diff - arr[i-1][1]
        else:
            a = max_length_diff - arr[i+1][1]
            b = max_length - arr[i-2][1]
area = max_length*max_length_diff - a*b
print(area*N)


