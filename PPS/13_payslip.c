#include <stdio.h>

int main()
{
    int basic;
    printf("enter basic: ");
    scanf("%d", &basic);
    // all things
    float da = basic * 0.10;
    float hra = basic * 0.075;
    float ma = 300;
    float pf = basic * 0.125;
    float gross = basic + da + hra + ma;
    float nt = gross - pf;
    // print
    printf("BASIC: %i\nDA   : %.*f\nHRA  : %.*f\nMA   : %.*f\nPROFIT %.*f\nGROSS: %.*f\nNET  : %.*f\n", basic, da, 3, hra, 3, ma, 3, pf, 3, gross, 3, nt, 3);
    return 0;
}