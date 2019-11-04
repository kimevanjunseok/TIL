# Random

```python
import random
```

### 사용법

```python
>>> random.random() // 0 ~ 1 사이 무작위 숫자 출력
0.44604387684048785
```

```python
>>> random.randrange(1, 7) // 1 ~ 6 사이 무작위 숫자 출력
6
```

```python
>>> L = [1, 3, 5, 7, 9]
>>> random.shuffle(L) // 리스트 L를 무작위로 섞음
>>> L
[5, 1, 3, 7, 9]
```

```python
>>> L = [1, 3, 5, 7, 9]
>>> random.choice(L) // 리스트 L를 무작위로 하나 선택
3
```

