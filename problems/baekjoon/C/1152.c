#include <stdio.h>

int main(void) {
    char s[1000001];
    int cnt = 0;
    int change = 0;
    int i = 0;
    
    // scanf("%[^\n]", s);
    gets(s);

    while (s[i] != '\0') {
        if (s[i] != ' ' && change == 0) {
            cnt++;
            change = 1;
        }
        else if (s[i] == ' ') {
            change = 0;
        }
        i++;
    }
    printf("%d\n", cnt);
    
}