# Scanner

### 사용법

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
    }
}
```

1. next()

   > 공백을 기준으로 입력을 받는다.

   ```java
   String inputNext = sc.next();
   ```

2. nextLine()

   > 라인을 기준으로 입력을 받는다.

   ```java
   String inputNextLine = sc.nextLine();
   ```

3. nextInt()

   > int를 공백 기준으로 입력 받는다.

   ```java
   int inputInt = sc.nextInt();
   ```

