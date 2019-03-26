S, X = map(str, input().split())
X = int(X)
result = 0
for i in range(1, len(S)):
    a = S[:i]
    b = S[i:]
    if X == int(a) + int(b):
        result = int(a) + int(b)
        break
if result:
    print(f'{int(a)}+{int(b)}={result}')
else:
    print('NONE')
