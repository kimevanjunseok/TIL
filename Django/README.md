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

`manage.py` : 장고 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인 유틸리티

`프로젝트이름폴더` : 디렉토리 내부에는 프로젝트를 위한 실제 파이썬 패키지들이 저장됩니다. 이 디렉토리 내의 이름을 이용하여 프로젝트 어디서나 파이썬 패키지들을 import 할 수 있음

`__init__.py` : 파이썬으로 하여금 이 디렉토리를 패키지처럼 다루라고 알려주는 용도의 단순한 빈 파일

`setting.py` : 현재 장고 프로젝트의 모든 환경과 구성을 저장합니다

`urls.py` : 현재 장고 프로젝트의 URL 선언을 저장. 사이트의 URL과 VIEWS의 연결을 지정

`wdgi.py` : 현재 프로젝트를 서비스하기 위한 WSGI호환 웹 서버의 진입점.

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

`admin.py ` : 관리자용 페이지 커스터마이징 장소

`apps.py`: 앱의 정보가 있는 곳. 우리는 보통 수정할 일이 없음

`models.py`: 앱에서 사용하는 MODEL을 정의하는곳

`tests.py`: 테스트 코드를 작성하는 곳

`views.py`: 뷰들이 정의 되는 곳. 사용자에게 어떤 데이터를 보여줄지 구현되는 곳

### 프로젝트 폴더 tree

```
# 프로젝트 폴더
├── 프로젝트명
│    └── __init__.py
│    └── settings.py
│    └── urls.py.py
│    └── wsgi.py
├── APP명
│    └── migrations
│        └── __init__.py
│    └── __init__.py
│    └── admin.py
│    └── apps.py.py
│    └── models.py
│    └── tests.py
│    └── views.py
├── db.sqlite3
└── manage.py
```

