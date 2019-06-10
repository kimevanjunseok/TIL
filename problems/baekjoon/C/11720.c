#include <stdio.h>

int main(void) {
    int n;
    char m[100];
    int sum = 0;
    scanf("%d", &n);
    scanf("%s", m);

    for (int i = 0; i < n; i++) {
        sum += m[i] - 48;
    }
    printf("%d\n", sum);
}
