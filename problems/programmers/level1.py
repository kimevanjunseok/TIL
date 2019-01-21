# 짝수와 홀수
# def solution(num):
#     if num % 2 == 0:
#         return 'Even'
#     else:
#         return 'Odd'

# 소수 찾기
# def solution(n):
#     L = [True] * (n + 1)
#     M = int(n**0.5)
#     for i in range(2, M+1):
#         if L[i] == True:
#             for j in range(i+i, n+1 ,i):
#                 L[j] = False
#     return len([i for i in range(2, n+1) if L[i] == True])

# 서울에서 김서방 찾기
# def solution(seoul):
#     for i in range(len(seoul)):
#         if seoul[i] in 'Kim':
#             return f"김서방은 {i}에 있다"

# 수박수박수박수박수박수?
# def solution(n):
#     s = ""
#     for i in range(1, n+1):
#         if i % 2 == 1:
#             s += "수"
#         else:
#             s += "박"
#     return s

# 약수의 합
# def solution(n):
#     L = []
#     for i in range(1, n+1):
#         if n % i == 0:
#             L.append(i)
#     return sum(L)

# 최대공약수와 최소공배수
# def solution(n, m):
#     a = max(n, m)
#     b = min(n, m)
#     num = a % b
#     while num > 0:
#         a = b
#         b = num
#         num = a % b
#     return [b, (n * m) // b]

# 평균구하기
# def solution(arr):
#     answer = sum(arr) / len(arr)
#     return answer

# 직사각형 별찍기
# a, b = map(int, input().split())
# print(("*" * a + "\n")*b)

# 행렬의 덧셈
# def solution(arr1, arr2):
#     answer = []
#     for i in range(len(arr1)):
#         result = []
#         for j in range(len(arr1[i])):
#             result.append(arr1[i][j] + arr2[i][j]) 
#         answer.append(result)
#     return answer

# 2016년
# def solution(a, b):
#     days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     weeks = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
#     day = sum(days[:a-1]) + int(b)
#     return weeks[day % 7]
# print(solution(5, 24))

# 제일 작은 수 제거하기
# def solution(arr):
#     min_num = arr[0]
#     if len(arr) > 1:
#         for i in range(len(arr)):
#             if min_num > arr[i]:
#                 min_num = arr[i]
#         arr.remove(min_num)
#         return  arr
#     else:
#         return [-1]
# print(solution([4, 3, 2, 1]))
# print(solution([10]))

# 자릿수 더하기
# def solution(n):
#     L = []
#     for i in range(len(str(n))):
#         L.append(n%10)
#         n = n // 10
#     return sum(L)
# print(solution(123))

# 콜라츠 추측
# def solution(num):
#     cnt = 0
#     while True:
#         if cnt == 500:
#             return -1
#         elif num == 1:
#             return cnt
#         elif num % 2 == 0:
#             num = num // 2
#             cnt += 1
#         elif num % 2 != 0:
#             num = num*3 + 1
#             cnt += 1
# print(solution(626331))

# 핸드폰 번호 가리기
# def solution(phone_number):
#     answer = '*'*(len(phone_number)-4) + phone_number[-4:]
#     return answer
# s = '123456789'
# print(s[-4:])
# print(solution("027778888"))

# 하샤드 수
# def solution(x):
#     L = []
#     calc = x
#     for i in range(len(str(calc))):
#         L.append(calc % 10)
#         calc = calc // 10
#     print(sum(L))
#     if x % sum(L) == 0:
#         return True
#     else:
#         return False
# print(solution(11))

# 정수 제곱근 판별
# def solution(n):
#     n = n ** 0.5
#     if n - int(n) == 0:
#         return (n+1) ** 2
#     else:
#         return -1

# x만큼 간격이 있는 n개의 숫자
# def solution(x, n):
#     answer = []
#     for i in range(n):
#         answer.append(x*(i+1))
#     return answer

