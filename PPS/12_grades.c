#include <stdio.h>


int main()
{
    int grades;
    printf("enter grades you got: ");
    scanf("%i", &grades);
    // else if ladder
    if (grades > 100){
        printf("you got more than possible\n");
    }
    else if (grades >= 80){
        printf("Grade: Distinction");
    }
    else if (grades >= 60){
        printf("Grade: First Class");
    }
    else if (grades >= 40){
        printf("Grade: Second Class");
    }
    else{
        printf("You Failed!!");
    }
    printf("\n");
    return 0;
}