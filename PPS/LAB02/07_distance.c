#include <stdio.h>

int main()
{
	float u, t, a;
	printf("enter inital velocity, u?: ");
	scanf("%f", &u);
	printf("enter time, t?: ");
	scanf("%f", &t);
	printf("enter acceleration, a?: ");
	scanf("%f", &a);
	float distance = u * t + 0.5 * a * t * t;
	printf("distance travelled is  %f\n", distance);
}