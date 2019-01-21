#아스키코드
# n = input()
# print(ord(n))

#chr()

#알파벳 찾기

# from string import ascii_lowercase
# from string import ascii_uppercase
# print(ascii_uppercase)
# print(ascii_lowercase)

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
# count = 0
# for i in S:
#     if alpa[i] == -1:
#         alpa[i] = count
#         count += 1
#     else:
#         count += 1
# for key in alpa.keys():
#     print(alpa[key], end = " ")

#문자열 반복
# S = int(input())
# for i in range(S):
#     R = input().split()
#     for j in R[1]:
#         j = j * int(R[0])
#         print(j, end='')
#     print()

#단어공부
# S = input().upper()
# set_S = set(S)
# count = 0
# list_count = 0
# L = []
# number = 0
# for i in set_S:
#     for j in S:
#         if i == j:
#             count += 1
#     L.append(count)
#     if number <= L[list_count]:  
#         number = L[list_count]        
#         str_save = i
#     list_count += 1
#     count = 0
# L.sort()
# L.reverse()
# if len(L) == 1:
#     print(str_save)
# elif L[0] == L[1]:
#     print('?')
# else:
#     print(str_save)

#그룹 단어 체커
# N = int(input())
# count = 0
# cnt_con = 0
# for i in range(N):
#     W = input()
#     W = list(W)
#     S = W[0]
#     for j in range(1, len(W)):
#         if S != W[j]:
#             if W[j-1] in W[j+1:]:
#                 count += 1
#         S = W[j]
#     if count == 0:
#         cnt_con += 1
#     count = 0
# print(cnt_con)

# N = input()
# print(list(N))

#상수
# first_N, second_N = input().split()
# first_N = first_N[::-1]
# second_N = second_N[::-1]
# if first_N > second_N:
#     print(first_N)
# else:
#     print(second_N)

#다이얼
# N = input()
# count = 0
# for_count = 3
# List = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# for i in range(len(N)):
#     for j in range(len(List)):
#         if N[i] in List[j]:
#             count += for_count
#         for_count += 1
#     for_count = 3
# print(count)

#크로아티아 알파벳
# N = input()
# D = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# count = 0
# while bool(N) != False:
#     if N[:3] == 'dz=':
#         N = N.replace('dz=', '')
#         count += 1
#     elif N[:2] in D:
#         N = N[2:]
#         count += 1
#     else:
#         N = N[1:]
#         count += 1
# print(count)