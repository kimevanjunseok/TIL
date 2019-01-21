#1
# N = int(input('입력 : '))
# if 1 <= N <= 100000:
#     for i in range(1, N+1):
#         print(i)
# else:
#     print("wrong number")

#2
# N = int(input('입력 : '))
# if 1 <= N <= 100000:
#     for i in range(N):
#         print(N-i)
# else:
#     print("wrong number")

#3
# N = int(input('입력 : '))
# for i in range(1, 10):
#     print(f'{N} * {i} = {N * i}')

#4
# N = int(input())
# star = "*"
# for i in range(1, N+1):
#     print(star*i)


#5
# N = int(input())
# for i in range(1, N+1):  
#     print(" "*(N-i) + "*"*(i))

#6
# N = int(input())
# for i in range(N+1):
#     print("*"*(N-i))

#7
# N = int(input())
# for i in range(N+1):
#     print(" "*i + "*"*(N-i))

#8
# x, y = input().split()
# x = int(x)
# y = int(y)
# jan = 31
# feb = 28 + jan
# mar = 31 + feb
# apr = 30 + mar
# may = 31 + apr
# jun = 30 + may
# jul = 31 + jun
# aug = 31 + jul
# seb = 30 + aug
# octo = 31 +seb
# nov = 30 + octo
# if x == 1:
#     day = y % 7
# elif x == 2:
#     day = (y + jan) % 7
# elif x == 3:
#     day = (y + feb) % 7
# elif x == 4:
#     day = (y + mar) % 7
# elif x == 5:
#     day = (y + apr) % 7
# elif x == 6:
#     day = (y + may) % 7
# elif x == 7:
#     day = (y + jun) % 7
# elif x == 8:
#     day = (y + jul) % 7
# elif x == 9:
#     day = (y + aug) % 7
# elif x == 10:
#     day = (y + seb) % 7
# elif x == 11:
#     day = (y + octo) % 7
# elif x == 12:
#     day = (y + nov) % 7

# if day == 0:
#     print('SUN')
# elif day == 1:
#     print('MON')
# elif day == 2:
#     print('TUE')
# elif day == 3:
#     print('WEB')
# elif day == 4:
#     print('THU')
# elif day == 5:
#     print('FRI')
# elif day == 6:
#     print('SAT')

# x, y = input().split()
# x = int(x)
# y = int(y)
# days = 0
# day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
# List = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
# for i in range(x-1):
#     days += day[i]
# days = (days + y) % 7
# print(List[days])

#9
# n = int(input())
# for i in range(1, n):
#     n += i
# print(n)

#10
# x = int(input())
# y = list(input())
# sum = 0
# for i in range(x):
#     sum += int(y[i])
# print(sum)

#11
# x = input()
# time = len(x) // 10
# for i in range(0, time+1):
#     print(x[:10])
#     x = list(x)
#     del x[:10]
#     x = "".join(x) #join은 리스트를 str로 변환

# a=input()
# for i in range(0,len(a),10): #range 3번쨰자리는 i의 변화량(10이면 i는 10씩 커짐)
#     print(a[i:i+10])

import sys
x = int(sys.stdin.readline())
for i in range(x):
    a, b = sys.stdin.readline().split()
    a = int(a)
    b = int(b)
    print(a+b)

#map 사용
n=int(input())
for i in range(n):
    print(sum(map(int, sys.stdin.readline().split())))