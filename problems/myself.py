#1
# print("Hello World")

#2
# A = int(input('A: '))
# B = int(input('B: '))
# if A <= 0 | A >= 10:
#     print("A의 범위는 0과 10 사이 숫자입니다.")
# elif B <= 0 | B >= 10:
#     print("B의 범위는 0과 10 사이 숫자입니다.")
# else:
#    print(A+B)

# def two_times(x): return x*2
# A = list(map(two_times, [1, 2, 3, 4]))
# print(A)
# a = "Life is too short"
# b = a.split()
# print(b)

# a,b = list(map(int, input().split()))
# print(a+b)

#3
# A = int(input('A: '))
# B = int(input('B: '))
# if A <= 0 | A >= 10:
#     print("A의 범위는 0과 10 사이 숫자입니다.")
# elif B <= 0 | B >= 10:
#     print("B의 범위는 0과 10 사이 숫자입니다.")
# else:
#    print(A-B)


# A = int(input('A: '))
# B = int(input('B: '))
# if A <= 0 | A >= 10:
#     print("A의 범위는 0과 10 사이 숫자입니다.")
# elif B <= 0 | B >= 10:
#     print("B의 범위는 0과 10 사이 숫자입니다.")
# else:
#    print(A/B)

#4
# print("맞은 수: 123 \n아이디: junseok")

#5
# print('|\\_/|\n''|q p|   /}\n''( 0 )"""\\\n''|"^"`    |\n''||_/=\\\\__|')

#한수
# N = int(input())
# cnt = 99
# if N < 100:
#         print(N)
# else:
#         for i in range(100, N+1):
#                 n_1 = i // 100
#                 n_2 = (i % 100) // 10
#                 n_3 = i % 10
#                 if (n_1 - n_2) == (n_2 - n_3):
#                         cnt += 1
#         print(cnt)

#별찍기 -11
# N = int(input())
# List = []
# List_2 = []
# a = '  *  '
# b = ' * * '
# c = '*****'
# List_2.append(a)
# List_2.append(b)
# List_2.append(c)
# List.append(a)
# List.append(b)
# List.append(c)
# cnt = N // 3
# num = 0
# for i in range(N):
#     if i > 2:
#         x = List_2[num] + ' ' + List_2[num]
#         List.append(x)
#         num += 1
#         if num == 3:
#             num = 0
#             for k in range(len(List)):
#                 List_2.append(List[k].center(N*2-1))
#             for k in range(3):
#                 del List_2[k]
#                 print(k)
#     print(List[i].center(N*2-1))

# for i in range(6):
#     print(List_2[i])

# def my_bin(x):
#     L = []
#     while True:
#         if x == 1:
#             L.append(1)
#             break
#         if x % 2 == 1:
#             L.append(1)
#             x = x // 2
#         elif x % 2 == 0:
#             L.append(0)
#             x = x // 2
#     bin_num = ''
#     for i in L:
#         i = str(i)
#         bin_num += i
#     bin_num = "0b" + bin_num[::-1]
#     return bin_num

# print(my_bin(4096), my_bin(5))
# print(my_bin(4096) == bin(4096))
# print(123)

#OX
# N = int(input())
# count = 0
# while count != N:
#     score = list(input())
#     cnt_1 = 0
#     point = 0
#     for i in score:
#         if i == 'O':
#             cnt_1 += 1
#             point += cnt_1
#         else:
#             cnt_1 = 0
#     print(point)
#     count += 1

#음계
# num = list(map(int, input().split()))
# ascending = list(range(1, 9))
# descending = list(reversed(ascending))
# if num == ascending:
#     print('ascending')
# elif num == descending:
#     print('descending')
# else:
#     print('mixed')

#평균 점수10
# score = 0
# for i in range(5):
#     total = int(input())
#     if total < 40:
#         total = 40
#     score += total
# print(score//5)

#아스키코드
# n = input()
# print(ord(n))

#chr()

