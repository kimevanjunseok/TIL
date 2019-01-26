# (소팅 & 그리디) - O( nlogn )
def solution(l, v):
    v.sort()
    ans = max(v[0], l - v[-1])
    for i in range(1, len(v)):
        ans = max(ans, (v[i] - v[i-1] + 1)//2)
    return ans

# (이분탐색) - O( nlogn )
def solution(l, v):    
    n = len(v)
    answer = l
    v.sort()

    left, right = 0, l
    while(left <= right) :
        mid = (left + right) // 2

        # 맨 앞 가로등과 맨 뒤 가로등이 도로의 양 끝을 밝히는지 확인
        if v[0] - mid > 0 or v[n-1] + mid < l :
            left = mid + 1
            continue

        # 나머지 가로등으로 이분 탐색
        flag = False
        for i in range(1, n) :
            if v[i-1] + mid < v[i] - mid :
                flag = True
                break
        if flag :
            left = mid + 1
        else :
            answer = mid 
            right = mid - 1
    return answer