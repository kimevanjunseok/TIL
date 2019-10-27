

# List

## 만드는 법

```python
>>> L1 = [] #빈 리스트
>>> L2 = list() #빈 리스트
>>> L3 = [1, 2, 3] # 숫자 가능
>>> L4 = ["apple", "banana"] # 스트링 가능
>>> L5 = [1, "apple"] # 둘 다 가능
>>> L6 = [1, 2, [1, "apple"]] # 리스트 안에 리스트 가능
```



## 연산

#### (1) (+)

```python
>>> a = [1, 2, 3]
>>> b = [6, 7, 8]
>>> a + b # a 리스트 뒤에 b 리스트가 더해진다.
[1, 2, 3, 6, 7, 8]
```



#### (2) (*)

```python
>>> L1 = [1]
>>> L * 4 # L1 리스트 4번 반복
[1, 1, 1, 1]
>>> L2 = [1, 2, 3]
>>> L2 * 2
[1, 2, 3, 1, 2, 3]
```

- 빼기, 나누기 연산 (X)



## 인덱싱

#### 첫 번째 리스트의 인덱스는 0이다.

```python
>>> a = [1, 2, 3, 4, 5]
>>> a[0] # a[0]의 값을 불러옴
1
>>> a[0] + a[2] # 사칙연산 가능 a[0] = 1, a[2] = 3
4
>>> a[-1] # a 리스트의 마지막 값
5
>>> a[-2] # 마지막에서 두 번째
4
```

```python
>>> a = [1, 2, 3, ['a', 'b', 'c']]
>>> a[0]
1
>>> a[3] # ['a', 'b', 'c']는 a 리스트의 3번 인덱스 값.
['a', 'b', 'c']
>>> a[3][0] # 리스트 안의 리스트 값 불러오기
a
```



## 슬라이싱

```python
>>> a = [1, 2, 3, 4, 5, 6 ,7]
>>> a[0:4] # a 리스트의 0번 인덱스부터 3번 인덱스까지 (0번 인덱스 <= a리스트 < 4번 인덱스)
[1, 2, 3, 4]
>>> a[:4] # a 리스트의 첫 번째 인덱스부터 3번 인덱스까지
[1, 2, 3, 4]
>>> a[4:] # a 리스트의 4번 인덱스부터 끝까지
[5, 6, 7]
>>> a[:-1] # 마지막 인덱스는 -1이기 떄문데 마지막 전까지 나온다.
[1, 2, 3, 4, 5, 6]
>>> a[:-2] # -2 인덱스까지 슬라이싱
[1, 2, 3, 4, 5]
>>> a[1:6:2] # 1번 인덱스부터 5번 인덱스까지 2씩 증가 (슬라이싱 3번째 자리는 증가률)
[2, 4, 6]
>>> a[::-1] # 역순
[7, 6, 5, 4, 3, 2, 1]
>>> a[::-2] # 역순을 2씩 인덱스 감소
[7, 5, 3, 1]
```



## 수정

```python
>>> L = [1, 2, 3]
>>> L[1] = 9 # L 리스트의 1번 인덱스를 9로 변경
>>> L
[1, 9, 3]
```



## 삭제

#### (1) del

```python
>>> L1 = [1, 2, 3, 4, 5]
>>> del L[1] # L 리스트 1번 인덱스를 삭제
>>> L
[1, 3, 4, 5]
>>> L2 = [4, 5, 6, 7]
>>> del L2[2:] # L2[2:]는 [6, 7]이다. 따라서 L2 리스트에서 [6, 7]를 삭제한다.
>>> L2
[4, 5]
```

#### (2) remove()

```python
>>> L = [1, 2, 5, 4, 3]
>>> L.remove(5) # 해당 원소 제거
>>> L
[1, 2, 4, 3]
```

#### (3) pop()

```python
>>> L = [1, 2, 3, 4]
>>> v = L.pop() # 마지막 원소를 제거하면서 값을 출력한다.
>>> v
4
>>> L = [1, 2, 3]
>>> L.pop(0) # 변수에 할당없이 그냥 써도되며 인덱스를 입력해주면 해당 인덱스를 제거하며 출력한다.
1
```



## 추가

#### (1) append()

```python
>>> L = [1, 2, 3, 4]
>>> L.append(9) # L 리스트 맨뒤에 추가 L = L + [9] 와 같음
>>> L
[1, 2, 3, 4, 9]
>>> L.append([1, 2]) # 리스트뿐만 아니라 세트 튜플도 가능 L = L + [[1, 2]] 와 같음
>>> L
[1, 2, 3, 4, 9, [1, 2]]
```

#### (2) (+)

```python
>>> L = [1, 2, 3]
>>> L += [4]
[1, 2, 3, 4]
```



## 정렬

#### (1) 숫자 정렬

```python
>>> L = [4, 3, 7, 1, 0] # 숫자정렬
>>> L.sort()
>>> L
[0, 1, 3, 4, 7]
```

```python
>>> L = [4, 3.1, 7, 1, 0] # 실수도 가능하다
>>> L.sort()
>>> L
[0, 1, 3.1, 4, 7]
```



#### (2) 문자정렬

##### sort()

```python
>>> L = ["H", "A", "C"] # 문자정렬
>>> L.sort()
>>> L
["A", "C", "H"]
>>> L = ["h", "b", "C", "A"]
>>> L.sort()
['A', 'C', 'b', 'h'] # 대문자가 먼저 온다.
```

```python
>>> L = ["head", "boy", "Cold", "APPLE"]
>>> L.sort()
>>> L
['APPLE', 'Cold', 'boy', 'head'] # 맨 앞 문자기준으로 정렬한다.
```



##### * 추가

```python
>>> L = [4, 3, 7, 1, 0]
>>> L.sort(reverse = True)
[7, 4, 3, 1, 0] # 역순도 가능
```



##### sorted()

```python
>>> L = [4, 3, 7, 1, 0]
>>> K = sorted(L) # sorted는 변수가 필요하다
>>> K
[0, 1, 3, 4, 7]
>>> L
[4, 3, 7, 1, 0]
```