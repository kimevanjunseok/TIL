#include <stdio.h>

int main(void) {
    int n, i, j;

    scanf("%d", &n);

    for (i = 1; i <= n; i++) {
        for (j = n; j >= 1; j--) {
            j > i ? printf(" ") : printf("*");
        }
        puts("");
    }
}