#include <stdio.h>


int main(){
    int a, b;
    printf("enter a: ");
    scanf("%d", &a);
    printf("enter b: ");
    scanf("%d", &b);
    printf("%i + %i =  %i\n", a, b, a + b);
    printf("%i - %i =  %i\n", a, b, a - b);
    printf("%i * %i =  %i\n", a, b, a * b);
    printf("%i / %i =  %i\n", a, b, a / b);
    return 0;
}