# 자연수 뒤집어 배열로 만들기
# def solution(n):
#     answer = []
#     for i in str(n):
#         answer.append(int(i)) 
#     answer.reverse()
#     return answer

# 같은 숫자는 싫어
# def solution(arr):
#     answer = [arr[0]]
#     point = 0
#     for i in range(1, len(arr)):
#         if answer[point] != arr[i]:
#             answer.append(arr[i])
#             point += 1
#     return answer

# 정수 내림차순으로 배치하기
# def solution(n):
#     L = [i for i in str(n)]
#     L.sort()
#     L.reverse()
#     answer = ''
#     for i in L:
#         answer += str(i)
#     return int(answer)
# print(solution(118372))
    
# 이상한 문자 만들기
# def solution(s):
#     answer = ''
#     cnt = 1
#     for i in s:
#         cnt += 1
#         if i == ' ':
#             cnt = 1
#         if cnt % 2 == 0:
#             answer += i.upper()
#         else:
#             answer += i.lower()
#     return answer
# print(solution('try  hello world'))

#예산
# def solution(d, budget):
#     d.sort()
#     for i in range(len(d)):
#         if budget >= sum(d):
#             answer = len(d)
#         elif budget < sum(d[:i+1]):
#             answer = i
#             break
#     return answer
# print(solution([1, 3, 2, 5, 4], 9))
# print(solution([2, 2, 3, 3], 10))

# 시저 암호
# def solution(s, n):
#     answer = ''
#     for i in s:
#         if i != ' ':
#             if 65 <= ord(i) <= 90:
#                 if ord(i) + n > 90:
#                     answer += chr(ord(i) + n -26)
#                 else:
#                     answer += chr(ord(i) + n)
#             elif 97 <= ord(i) <= 122:
#                 if ord(i) + n > 122:
#                     answer += chr(ord(i) + n -26)
#                 else:
#                     answer += chr(ord(i) + n)
#         else:
#             answer += ' '
#     return answer
# print(solution("AB", 1))
# print(solution("z", 1))
# print(solution("a B z", 4))

# 문자열을 정수로 바꾸기
# def solution(s):
#     return int(s)

# 가운데 글자 가져오기
# def solution(s):
#     answer = ''
#     if len(s) % 2 != 0:
#         answer = s[len(s)//2]
#     else:
#         answer = s[len(s)//2 -1] + s[len(s)//2]
#     return answer
# print(solution("abcde"))
# print(solution("qwer"))

# 문자열 다루기 기본
# def solution(s):
#     L = list(range(10)) * 6
#     if len(s) == 4:
#         for i in L:
#             s = s.replace(str(i), '')
#     else:
#         return False
#     return not s

# 두 정수 사이의 합
# def solution(a, b):
#     M = max(a, b)
#     N = min(a, b)
#     answer = 0
#     for i in range(N, M+1):
#         answer += i
#     return answer
# print(solution(3, 5))
# print(solution(3, 3))
# print(solution(5, 3))

# 나누어 떨어지는 숫자 배열
# def solution(arr, divisor):
#     answer = []
#     for i in arr:
#         if i % divisor == 0:
#             answer.append(i)
            
#     if answer:
#         answer.sort()
#     else:
#         answer.append(-1)
#     return answer

# 문자열 내 p와 y의 개수
# def solution(s):
#     s = s.lower()
#     cnt_p, cnt_y = 0, 0
#     for i in s:
#         if i == "p":
#             cnt_p += 1
#         elif i == "y":
#             cnt_y += 1
#     return cnt_p == cnt_y

# def solution(s):
#     return s.lower().count('p') == s.lower().count('y') 

# print(solution('p  PoooyY'))
# print(solution('Pyy'))
# print(solution('oo  o'))

