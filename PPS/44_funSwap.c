#include <stdio.h>

void swap(int *i, int *j){
    int tmp = *i;
    *i = *j;
    *j = tmp;
}

void main(){
    int a, b;
    printf("enter [a, b]: ");
    scanf("%d, %d", &a, &b);
    swap(&a, &b);
    printf("a= %d, b= %d\n", a, b);
}