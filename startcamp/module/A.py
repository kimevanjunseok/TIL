def func():
    print("function A.py")
# print(f"A의 __name__은 {__name__}.")
print("top-level A.py")

if __name__=="__main__": # 매인이냐 import되냐 차이
    print('A.py 가 직접 실행')
else:
    print('A.py 가 import 되어 사용됨')