#알파벳 찾기
# S = input()
# alpa = {
#     'a' : -1,
#     'b' : -1,
#     'c' : -1,
#     'd' : -1,
#     'e' : -1,
#     'f' : -1,
#     'g' : -1,
#     'h' : -1,
#     'i' : -1,
#     'j' : -1,
#     'k' : -1,
#     'l' : -1,
#     'm' : -1,
#     'n' : -1,
#     'o' : -1,
#     'p' : -1,
#     'q' : -1,
#     'r' : -1,
#     's' : -1,
#     't' : -1,
#     'u' : -1,
#     'v' : -1,
#     'w' : -1,
#     'x' : -1,
#     'y' : -1,
#     'z' : -1,
# }
# t = ()
# for i in range(len(S)):
#     if S[i] != S[i-1]:
#         alpa[S[i]] = i
#     else:

# for value in alpa.values():
#     print(value, end=' ')

#카잉달력
# import sys
# def gcd(a, b):
#     mod = a % b
#     while mod > 0:
#         a = b
#         b = mod
#         mod = a % b
#     return b

# def lcm(a, b):
#     return (a*b) // gcd(a, b)

# N = int(sys.stdin.readline())
# for i in range(N):
#     M, N, x, y = map(int, sys.stdin.readline().split())  
#     a = b = 1
#     k = cnt = 0
#     if (M % 2 == 0 and N % 2 == 0 and (x + y) % 2 == 1) or (N == M and x != y):
#         print(-1)
#     elif M > N:
#         if (N == y) or (M == x and N == y):
#             print(lcm(x, y))
#         else:
#             while True:
#                 if b > N:
#                     b = b - N
#                 elif x <= y and b == y - x + 1:
#                     print(cnt + x)
#                     break
#                 elif x > y and b == y - x + 1 + N:
#                     print(cnt + x)
#                     break
#                 else:
#                     cnt += M
#                     b += (M - N)
#     elif M < N:
#         if (M == x) or (M == x and N == y):
#             print(lcm(y, x))
#         else:
#             while True:
#                 if b > M:
#                     b = b - M
#                 elif y <= x and b == x - y + 1:
#                     print(cnt + y)
#                     break
#                 elif y > x and b == x - y + 1 + M:
#                     print(cnt + y)
#                     break
#                 else:
#                     cnt += N
#                     b += (N - M)
#     elif M == N:
#         print(x)

# import sys
# def gcd(a, b):
#     mod = a % b
#     while mod > 0:
#         a = b
#         b = mod
#         mod = a % b
#     return b

# def lcm(a, b):
#     return (a*b) // gcd(a, b)
    
# N = int(sys.stdin.readline())
# for i in range(N):
#     M, N, x, y = map(int, sys.stdin.readline().split())  
#     a, b = M, N
#     k = cnt = 0
#     if (M % 2 == 0 and N % 2 == 0 and (x + y) % 2 == 1) or (N == M and x != y):
#         print(-1)
#     elif M > N:
#         if M == x and N == y:
#             print(lcm(x, y))
#         else:
#             if x < y:
#                 while True:
#                     if (cnt > 0) and (a - b == y - x):
#                         print(a+x)
#                         break
#                     elif a > b:
#                         b += N
#                     elif a < b:
#                         a += M
#                     cnt += 1
#             elif x > y:
#                 while True:
#                     if (cnt > 0) and (b - a == x - y):
#                         print(a+x)
#                         break
#                     elif a > b:
#                         b += N
#                     elif a < b:
#                         a += M
#                     cnt += 1
#     elif M < N:
#         if M == x and N == y:
#             print(lcm(y, x))
#         else:
#             if x < y:
#                 while True:
#                     if (cnt > 0) and (a - b == y - x):
#                         print(a+x)
#                         break
#                     elif a > b:
#                         b += N
#                     elif a < b:
#                         a += M
#                     cnt += 1
#             elif x > y:
#                 while True:
#                     if (cnt > 0) and (a - b == x - y):
#                         print(b+y)
#                         break
#                     elif a > b:
#                         b += N
#                     elif a < b:
#                         a += M
#                     cnt += 1
#     elif M == N:
#         print(x)

