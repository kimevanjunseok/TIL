# My solution

def solution(arr):
    min_num = arr[0]
    if len(arr) > 1:
        for i in range(len(arr)):
            if min_num > arr[i]:
                min_num = arr[i]
        arr.remove(min_num)
        return  arr
    else:
        return [-1]