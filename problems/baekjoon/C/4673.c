#include <stdio.h>
#define MAX 10000

int func(int x);

int main(void) {
    int ary[10000] = {};
    for (int i = 1; i < 10000; i++) {
        ary[i] = i + func(i);
        int cnt = 0;
        for (int j = 1; j < sizeof(ary) / sizeof(ary[0]); j++) {
            if (i == ary[j]) {
                cnt = 1;
            }
        }
        if (cnt == 0) {
            printf("%d\n", i);
        }
    }
}

int func(int x) {
    if (x == 0) {
        return 0;
    }
    return (x % 10 + func(x / 10));
}

