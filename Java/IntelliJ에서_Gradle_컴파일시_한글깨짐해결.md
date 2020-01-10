# IntelliJ에서 Gradle 컴파일시 한글깨짐해결

### 1. IntelliJ 가상머신 설정

`C:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2019.2.4\bin`폴더 안에 `idea.exe.vmoptions`와 `idea64.exe.vmoptions`가 있다.

 본인의 OS bit 파일에 들어가서 `-Dfile.encoding=UTF-8`를 추가한다. 

### 2. IntelliJ에서 Setting

IntelliJ를 실행하고 `help -> idea64.exe.vmoptions`에 들어간다.

마찬가지로 `-Dfile.encoding=UTF-8`를 추가한다.

