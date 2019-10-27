# Module

- 파일구조

> module
>
> > A.py
> >
> > B.py

A.py

```python
def func():
    print("function A.py")

print("top-level A.py")

if __name__=="__main__": # 파일이 메인으로 실행될 경우
    print('A.py 가 직접 실행')
else:
    print('A.py 가 import 되어 사용됨')
```

B.py

```python
import A

print("top-level B.py")
A.func()

if __name__=="__main__":
    print('B.py 가 직접 실행')
else:
    print('B.py 가 import 되어 사용됨')
```

A.py실행

```bash
$ python A.py
top-level A.py
A.py 가 import 되어 사용됨
```

B.py실행

```bash
$ python B.py
top-level A.py
A.py 가 import 되어 사용됨
top-level B.py
function A.py
B.py 가 직접 실행
```

