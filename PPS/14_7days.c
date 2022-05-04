#include <stdio.h>

int main()
{
    int i;
    do
    {
        printf("enter no. from 1-7: ");
        scanf("%d", &i);
    }
    while (i > 7 || i < 1);
    switch (i)
    {
    case 1:
        printf("Sunday\n");
        break;
    case 2:
        printf("Monday\n");
        break;
    case 3:
        printf("Tuesday\n");
        break;
    case 4:
        printf("Wednesday\n");
        break;
    case 5:
        printf("Thursday\n");
        break;
    case 6:
        printf("Friday\n");
        break;
    case 7:
        printf("Saturday\n");
        break;
    default:
        break;
    }
    
}