#include <stdio.h>

int main()
{
    int n;
    printf("enter any integer: ");
    scanf("%d", &n);
    printf("reverse is ");
    while (n != 0)
    {
        printf("%d", n % 10);
        n = n / 10;
    }
    printf("\n");
    return 0;
}