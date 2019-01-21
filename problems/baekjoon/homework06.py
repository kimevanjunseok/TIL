#단어의 개수
# N = list(input().split())
# print(len())

#숫자의 개수
# A = int(input())
# B = int(input())
# C = int(input())
# n = str(A*B*C)
# List = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# for i in range(len(n)):
#     if n[i] == '0':
#         List[0] += 1
#     elif n[i] == '1':
#         List[1] += 1
#     elif n[i] == '2':
#         List[2] += 1
#     elif n[i] == '3':
#         List[3] += 1
#     elif n[i] == '4':
#         List[4] += 1
#     elif n[i] == '5':
#         List[5] += 1
#     elif n[i] == '6':
#         List[6] += 1
#     elif n[i] == '7':
#         List[7] += 1
#     elif n[i] == '8':
#         List[8] += 1
#     else:
#         List[9] += 1
# for i in range(len(List)):
#     print(List[i])

#OX퀴즈
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