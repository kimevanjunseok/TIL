# My solution

def solution(str_list, n):
    str_list.sort()
    for i in range(len(str_list)-1, 0, -1):
        for j in range(i):
            if ord(str_list[j][n]) > ord(str_list[j+1][n]):
                str_list[j+1], str_list[j] = str_list[j], str_list[j+1]
    return str_list

###########################################################################

# Other

