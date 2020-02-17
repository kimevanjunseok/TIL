# Static

> static은 정적의, 고정의 뜻으로 클래스에서 공유될때 사용한다.

## 예시

- 인스턴스 변수일 때

  ```java
  public class Main {
  
      public static void main(String[] args) {
          Test test1 = new Test();
          Test test2 = new Test();
      }
  }
  
  class Test {
  
      int number = 0;
  
      public Test() {
          number++;
          System.out.println(number);
      }
  }
  ```

  먼저 static이 없는 인스턴스 변수를 예로 위와 같은 코드실행 시키면 이렇게 출력이 된다.

  ```
  1
  1
  ```

- 클래스(static) 변수일 때

  ```java
  public class Main {
  
      public static void main(String[] args) {
          Test test1 = new Test();
          Test test2 = new Test();
      }
  }
  
  class Test {
  
      static int totalNo = 0;
  
      public Test() {
          totalNo++;
          System.out.println(totalNo);
      }
  }
  
  ```

  static이 있으면 해당 클래스는 값을 클래스 내에서 공유되어 다음과 같이 출력한다.

  ```
  1
  2
  ```

## Static은 

- 공통적으로 사용하는 인스턴스 변수에 붙여준다. 

- static이 있는 변수를 멤버변수라고하고, static이 붙은 변수나 메서드는 메모리에 자동으로 저장되기때문에 인스턴스를 생성하지 않아도 사용할 수 있다.

  ```java
  public class Main {
  
      public static void main(String[] args) {
          // 멤버 변수 호출
          System.out.println(Test.totalNo);
          // static 메소드 호출
          Test.Test();
      }
  }
  
  class Test {
  
      static int totalNo = 0;
  
      public static void Test() {
          System.out.println(totalNo);
      }
  }
  
  ```

  ```
  0
  0
  ```

- static 메서드에서는 인스턴스 변수를 사용할 수 없다.

  - static 메소드는 프로그램이 실행되면 메모리에 저장되어 인스턴스 생성없이 바로 사용이 가능하지만 인트턴스 변수는 클래스가 실행되야 생성되기 때문이다. 따라서 static 메서드를 호출할 때, 인스턴스 변수는 생성되지 않았을 수도 있기 때문에 static 메소드에서 인스턴스 변수는 사용할 수 없다.