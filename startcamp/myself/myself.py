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
N = int(input())
cnt = 99
if N < 100:
        print(N)
else:
        for i in range(100, N+1):
                n_1 = i // 100
                n_2 = (i % 100) // 10
                n_3 = i % 10
                if (n_1 - n_2) == (n_2 - n_3):
                        cnt += 1
        print(cnt)

#별찍기 -11
