# With

- open("파일명", "쓰기/읽기", "인코딩") as 변수명
  - encoding="utf-8"은 한글데이터가 깨질 수 있으니 쓰는 것이 좋다
- write()와 writelines(), read(), readlines()가 있다.

### 파일 쓰기

```python
with open("new.txt", "w", encoding="utf-8") as f:
    L = ["안녕\n", "잘가\n"]
    f.writelines(L)
```

```txt
안녕
잘가
```

- "\n"가 없으면 한줄로 입력되기 때문에 원하는 데이터를 읽기 힘들 수 있다
- write()는 한번에 데이터를 한개밖에 못넣는다 따라서 위에 데이터를 저장하려면 다음과 같이 해야한다.

```python
with open("new.txt", "w", encoding="utf-8") as f:
    L = ["안녕\n", "잘가\n"]
    for i in range(len(L)):
    	f.write(L[i])
```



### 파일 읽기

```python
with open("new.txt", "r") as f:
    data = f.readlines()
    print(data)

>>>["안녕\n", "잘가\n"]
```

- read()를 쓰면 줄 상관없이 불러오기 때문에 여러 줄일 경우 readlines()가 사용하기 편리하다

```python
with open("new.txt", "r") as f:
    data = f.read()
    print(data[0])

>>>안
```

