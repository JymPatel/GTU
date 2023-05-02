#include <stdio.h>


int main()
{
	int a;
	printf("enter digit: ");
	scanf("%i", &a);
	int ones = a % 10;
	if (ones % 2 == 0)
	{
		printf("it's even!\n");
		return 0;
	}
	printf("it's odd!\n");
	return 0;
}
