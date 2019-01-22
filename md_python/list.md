# 리스트

### 리스트 만드는 법

```python
>>> a1 = [] #빈 리스트
>>> a2 = list() #빈 리스트
>>> b = [1, 2, 3] # 숫자 가능
>>> c = ["apple", "banana"] # 스트링 가능
>>> d = [1, "apple"] # 둘 다 가능
>>> e = [1, 2, [1, "apple"]] # 리스트 안에 리스트 가능
```



### 인덱싱

```python
>>> a = [1, 2, 3, 4, 5]
>>> a[0] # a[0]의 값을 불러옴
1
>>> a[0] + a[2] # 사칙연산 가능 a[0] = 1, a[2] = 3
4
>>> a[-1] # a 리스트의 마지막 값
5
```

```python
>>> a = [1, 2, 3, ['a', 'b', 'c']]
>>> a[0]
1
>>> a[3] # ['a', 'b', 'c']는 a 리스트의 하나의 값.
['a', 'b', 'c']
>>> a[3][0] # 리스트 안의 리스트 값 불러오기
a
```
