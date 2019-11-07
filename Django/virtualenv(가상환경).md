# virtualenv(가상환경)

> 윈도우 설치/사용

#### 설치

```bash
$ pip install virtualenv
```

#### 원하는 폴더에서 가상환경 만들기

```bash
$ viryualenv 가상환경이름
```

#### 가상환경 실행

```bash
$ source 가상환경이름/Scripts/activate
```

#### 가상환경 종료

```bash
$ source 가상환경이름/Scripts/deactivate 
```

#### 가상환경에 설치된 페키지 목록을 저장

> requirements.txt를 관례적으로 사용

```bash
$ pip freeze > requirements.txt
```

#### 가상환경의 페키지 목록을 설치

```bash
$ pip install -r requirements.txt
```

