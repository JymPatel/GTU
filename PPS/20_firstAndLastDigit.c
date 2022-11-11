#include <stdio.h>

int main(){
	int i;
	printf("enter integer i: ");
	scanf("%d", &i);
	int lastD = i % 10;
	int firstD;
	while (i > 0){
		firstD = i;
		i = i / 10;
	}
	printf("sum of first and last digit is %i\n", lastD + firstD);
	return 0;
}

