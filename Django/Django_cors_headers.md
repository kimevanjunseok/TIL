# Django cors headers

> Frontend와 Post번호가 다르면 다른 서버로 인식하기 때문에 오류을 발생한다. 이를 해결할 수 있는 것이 Django cors headers 이다.

### 설치

```bash
$ pip install django-cors-headers
```

### 설정

- settings.py

  ```python
  ...
  
  INSTALLED_APPS = [
      ...
      'corsheaders',
      ...
  ]
  
  ...
  
  MIDDLEWARE = [
      ...
      'corsheaders.middleware.CorsMiddleware',
      'django.middleware.common.CommonMiddleware',
      ...
  ]
  
  ...
  
  CORS_ORIGIN_ALLOW_ALL=True # CORS_ORIGIN_ALLOW_ALL의 기본값 False
  ```

### 참고 [Link](<https://pypi.org/project/django-cors-headers/>)

