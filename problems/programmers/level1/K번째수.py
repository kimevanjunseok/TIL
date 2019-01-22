#My solution

def solution(array, commands):
    answer = []
    array_smaple = array
    for i in commands:
        sort_list = array_smaple[i[0]-1:i[1]]
        sort_list.sort()
        answer.append(sort_list[i[2]-1])
        sort_list = []
        array_smaple = array
    return answer

#################################################

# Other

def solution(array, commands):
    answer = []
    for i in commands:
        answer.append(sorted(array[i[0]-1:i[1]])[i[2]-1])
    return answer
