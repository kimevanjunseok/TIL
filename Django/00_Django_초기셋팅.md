# Django

### 0. 준비사항

 1. pyenv / python / pyenv-virtualenv 설치 및 설정([c9 초기설정](https://zzu.li/djpy2_c9))

    ```bash
    - python 3.6.7
    
    # install pyenv
    $ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
    $ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
    $ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
    $ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
    $ source ~/.bashrc
    $ pyenv install 3.6.7
    $ pyenv global 3.6.7
    $ pyenv rehash
    
    # install pyenv-virtualenv
    $ git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
    $ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
    $ source ~/.bashrc
    ```

    ```bash
    - git
    ```

 2. 가상환경

    ```bash
    $ pyenv virtualenv 3.6.7 django-venv
    ```

 3. 프로젝트 폴더 생성 및 이동

    ```bash
    $ mkdir PROJECT01
    $ cd PROJECT01/
    ```

 4. Local 가상환경 활성화

    ```bash
    $ pyenv local django-venv 
    ```

 5. 장고 설치

    ```bash
    $ pip install django
    $ pip install --upgrade pip
    ```

 6. Django start


### 1. 1 장고 프로젝트

1. 프로젝트 생성

   ```bash
   $ django-admin startproject django_intro .
   							[프로젝트이름]
   $ python manage.py startapp home
   							[이름]
   ```

   - django, test, class, django-test은 프로젝트 이름으로 사용하면 안됩니다.

2. 서버실행

   ```python
   ALLOWED_HOST=['*']
   ALLOWED_HOST=['주소']
   ```

   ```bash
   $ python manage.py runserver $IP:$PORT
   ```

   주소를 입력해 주려면 실행후 오류 화면창에서 홈페이지 주소를 가져와야한다.

   ```python
   ALLOWED_HOSTS = ['django-intro-kimevanjunseok.c9users.io']
   ```

3. `.gitignore`설정

   ```bash
   $ touch .gitignore
   ```

   - gitignore.io 에 들어가서 django 쳐서 복붙!!

4. TIMEZONE, LANGUAGE_CODE 설정(`setting.py`)

   ```python
   LANGUAGE_CODE = 'ko-kr'
   TIME_ZONE = 'Asia/Seoul'
   ```

5. 로켓 페이지 한글화 확인

   ```bash
   $ python manage.py runserver $IP:$PORT
   ```

   - 들어가서 확인!!

6. 프로젝트 구조

   `manage.py` : 장고 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인 유틸리티

   `프로젝트이름폴더` : 디렉토리 내부에는 프로젝트를 위한 실제 파이썬 패키지들이 저장됩니다. 이 디렉토리 내의 이름을 이용하여 프로젝트 어디서나 파이썬 패키지들을 import 할 수 있습니다.

   `setting.py` : 현재 장고 프로젝트의 모든 환경과 구성을 저장합니다.

   `__init__.py` : 파이썬으로 하여금 이 디렉토리를 패키지처럼 다루라고 알려주는 용도의 단순한 빈 파일

   `urls.py` : 현재 장고 프로젝트의 URL 선언을 저장. 사이트의 URL과 VIEWS의 연결을 지정.

   `wdgi.py` : 현재 프로젝트를 서비스하기 위한 WSGI호환 웹 서버의 진입점. 

-------------------------------------

### 1. 2 장고 어플리케이션(APP)

- 실제로 특정한 역할을 하는 친구가 바로 APP

- 프로젝트는 이러한 어플리케이션의 집합

- 하나의 프로젝트는 여러개의 어플리케이션을 가질 수 있다.

- 각각의 어플리케이션은 MTV패턴으로 구성되어 있다.


1. 어플리케이션 만들기

2. 어플리케이션 구조

   `admin.py ` : 관리자용 페이지 커스터마이징 장소

   `apps.py`: 앱의 정보가 있는 곳. 우리는 수정할 일이 없습니다.

   `models.py`: 앱에서 사용하는 MODEL을 정의하는곳

   `tests.py`: 테스트 코드를 작성하는 곳

   `views.py`: 뷰들이 정의 되는 곳. 사용자에게 어떤 데이터를 보여줄지 구현되는 곳

3. 어플리케이션 등록

   > home > apps.py > class HomeConfig()
   >
   > `home.apps.HomeConfig`, 등록
   >
   > 혹은 그냥 home이라고 작성가능. 다만 추후에 자세한 설명을 할 수 없다.

4. MTV 패턴

5. view - url

   - view => urls => template 순으로 코드 작성

   - HttpResponse 로 첫 리턴 값 출력해보기

     ```python
     def index(request):
         return HttpResponse('Welcome to Django !')
     ```

   - path(route, views, name) 2개의 필수인자와 1개의 선택 인자

     ```python
     path('home/hello/<name>/', views.hello, name='hello'),
     path('home/index/', views.index, name='index'),
     ```

   - 저녁 메뉴 리턴 실습

     `views.py`에서

     ```python
     def dinner(request):
         menus = ["bob", "soup", "pizza", "고기", "볶음밥"]
         pick = random.choice(menus)
         return render(request, "dinner.html", {"menus": menus, "pick": pick})
     ```

     `urls.py`에서 path설정

     ```python
     path('home/dinner/', views.dinner, name='dinner'),
     ```

     `dinner.py`에서

     ```html
     {% for menu in menus %}
     <p>{{ menu }}</p>
     {% endfor %}
     <hr>
     {% if pick == "볶음밥" %}
     <p>김치볶음밥!!!</p>
     {% else %}
     <p>{{ pick }}</p>
     {% endif %}
     ```

6. Template

   - 장고에서 사용되는 템플릿은 DTL(Django Template Language)이다.

   - jinja2와 문법이 유사하지만 다르다.

   1. render()

      - render(request, template_name, context=None, context_type=None, status=None, using=None)

   2. Variable Routing

      ```python
      def hello(request, name):
      	return render(request, 'hello.html', {'name': name})
      ```

7. Form data (get / post)

   ```python
   request.GET.get('data')
   request.PORT.get('data')
   ```

   {{% csrf_token %}}를 form안에서 같이 보내줘야 합니다.(PORT일때)

   >csrf 공격과 같은 보안과 관련된 사항은 settings에 MIDDLEWARE에 되어있다.
   >
   >실제로 요청은 미들웨어 설정 사항들을 순차적으로 거친다. 응답은 아래에서 위로 거쳐서 응답이 리턴된다.

8. Template inheritance

   - home/templates/base.html 생성

     base.html 생성

     ```html
     <!DOCTYPE html>
     <html lang="en">
     
     <head>
         <meta charset="UTF-8">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <meta http-equiv="X-UA-Compatible" content="ie=edge">
         <title>{% block title %}{% endblock %}</title>
         <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
     </head>
     
     <body>
         <h1>장고 연습</h1>
         
         <hr>
         
         <div class="container">
         {% block body %}
         {% endblock %}
         </div>
         
         <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
         <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
         <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
     </body>
     
     </html>
     ```

     상속 html(`cube.py`)

     ```html
     {% extends 'base.html' %}
     {% block title %}cube{% endblock %}
     {% block body %}
     <h1>{{ number }}의 3제곱: {{ num3 }}</h1>
     {% endblock %}
     ```
