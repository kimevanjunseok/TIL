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
import sys
N = int(sys.stdin.readline())
k = a = b = 0
for i in range(N):
    M, N, x, y = map(int, sys.stdin.readline().split())  
    if (M % 2 == 0 and N % 2 == 0 and (x + y) % 2 == 1) or (N == M and x != y):
        print(-1)
    else:    
        while True:
            a += 1
            b += 1
            if a > M and b > N:
                a = b = 1
            elif a > M:
                a = 1
            elif b > N:
                b = 1
            elif a == x and b == y:
                k += 1
                print(k)
                break 
            k += 1
        k = a = b = 0   

# import sys
# N = int(sys.stdin.readline())
# cnt = 0
# for i in range(N):
#     M, N, x, y = map(int, sys.stdin.readline().split())  
#     a = 1
#     b = 1
#     if (M % 2 == 0 and N % 2 == 0 and (x + y) % 2 == 1) or (N == M and x != y):
#         print(-1)
#         break
#     elif M > N:
#         while True:
#             if b > N:
#                 b = b - N
#             elif x <= y and b == y - x + 1:
#                 print(cnt + x)
#                 break
#             elif x > y and b == y - x + 1 + N:
#                 print(cnt + x)
#                 break
#             else:
#                 cnt += M
#                 b += (M - N)
#     elif M < N:
#         while True:
#             if b > M:
#                 b = b - M
#             elif y <= x and b == x - y + 1:
#                 print(cnt + y)
#                 break
#             elif y > x and b == x - y + 1 + M:
#                 print(cnt + y)
#                 break
#             else:
#                 cnt += N
#                 b += (N - M)