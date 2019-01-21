# 소수 찾기
# N = int(input())
# cnt = 0
# sosu_find = list(map(int, input().split()))
# for i in range(N):
#     L = []
#     for j in range(1, sosu_find[i]+1):
#         if sosu_find[i] % j == 0:
#             L.append(j)
#     if len(L) == 2:
#         cnt += 1
# print(cnt)

# 소수
# N = int(input())
# M = int(input())
# len_L = []
# for i in range(N, M+1):
#     L = []
#     for j in range(1, i+1):
#         if i % j == 0:
#             L.append(j)
#     if len(L) == 2:
#         len_L.append(i)
# if len(len_L) > 0:
#     print(sum(len_L))
#     print(min(len_L))
# else:
#     print(-1)

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

#베르트랑 공준
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
