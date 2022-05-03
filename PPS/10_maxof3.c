#include <stdio.h>

int main()
{
	// get integers
	int a, b, c;
	printf("a? ");
	scanf("%i", &a);
	printf("b? ");
	scanf("%i", &b);
	printf("c? ");
	scanf("%i", &c);
	// check for greatest
	if (a > c && a > b)
	{
		printf("%i is greatest number", a);
	}
	else if (b > c)
	{
		printf("%i is greatest number", b);
	}
	else
	{
		printf("%i is greatest number", c);
	}
	printf("\n");
	return 0;
}
