# Django-rest-knox

> Knox는 Django REST Framework에 대한 사용하기 쉬운 인증을 제공합니다 .

## 설치

```bash
$ pip install django-rest-knox
```

## 설정

- settings.py

  ```python
  ...
  
  INSTALLED_APPS = [
      ...
      'knox',
      ...
  ]
  
  ...
  
  REST_FRAMEWORK = {
      "DEFAULT_AUTHENTICATION_CLASSES": ("knox.auth.TokenAuthentication",),
  }
  
  ...
  ```

## 회원가입 및 로그인 구현하기

- serializers.py

  ```python
  from rest_framework import serializers
  from django.contrib.auth import get_user_model
  from django.contrib.auth import authenticate
  
  User = get_user_model()
  
  class CreateUserSerializer(serializers.ModelSerializer):
      class Meta:
          model = User
          fields = ("id", "username", "password")
          extra_kwargs = {"password": {"write_only": True}}
  
      def create(self, validated_data):
          user = User.objects.create_user(
              validated_data["username"], None, validated_data["password"]
          )
          return user
  
  class LoginUserSerializer(serializers.Serializer):
      username = serializers.CharField()
      password = serializers.CharField()
  
      def validate(self, data):
          user = authenticate(**data)
          if user and user.is_active:
              return user
          raise serializers.ValidationError("Unable to log in with provided credentials.")
  
  class UserSerializer(serializers.ModelSerializer):
      class Meta:
          model = User
          fields = ("id", "username")
  ```

- views.py

  ```python
  from rest_framework import viewsets, permissions, generics, status
  from rest_framework.decorators import api_view
  from rest_framework.response import Response
  from rest_framework.views import APIView
  from .serializers import CreateUserSerializer, UserSerializer, LoginUserSerializer
  from knox.models import AuthToken
  
  # Create your views here.
  class RegistrationAPI(generics.GenericAPIView):
      serializer_class = CreateUserSerializer
  
      def post(self, request, *args, **kwargs):
          if len(request.data["username"]) < 6 or len(request.data["password"]) < 4:
              body = {"message": "short field"}
              return Response(body, status=status.HTTP_400_BAD_REQUEST)
          serializer = self.get_serializer(data=request.data)
          serializer.is_valid(raise_exception=True)
          user = serializer.save()
          return Response(
              {
                  "user": UserSerializer(
                      user, context=self.get_serializer_context()
                  ).data,
                  "token": AuthToken.objects.create(user),
              }
          )
  
  
  class LoginAPI(generics.GenericAPIView):
      serializer_class = LoginUserSerializer
  
      def post(self, request, *args, **kwargs):
          serializer = self.get_serializer(data=request.data)
          serializer.is_valid(raise_exception=True)
          user = serializer.validated_data
          return Response(
              {
                  "user": UserSerializer(
                      user, context=self.get_serializer_context()
                  ).data,
                  "token": AuthToken.objects.create(user)[1],
              }
          )
  
  
  class UserAPI(generics.RetrieveAPIView):
      permission_classes = [permissions.IsAuthenticated]
      serializer_class = UserSerializer
  
      def get_object(self):
          return self.request.user
  ```

- (app)urls.py

  ```python
  from django.urls import path, include
  from .views import RegistrationAPI, LoginAPI, UserAPI
  
  urlpatterns = [
      path("register/", RegistrationAPI.as_view()),
      path("login/", LoginAPI.as_view()),
      path("user/", UserAPI.as_view()),
  ]
  ```

- (project)urls.py

  ```python
  ...
  from django.urls import path, include
  
  urlpatterns = [
      ...
      path('auth/', include('[app-name].urls')),
      ...
  ]
  
  ...
  ```

- migrate

  ```bash
  $ python manage,py migrate
  ```