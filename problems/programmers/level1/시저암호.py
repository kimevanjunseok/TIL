# My solution

def solution(s, n):
    answer = ''
    for i in s:
        if i != ' ':
            if 65 <= ord(i) <= 90:
                if ord(i) + n > 90:
                    answer += chr(ord(i) + n -26)
                else:
                    answer += chr(ord(i) + n)
            elif 97 <= ord(i) <= 122:
                if ord(i) + n > 122:
                    answer += chr(ord(i) + n -26)
                else:
                    answer += chr(ord(i) + n)
        else:
            answer += ' '
    return answer