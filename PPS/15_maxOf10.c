#include <stdio.h>


int main(){
    int a; 
    printf("enter number 1: ");
    scanf("%d", &a);
    int MAX = a;
    int MIN = a;

    for (int i = 1; i < 10; i++)
    {
        printf("enter number %i: ", i + 1);
        scanf("%d", &a);
        if (a > MAX){
            MAX = a;
        }
        else if (a < MIN){
            MIN = a;
        }
    }

    printf("the (max, min) numbers out of are are (%i, %i)\n", MAX, MIN);
}