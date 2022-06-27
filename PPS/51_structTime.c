#include <stdio.h>

struct time_struct{
    int hours;
    int minutes;
    int seconds;
};

void main(){
    struct time_struct current_time;
    printf("enter [hours, minutes, seconds]: ");
    scanf("%d, %d, %d", &current_time.hours, &current_time.minutes, &current_time.seconds);
    printf("current time is %d : %d : %d\n", current_time.hours, current_time.minutes, current_time.seconds);
}