#include <stdio.h>
#include <stdlib.h>

int main(){

	int n;
	printf("enter number of characters: ");
	scanf("%d", &n);
	char *pointer;
	pointer = (char *)malloc(n * sizeof(char));
	printf("enter char: ");

	for (int i = 0; i < n; i++){
		pointer[i] = getchar();
	}
	printf("%s\n", pointer);

	free(pointer);

	return(0);
}
