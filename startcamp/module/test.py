def add(a, b=0):
    return a+b

def mul(a, b=1):
    return a*b
# 프로그램의 시작점일때만 아래 코드가 실행
if __name__ == '__main__':
    print(add(10, 20))
    print(mul(10, 20))