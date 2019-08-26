def judge(x):
    n = len(x)
    if n % 2:
        for i in range(n//2 + 1):
            if x[i] != x[n-i-1]:
                return False
        return n
    else:
        for i in range(n//2):
            if x[i] != x[n-i-1]:
                return False
        return n

def solution(s):
    n = len(s)
    for i in range(n, 0, -1):
        for j in range(n-i+1):
            result = judge(s[j:i+j])
            if result:
                return result

if __name__ == "__main__":
    s = ["abcdcba", "abacde"]
    for i in s:
        print(solution(i))