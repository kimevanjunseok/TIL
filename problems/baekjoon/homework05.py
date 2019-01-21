#셀프 넘버
# N = list(range(1, 10001))
# group = []
# for i in range(0, len(N)):
#     number = N[i] + (N[i] % 10) + ((N[i] // 10) % 10) + ((N[i] // 100) % 10) + ((N[i] // 1000) % 10)
#     group.append(number)
# group = set(group)
# N = set(N)
# total = N - group
# total = list(total)
# total.sort()
# for i in range(0, len(total)):
#     print(total[i])

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

#별 찍기 11
N = int(input())
List = []
a = '*'
b = '* *'
c = '*****'
List.append(a)
List.append(b)
List.append(c)
List_2 = List
x = 1
y = 3
z = 0
if N >= 6:
    for i in range(N-3):
        if z <= y-1:
            a = List_2[z] + ' '*(y*2-2*x+1) + List_2[z]
            List.append(a)
            x += 1
            if z == y-1:
                List_2 = List
                y *= 2
                z = 0
                x = 1
            else:
                z += 1
for i in range(N):
    print(List[i].center(N*2-1))