# 1로 만들기
# N = int(input())
# cnt = 0
# while True:
#     if N == 1:
#         print(cnt)
#         break
#     if N % 3 == 0:
#         N = N // 3
#     elif (N - 1) % 3 == 0:
#         N = N - 1    
#     elif N % 2 == 0:
#         N = N // 2
#     else:
#         N = N - 1
#     cnt += 1

# 소수 구하기
# N, M = input().split()
# N = int(N)
# if N == 1:
#     N = 2
# M = int(M)
# root_M = int(M**0.5)
# L = [True] * (M+1)
# for i in range(2, root_M + 1):
#     if L[i] == True:
#         for j in range(i+i, M+1, i ):
#             L[j] = False
# result = [i for i in range(N, M+1) if L[i] == True]
# for i in result:
#     print(i)

# def solution(n):
#     L = [True] * (n + 1)
#     M = int(n**0.5)
#     for i in range(2, M+1):
#         if L[i] == True:
#             for j in range(i+i, n+1 ,i):
#                 L[j] = False
#     return len([i for i in range(2, n+1) if L[i] == True])
# print(solution(100))

# def solution(seoul):
#     for i in range(len(seoul)):
#         if seoul[i] in 'Kim':
#             return f"김서방은 {i}에 있다"
# print(solution(['Jane','iu', 'Kim']))

# def solution(n):
#     L = []
#     for i in range(1, n+1):
#         if n % i == 0:
#             L.append(i)
#     return sum(L)
# print(solution(12))

# def solution(n):
#     s = ""
#     for i in range(1, n+1):
#         if i % 2 == 1:
#             s += "수"
#         else:
#             s += "박"
#     return s
# print(solution(5))

# 베르트랑 공준
# while True:
#     N = int(input())
#     if N == 0:
#         break
#     M = int((2*N)**0.5)
#     L = [True] * ((2*N)+1)
#     for i in range(2, M + 1):
#         if L[i] == True:
#             for j in range(i+i, (2*N)+1, i ):
#                 L[j] = False
#     result = [i for i in range(N+1, (2*N)+1) if L[i] == True]
#     print(len(result))

#
# def solution(a, b):
#     days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     weeks = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
#     day = sum(days[:a-1]) + int(b)
#     return weeks[day % 7]
# print(solution(5, 24))

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

# def solution(n):
#     L = []
#     for i in range(len(str(n))):
#         L.append(n%10)
#         n = n // 10
#     return sum(L)
# print(solution(123))

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

# def solution(phone_number):
#     answer = '*'*(len(phone_number)-4) + phone_number[-4:]
#     return answer
# s = '123456789'
# print(s[-4:])
# print(solution("027778888"))

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

# def solution(n):
#     n = n ** 0.5
#     if n - int(n) == 0:
#         return (n+1) ** 2
#     else:
#         return -1

# def solution(x, n):
#     answer = []
#     for i in range(n):
#         answer.append(x*(i+1))
#     return answer

# def solution(n):
#     answer = []
#     for i in str(n):
#         answer.append(int(i)) 
#     answer.reverse()
#     return answer

# def solution(arr):
#     answer = [arr[0]]
#     point = 0
#     for i in range(1, len(arr)):
#         if answer[point] != arr[i]:
#             answer.append(arr[i])
#             point += 1
#     return answer

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

####################################################3
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

# def solution(n, lost, reserve):
#     answer = [1]*(n+1)
#     for i in lost:
#         answer[i] = 0
#     for i in reserve:
#         answer[i] += 1
#     for i in lost:
#         if answer[i-1] == 2:
#             answer[i] += 1
#             answer[i-1] += -1
#         elif answer[i+1] == 2:
#             answer[i] += 1
#             answer[i+1] += -1
#     return answer

# print(solution(5, [2, 4], [1, 3, 5]))
