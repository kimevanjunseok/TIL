#include <stdio.h>

int main(void) {
    char DAY[7][3] = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
    int MONTH[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int n, m;
    int sum = 0;

    scanf("%d %d", &n, &m);

    for (int i = 0; i < n-1; i++) {
        sum += MONTH[i];
    }
    sum += m;

    for (int i = 0; i < 3; i++) {
        printf("%c", DAY[sum % 7][i]);
    }
    printf("\n");
}