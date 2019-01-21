#벌집
# N = int(input())
# n = 1
# while True:
#     if N <= (3*(n**2) - 3*n + 1):
#         print(n)
#         break
#     n += 1

#분수찾기
# N = int(input())
# n = 1
# while True:
#     if N == 1:
#         print('1/1')
#         break
#     elif N <= (n*(n+1))/2:
#         N = N - (n*(n-1))//2
#         if n % 2 == 0:
#             print(f'{N}/{n-(N-1)}')
#             break
#         else:
#             print(f'{n-(N-1)}/{N}')
#             break
#     n += 1

#Fly me to the Alpha Centauri
# N = int(input())
# cnt = 2
# for i in range(N):
#     A, B = input().split()
#     D = int(B) - int(A)
#     while True:
#         if D > 2:
#             if D <= cnt**2 + cnt:
#                 if D <= cnt**2 + cnt - cnt:
#                     print(cnt*2 -1)
#                     cnt = 2
#                     break
#                 else:
#                     print(cnt*2)
#                     cnt = 2
#                     break
#         else:
#             print(1)
#             cnt = 2
#             break
#         cnt += 1

#ACM호텔
# num = int(input())
# for i in range(num):
#     H, W, N = map(int, input().split())
#     A = N // H + 1
#     B = (N % H)*100
#     if B != 0:
#         print(B+A)
#     else:
#         print(H*100 + A-1)

#부녀회장이 될테야
# N = int(input())
# out_n = []
# num = 0
# for i in range(N):
#     k = int(input())
#     n = int(input())
#     for x in range(k+1):
#         for y in range(1, n+1):
#             if x == 0:
#                 out_n.append(y)
#             else:
#                 num += out_n[y-1]
#                 out_n.append(num)
#         if x > 0:
#             out_n = out_n[n:]
#             num = 0
#     print(out_n[-1])
#     out_n = []

#방번호
# N = list(input())
# L = ['1', '2', '3', '4', '5', '6', '6', '7', '8', '0']
# count = 1
# for i in range(len(N)):
#     if N[i] == '9':
#         del N[i]
#         N.insert(i, '6')
# for i in range(len(N)):
#     if N[i] in L:
#         L.remove(N[i])
#     else:
#         count += 1
#         L = L + ['1', '2', '3', '4', '5', '6', '6', '7', '8', '0']
#         L.remove(N[i])
# print(count)

#카잉달력
# import sys
# N = int(sys.stdin.readline())
# k = a = b = 0
# for i in range(N):
#     M, N, x, y = map(int, sys.stdin.readline().split())  
#     if (M % 2 == 0 and N % 2 == 0 and (x + y) % 2 == 1) or (N == M and x != y):
#         print(-1)
#     else:    
#         while True:
#             a += 1
#             b += 1
#             if a > M and b > N:
#                 a = b = 1
#             elif a > M:
#                 a = 1
#             elif b > N:
#                 b = 1
#             elif a == x and b == y:
#                 k += 1
#                 print(k)
#                 break 
#             k += 1
#             print(k)
#         k = a = b = 0  

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
