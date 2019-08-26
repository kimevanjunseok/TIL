def cal(x, food_times):
    sum_N = 0
    for i in food_times:
        if i >= x:
            sum_N += x
        else:
            sum_N += i

    return sum_N

def bin_search(start, end, food_times, k):
    save = 0
    while start <= end:
        mid = (start + end) // 2
        com = cal(mid, food_times)
        if com < k:
            start = mid + 1
            save = mid
        elif com == k:
            return mid, "true"
        else:
            end = mid - 1
    return save, "false"

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    else:
        result = 0
        max_n = max(food_times)
        judge = bin_search(0, max_n, food_times, k)
        if judge[1] == "true":
            for i in range(len(food_times)):
                if food_times[i] > judge[0]:
                    result = i + 1
                    break
        else:
            for i in range(len(food_times)):
                if food_times[i] > judge[0]:
                    k -= judge[0]
                    food_times[i] -= judge[0]
                else:
                    k -= food_times[i]
                    food_times[i] = 0
            
            for i in range(len(food_times)):
                if food_times[i] > 0:
                    food_times[i] -= 1
                    k -= 1
                
                if k == 0:
                    for j in range(i+1, len(food_times)):
                        if food_times[j] > 0:
                            result = j + 1
                            break
                    
                    if not result:
                        for j in range(len(food_times)):
                            if food_times[j] > 0:
                                result = j + 1
                                break
                    break
            

        return result

if __name__ == "__main__":
    food_tiems = [2, 0, 0, 0]
    k = 1
    print(solution(food_tiems, k))