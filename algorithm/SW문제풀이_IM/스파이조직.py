# S = input().split()
# N = int(S[0])
# S = S[1]
# index = 0
# D = dict()
# String = ""
# for i in range(51):
#     D[i] = []
# D[index] = ['0']
# for i in range(1, len(S)):
#     if S[i] == '<':
#         D[index].append(String)
#         String = ""
#         index += 1
#     elif S[i] == '>':
#         D[index].append(String)
#         String = ""
#         index += -1
#     else:
#         String += S[i]
#
# L = (" ".join(D[N])).split()
#
# for i in range(len(L)):
#     print(L[i], end=" ")

S = input().split()
N = int(S[0])
S = S[1]
index = 0
String = ""
L = []
for i in range(len(S)):
    if S[i] == "<":
        if index == N:
            L.append(String)
            String = ''
        index += 1
        String = ''
    elif S[i] == ">":
        if index == N:
            L.append(String)
            String = ''
        index += -1
        String = ''
    else:
        String += S[i]

for i in range(len(L)):
    if L[i] != "":
        print(L[i], end=" ")

