## 1. 우리가 이제까지 활용했던 print는 내장 함수(built-in function)입니다. 배웠던 내장 함수 중 5개만 나열해보세요.

### 답 : range, int, input, max, min 등등



## 2. 다음 중 틀린 것은?

### (1) 함수는 오직 하나의 객체만 반환할 수 있어서, return a, b 처럼 쓸 수 없다. 

### = False

### (2) 함수에서 return을 작성하지 않으면 None 값을 반환한다. 

### = True

### (3) 함수의 인자(parameter)는 함수 선언시 설정한 값이며, 인수(argument)는 함수 호출시 넘겨주는 값이다. 

### = True

### (4) 가변 인자를 설정할 때는 인자 앞에서 *을 붙이고, 이때는 함수 내에서 tuple로 처리된다. 

### = True

### (5) 파이썬 활용되는 ‘스코프(scope)’ 룰에 따르면 변수에서 값을 Local scope -> Global scope -> Built-in scope 순으로 찾는다.

### = True



## 3. 함수의 인자 기본 값을 설정을 활용하여 곱셈의 결과를 반환하는 my_mul을 만들어주세요.

```python
def my_mul(*num):
    n = 1
    for i in num:
        n *= i
    return n

def my_mul(a, b=1):
    return a*b
```