# 문자열 내림차순으로 배치하기
# def solution(s):
#     L = []
#     for i in s:
#         L.append(ord(i))
#     L.sort()
#     L.reverse()
#     answer = ''
#     for i in L:
#         answer += chr(i)
#     return answer

# def solution(s):
#     return ''.join(sorted(s, reverse=True))

# print(solution("Zbcdefg"))

# 문자열 내 마음대로 정렬하기(문자열도 sort사용가능)
# def solution(str_list, n):
#     str_list.sort()
#     for i in range(len(str_list)-1, 0, -1):
#         for j in range(i):
#             if ord(str_list[j][n]) > ord(str_list[j+1][n]):
#                 str_list[j+1], str_list[j] = str_list[j], str_list[j+1]
#     return str_list
# print(solution(["sun", "bed", "car"], 1))
# print(solution(["abce", "abcd", "cdx"], 2))

# 완주하지 못한 선수
# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
#     for i in range(len(completion)):
#         if participant[i] != completion[i]:
#             return participant[i]
#     return participant[-1]
# print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
# print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))

# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
#     for p, c in zip(participant, completion):
#         if p != c:
#             return p
#     return participant[-1]

# import collections
# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]

# K번째수
# def solution(array, commands):
#     answer = []
#     array_smaple = array
#     for i in commands:
#         sort_list = array_smaple[i[0]-1:i[1]]
#         sort_list.sort()
#         answer.append(sort_list[i[2]-1])
#         sort_list = []
#         array_smaple = array
#     return answer
# print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

# def solution(array, commands):
#     answer = []
#     for com in commands:
#         answer.append(sorted(array[com[0]-1:com[1]])[com[2]-1])
#     return answer

# 모의고사
# def solution(answers):
#     frist = [1, 2, 3, 4, 5]*(len(answers) // 5 + 1)
#     second = [2, 1, 2, 3, 2, 4, 2, 5]*(len(answers) // 8 + 1)
#     third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*(len(answers) // 10 + 1)
#     answer = []
#     cnt_first, cnt_second, cnt_third = 0, 0, 0
#     for i in range(len(answers)):
#         if answers[i] == frist[i]:
#             cnt_first += 1
        
#         if answers[i] == second[i]:
#             cnt_second += 1
        
#         if answers[i] == third[i]:
#             cnt_third += 1

#     if cnt_first > cnt_second and cnt_first > cnt_third:
#         answer = [1]
#     elif cnt_second > cnt_first and cnt_second > cnt_third:
#         answer = [2]
#     elif cnt_third > cnt_first and cnt_third > cnt_second:
#         answer = [3]
#     elif cnt_first == cnt_second and cnt_first > cnt_third:
#         answer = [1, 2]
#     elif cnt_first == cnt_third and cnt_first > cnt_second:
#         answer = [1, 3]
#     elif cnt_second == cnt_third and cnt_second > cnt_first:
#         answer = [2, 3]
#     else:
#          answer = [1,2,3]
#     return answer
# print(solution([1,2,3,4,5]))
# print(solution([1,3,2,4,2]))

# 체육복
# def solution(n, lost, reserve):
#     answer = [1]*(n+2)
#     answer[n+1] = 0
#     answer[0] = 0
#     cnt = 0

#     for i in lost:
#         answer[i] += -1
#     for i in reserve:
#         answer[i] += 1
#     for i in range(2, n-1):
#         if answer[i] == 0:
#             if answer[i-1] == 2:
#                 answer[i] += 1
#                 answer[i-1] += -1
#             elif answer[i+1] == 2:
#                 answer[i] += 1
#                 answer[i+1] += -1
#     for i in answer:
#         if i >= 1:
#             cnt += 1

#     return cnt

# print(solution(5, [2, 4], [1, 3, 5]))
# print(solution(5, [2,4], [3]))
# print(solution(5, [2, 4, 5], [1, 4]))
# print(solution(5, [5], [3]))

# 
a = "//"
b = "3"
c = "4"

print(type(+))