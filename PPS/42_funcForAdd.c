#include <stdio.h>

int sum(int i, int j){
    int result = i + j;
    return result;
}

void main(){
    int a, b;
    printf("enter [a, b]: ");
    scanf("%d, %d", &a, &b);
    printf("sum of %d and %d is %d\n", a, b, sum(a, b));
}