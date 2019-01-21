#1
# score = int(input())
# if 90 <= score <= 100:
#     print('A')
# elif 80 <= score < 90:
#     print('B')
# elif 70 <= score < 80:
#     print('C')
# elif 60 <= score < 70:
#     print('D')
# else:
#     print('F')

#2
# A, B, C = map(int, input().split())
# if A == B:
#     print(A)
# elif B == C:
#     print(B)
# elif A == C:
#     print(C)
# elif A > B:
#     if A > C:
#         if B > C:
#             print(B)
#         else:
#             print(C)
#     else:
#         print(A)
# else:
#     if B > C:
#         if A > C:
#             print(A)
#         else:
#             print(C)
#     else:
#         print(B)

# A, B, C = map(int, input().split())
# if (A > B and C > A) or (A > C and B > A) or A == B or A == C:
#     print(A)
# elif (A > B and B > C) or (C > B and B > A) or B == C:
#     print(B)
# else:
#     print(C)

# A = list(map(int, input().split()))
# A.sort()
# print(A[1])

#3
# x, y = map(int, input().split())
# z = list(map(int, input().split()))
# for i in range(x):
#     if z[i] < y:
#         print(z[i], end = ' ')

#4
# N = int(input())
# score = list(map(int, input().split()))
# score.sort()
# total = 0
# for i in range(N):
#     total += (score[i] / score[N-1]) * 100
# print(total / N)

# N = int(input())
# score = list(map(int, input().split()))
# print(sum(score)/max(score)*100/N)

#5
# N = int(input())
# total = []
# for i in range(N):
#     count = 0
#     score = list(map(int, input().split()))
#     sum_score = 0
#     for j in range(1, len(score)):
#         sum_score += score[j]
#     aver_score = sum_score / score[0]
#     for k in range(1, len(score)):
#         if aver_score < score[k]:
#             count += 1  
#     total.append(format(count / score[0] * 100, '.3f')+'%')
# for i in range(len(total)):
#     print(total[i])

#6
N = int(input())
count = 1
N_nd = N
while True:
    if N_nd >= 10:
        ten_N = N_nd // 10
        one_N = N_nd % 10
        tenone_N = N_nd // 10 + N_nd % 10
        N_nd = (one_N * 10) + (tenone_N % 10)
        if N == N_nd: break   
    else:
        N_nd = (N_nd * 10) + N_nd
        if N == N_nd: break 
    count += 1
print(count)
