import sys
sys.stdin = open('contact_input.txt')

T = 10

for n in range(1, T+1):
    E, S = map(int, input().split())
    arr = list(map(int, input().split()))
    contact = [[arr[i], arr[i+1]] for i in range(0, len(arr), 2)]
    queue = [S]
    save = []
    visited = [S]
    cnt = [1, 0]

    copy_queue = queue
    queue_len = len(queue)

    while True:
        
        for i in contact:
            if (i[0] in queue) and (i[1] not in visited):
                save.append(i[1])
                cnt[1] += 1

        if not save:
            break
                
        queue += save
        save = []
        visited += queue
        
        for _ in range(cnt[0]):
            queue.pop(0)

        cnt[0], cnt[1] = cnt[1], 0

    print(f'#{n} {max(queue)}')
    