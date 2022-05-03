#include <stdio.h>


int main()
{
	char c;
	printf("enter char: ");
	scanf("%c", &c);
	if (c >= 97 && c <= 122)
	{
		printf("small character\n");
	}
	else if (c >= 65 && c <= 90)
	{
		printf("capital\n");
	}
	else if (c >= 48 && c <= 57)
	{
		printf("digit\n");
	}
	else
	{
		printf("special character\n");
	}
	return 0;
}
