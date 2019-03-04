import sys
sys.stdin = open('공통조상_input.txt')

T = int(input())

def preorder(node):
    if node != 0:
        save.append(node)
        preorder(tree[node][0])
        preorder(tree[node][1])

for n in range(1, T+1):
    V, E, son1, son2 = map(int, input().split())
    tree = [[0 for _ in range(2)] for _ in range(V + 1)]
    temp = list(map(int, input().split()))
    stack_1, stack_2 = [son1], [son2]
    save = []
    for i in range(0, len(temp), 2):
        n1 = temp[i]
        n2 = temp[i + 1]
        if not tree[n1][0]:
            tree[n1][0] = n2
        else:
            tree[n1][1] = n2


    while True:
        length_1 = len(stack_1)
        for i in range(0, len(temp), 2):
            if stack_1[-1] == temp[i+1]:
                stack_1.append(temp[i])

        length_2 = len(stack_2)
        for i in range(0, len(temp), 2):
            if stack_2[-1] == temp[i+1]:
                stack_2.append(temp[i])

        if set(stack_1) & set(stack_2):
            break

    p = max(set(stack_1) & set(stack_2))
    preorder(p)
    result = len(save)

    print('#{0} {1} {2}'.format(n, p, result))