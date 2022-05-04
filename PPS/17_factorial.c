#include <stdio.h>

int main(){
    int n;
    printf("enter n to find it's factorial: ");
    scanf("%i", &n);
    int factorial = 1;
    while (n != 0){
        factorial *= n;
        n -= 1;
    }
    printf("n! is equal to %i\n", factorial);
}