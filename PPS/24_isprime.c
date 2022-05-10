#include <stdio.h>

int main(){
	int i;
	printf("enter integer i: ");
	scanf("%d", &i);
	if (i < 2 && i >= 0){
		printf("%i is not a prime number\n", i);
		return 0;
	}
	for (int a = 2; a < i; a++){
		if (i % a == 0){
			printf("%i is not a prime number\n", i);
			return 0;
		}	
	}
	printf("%i is a prime number!\n", i);
	return 0;
}
