def solution(A, B):
    return [[sum([A[i][k]*B[k][j] for k in range(len(B))]) for j in range(len(B[0]))] for i in range(len(A))]

# or

def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr2)):
                answer[i][j] += arr1[i][k]*arr2[k][j]
    return answer