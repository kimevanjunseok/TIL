def solution(arr):
    def lcm(x, y, z):
        return (x*y)//z
    def gcm(x, y):
        while x:
            x, y = y%x ,x
        return y
    answer = lcm(arr[-2], arr[-1], gcm(arr[-2], arr[-1]))
    for i in range(len(arr)-3, -1, -1):
        answer = lcm(arr[i], answer, gcm(arr[i], answer))
    return answer