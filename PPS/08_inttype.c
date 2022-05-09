#include <stdio.h>


int main(){
    int a;
    printf("enter an integer a: ");
    scanf("%d", &a);
    printf("%i is a ", a);
    if (a > 0){
        printf("positive number\n");
        return 0;
    }
    else if (a < 0){
        printf("negative number\n");
        return 0;
    }
    else{
        printf("neither -ve nor +ve\n");
        return 0;
    }
}