numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd = []
even = []

for n in numbers:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)
        
print(even, "짝수입니다.")
print(odd, "홀수입니다.")