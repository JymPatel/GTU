#include <stdio.h>

int main()
{
    int marks;
    printf("what's the marks you scored out of 100? ");
    scanf("%d", &marks);
    if (marks >= 23){
        printf("you passed your exams!!\n");
        return 0;
    }
    printf("good luck for next time!! sorry but you failed\n");
    return 0;
}