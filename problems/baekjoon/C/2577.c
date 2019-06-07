#include <stdio.h>

int main(void) {
    int A, B, C, sum;
    int s[10] = {0};
    scanf("%d %d %d", &A, &B, &C);

    sum = A * B * C;
    while (sum) {
        s[sum % 10]++;
        sum = sum / 10;
    }
    for (int i = 0; i < 10; i++) {
        printf("%d\n", s[i]);
    }
}