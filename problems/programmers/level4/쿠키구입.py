def solution(cookie):
    stand = 0
    max_n = 0
    while stand < len(cookie)-1:
        left = stand
        right = stand+1
        left_v = cookie[left]
        right_v = cookie[right]
        while True:
            if left_v == right_v:
                if max_n < left_v:
                    max_n = left_v
                
                if right + 1 < len(cookie) and left - 1 >= 0:
                    right += 1
                    right_v += cookie[right]
                    left += -1
                    left_v += cookie[left]
                else:
                    break

            elif left_v < right_v:
                if left - 1 >= 0:
                    left += -1
                    left_v += cookie[left]
                else:
                    break

            elif left_v > right_v:
                if right + 1 < len(cookie):
                    right += 1
                    right_v += cookie[right]
                else:
                    break
        stand += 1
        
    return max_n

if __name__ == "__main__":
    cookie = [[1, 1, 2, 3], [1, 2, 4, 5]]
    for i in range(2):
        print(solution(cookie[i]))