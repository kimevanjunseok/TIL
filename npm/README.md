# npm

npm란?

> 자바스크립트 런타임 환경 Node.js의 기본 패키지 관리자

Version

> 6.9.0

### 기본 명령어

`npm -v`: 버전 확인

`npm init`: package.json를 만드는 명령어

`npm list`: 현재 디렉토리에 설치된 모듈 확인

`npm list -g`: 전역에 설치된 모듈 확인

`npm install`: package.json에 명시된 모든 dependencies의 모듈 설치 

`npm install 모듈명` : 모듈 설치



#### npm install [모듈명] 과 npm install [모듈명] --save 차이(의존성 모듈 관리)

> npm@5부터는 --save는 기본옵션으로 되있다.

프로젝트시 npm install [모듈명]만하면 node_modules에는 설치되지만, package.json에 명시하지 못한다.

`npm install`실행시 package.json의 명시된 모듈을 설치할 수 있어 package.json파일의 의존하여 프로젝트를 관리하기 때문에 의존성 모듈관리라고 한다.