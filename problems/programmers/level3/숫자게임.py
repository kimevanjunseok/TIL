def func(A, B):
    global result

    for i in range(len(A)):
        if B:
            for j in range(len(B)):
                if A[i] < B[j]:
                    B.pop(j)
                    result += 1
                    break
        else:
            return

def solution(A, B):
    global result

    A.sort()
    B.sort()
    func(A, B)

    return result

result = 0

if __name__ == "__main__":
    A = [[5,1,3,7], [2,2,2,2]]
    B = [[2,2,6,8], [1,1,1,1]]
    for i in range(len(A)):
        print(solution(A[i], B[i]))