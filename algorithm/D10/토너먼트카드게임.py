import sys
sys.stdin = open('토너먼트카드게임_input.txt')

# def fight(L):

#     if L[0][1] == L[1][1]:
#         return L[0]
#     elif L[0][1] == 1 and L[1][1] == 2:
#         return L[1]
#     elif L[0][1] == 1 and L[1][1] == 3:
#         return L[0]
#     elif L[0][1] == 2 and L[1][1] == 1:
#         return L[0] 
#     elif L[0][1] == 2 and L[1][1] == 3:
#         return L[1]
#     elif L[0][1] == 3 and L[1][1] == 1:
#         return L[1]
#     elif L[0][1] == 3 and L[1][1] == 2:
#         return L[0]

# T = int(input())

# for n in range(1, T+1):
#     N = int(input())
#     S = input().split()
#     group = []
#     stack = []

#     for idx, i in enumerate(S):
#         group.append([idx+1, int(i)])
    
#     group = [group]
#     stack = group

#     while True:
#         win_stack = []
#         while True:    
#             group1 = stack[-1][:(len(stack[-1])+1)//2]
#             group2 = stack[-1][(len(stack[-1])+1)//2:]
#             stack.pop()
#             stack += [group2] + [group1]

#             while True:

#                 if (not stack) or (len(stack[-1]) > 2):
#                     break

#                 elif len(stack[-1]) == 1:
#                     win_stack += stack[-1]
#                     stack.pop()

#                 elif len(stack[-1]) == 2:
#                     win_stack += [fight(stack[-1])]
#                     stack.pop()
            
#             if not stack:
#                 break

#         if len(win_stack) == 2:
#             result = fight(win_stack)
#             break

#         stack = [win_stack]

#     print(f'#{n} {result[0]}')

#################################################################

# 재귀함수

T = int(input())

def fight(L):

    if L[0][1] == L[1][1]:
        return L[0]
    elif L[0][1] == 1 and L[1][1] == 2:
        return L[1]
    elif L[0][1] == 1 and L[1][1] == 3:
        return L[0]
    elif L[0][1] == 2 and L[1][1] == 1:
        return L[0] 
    elif L[0][1] == 2 and L[1][1] == 3:
        return L[1]
    elif L[0][1] == 3 and L[1][1] == 1:
        return L[1]
    elif L[0][1] == 3 and L[1][1] == 2:
        return L[0]

def half(L):

    global win_stack

    if not L:
        if len(win_stack) == 1:
            return
        else:
            win_stack = [win_stack]
            half([win_stack.pop()])

    elif len(L[-1]) > 2:
        group1 = L[-1][:(len(L[-1])+1)//2]
        group2 = L[-1][(len(L[-1])+1)//2:]
        L.pop()
        L += [group2] + [group1]
        half(L)

    elif len(L[-1]) == 2:
        win_stack += [fight(L.pop())]
        half(L)

    elif len(L[-1]) == 1:
        win_stack += L.pop()
        half(L)
    
for n in range(1, T+1):
    N = int(input())
    S = input().split()
    group = []
    win_stack = []

    for idx, i in enumerate(S):
        group.append([idx+1, int(i)])
    
    half([group])
    print(f'#{n} {win_stack[0][0]}')