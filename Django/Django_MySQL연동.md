# Django MySQL연동

> Django와 MySQL 연동하는 방법
>
> Django와 MySQL 기본 설치는 했다고 가정하고 설명

## MySQL Workbench

- 데이터베이스 생성

  ```mysql
  CREATE DATABASE databasename;
  ```

## Django

- pip install

  ```bash
  $pip install mysqlclient
  ```

- settings.py

  ```python
  ...
  
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'database 이름',
          'USER': 'Username',
          'PASSWORD': '설정한 password',
          'HOST': '호스트 ip주소',
          'PORT': '포트주소(default=3306)',
      }
  }
  
  ...
  ```

- migrate

  ```bash
  $python manage.py migrate
  ```
