import sys
sys.stdin = open("Flatten_input.txt")


for n in range(1, 11):
    N = int(input())
    boxes = list(map(int, input().split()))
    cnt = 0
    boxes_num = boxes[0]
    for T in range(N):
        for i in range(len(boxes)):
            if boxes_num < boxes[i]:
                boxes_num = boxes[i]
                boxes_number = i
        boxes[boxes_number] += -1

        for i in range(len(boxes)):
            if boxes_num > boxes[i]:
                boxes_num = boxes[i]
                boxes_number = i
        boxes[boxes_number] += 1

    max_num = boxes[0]
    for i in range(len(boxes)):
        if max_num < boxes[i]:
            max_num = boxes[i]

    min_num = boxes[0]
    for i in range(len(boxes)):
        if min_num > boxes[i]:
            min_num = boxes[i]

    result = max_num - min_num
    print(f'#{n} {result}')






