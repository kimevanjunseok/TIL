#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);

    if (n < 100) {
        printf("%d\n", n);
    }
    else {
        int cnt = 99;
        int a, b, c;

        for (int i = 100; i <= n; i++) {
            if (i == 1000) {
                break;
            }
            a = i % 10;
            b = (i / 10) % 10;
            c = i / 100;
            if (a - b == b - c) {
                cnt++;
            }
        }
        printf("%d\n", cnt);
    }
}