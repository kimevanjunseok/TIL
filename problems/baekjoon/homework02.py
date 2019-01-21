#1
# A = int(input())
# B = int(input())
# if A <= 0 or 10 <= A:
#     print("A 범위 오류")
# elif B <= 0 or 10 <= B:
#     print("B 범위 오류")
# else:
#     print(A+B)

#2
# A = int(input())
# B = int(input())
# if A <= 0 or 10 <= A:
#     print("A 범위 오류")
# elif B <= 0 or 10 <= B:
#     print("B 범위 오류")
# else:
#     print(A-B)

#3
# A, B = input().split()
# A = int(A)
# B = int(B)
# if A <= 0 or 10 <= A:
#     print("A 범위 오류")
# elif B <= 0 or 10 <= B:
#     print("B 범위 오류")
# else:
#     print(A*B)

#4
# A, B = input('A, B의 값 입력 : ').split() #split 사용하면 변수 2개입력가능(enter대신 space bar)
# A = int(A)
# B = int(B)
# if A <= 0 or 10 <= A:
#     print("A 범위 오류")
# elif B <= 0 or 10 <= B:
#     print("B 범위 오류")
# else:
#     print(round(A/B, 9)) # round 사용하면 소수점 반올림 가능

# A, B = input().split()
# A = int(A)
# B = int(B)
# if A <= 0 or 10 <= A:
#     print("A 범위 오류")
# elif B <= 0 or 10 <= B:
#     print("B 범위 오류")
# else:
#     print(A/B)

#5
# A, B = input('A, B의 값 입력 : ').split()
# A = int(A)
# B = int(B)
# if A < 1 or 10000 < A:
#     print("A 범위 오류")
# elif B < 1 or 10000 < B:
#     print("B 범위 오류")
# else:
#     print(f'{A+B}\n' f'{A-B}\n' f'{A*B}\n' f'{A//B}\n' f'{A%B}')

#6
# A, B, C = input('A, B, C의 값 입력 : ').split()
# A = int(A)
# B = int(B)
# C = int(C)
# if A < 2 or 10000 < A:
#     print("A 범위 오류")
# elif B < 2 or 10000 < B:
#     print("B 범위 오류")
# elif C < 2 or 10000 < C:
#     print("C 범위 오류")
# else:
#     print((A+B)%C)
#     print((A%C+B%C)%C)
#     print((A*B)%C)
#     print((A%C*B%C)%C)

#7
# A = int(input('A 입력 : '))
# B = int(input('B 입력 : '))
# if 0 < A < 10 and 0 < B < 10:
#     print(A+B)
# else:
#     print("wrong number")

#8
# N = int(input())
# if N == 4 or N == 7:
#     print('-1')
# elif N % 5 == 0:
#     number = N // 5
#     print(number)
# elif N % 5 == 1:
#     number = N // 5 + 1
#     print(number)
# elif N % 5 == 4:
#     number = N // 5 + 2
#     print(number)
# elif N % 5 == 3:
#     number = N // 5 + 1
#     print(number)
# else:
#     number = N // 5 + 2
#     print(number)

#map 사용법
# a, b = map(int, input().split())
# print(a+b)