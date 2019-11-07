# Django

> 파이썬으로 작성된 오픈 소스 웹 애플리케이션 프레임워크로, 모델-뷰-컨트롤러 패턴(MVC)을 따르고 있다. 현재는 장고 소프트웨어 재단에 의해 관리되고 있다. 고도의 데이터베이스 기반 웹사이트를 작성하는 데 있어서 수고를 더는 것이 장고의 주된 목표이다.

### 설치

```bash
$ pip install django
```

## 프로젝트 생성

```bash
$ django-admin startproject 프로젝트명 . # 현재 폴더에 프로젝트 생성
# or
$ django-admin startproject 프로젝트명 # (프로젝트명)폴더 생성 후 그 안에 프로젝트 생성
```

### 서버실행

```bash
# 프로젝트 폴더에서 서버 실행(manage.py있는 폴더)
$ python manage.py runserver
```

> 로켓화면이 나와야 정상이다

![캡처](https://user-images.githubusercontent.com/45934117/68356262-22728580-0155-11ea-9632-a7ed2f9b7c64.PNG)

### 파일 셋팅

- 프로젝트명/settings.py

  ```python
  # ...
  ALLOWED_HOSTS = ['*']
  # ...
  LANGUAGE_CODE = 'ko-kr'
  TIME_ZONE = 'Asia/Seoul'
  # ...
  USE_TZ = False # 서버 내부적으로 돌아가는 시간 UTC시간을 바꾸는 설정
  ```

  > 설정 후 이와같은 화면이 나오면 정상

  ![캡처](https://user-images.githubusercontent.com/45934117/68357665-69fb1080-0159-11ea-8a4b-744f0c8c45b2.PNG)

## APP 생성

프로젝트 폴더에서 다음 명령어 실행

```bash
$ python manage.py startapp APP명
```

- 프로젝트명/settings.py

  ```python
  # ...
  INSTALLED_APPS = [
      'app명.apps.app명Config', 
      # app명이 post면 'post.apps.PostConfig', 
      # ...
  ]
  # ...
  ```

### 프로젝트 폴더 tree

```
# 프로젝트 폴더
├── 프로젝트명
│	└── __init__.py
│	└── settings.py
│	└── urls.py.py
│	└── wsgi.py
├── APP명
│	└── migrations
│		└── __init__.py
│	└── __init__.py
│	└── admin.py
│	└── apps.py.py
│	└── models.py
│	└── tests.py
│	└── views.py
├── db.sqlite3
└── manage.py
```

