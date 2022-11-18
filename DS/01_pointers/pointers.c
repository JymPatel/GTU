#include <stdio.h>


int add100(int *p){
	*p += 100;
	return(*p);
}

int addAB(int p, int q){
	return(p + q);
}


int main(){
	int A;
	printf("enter number (A): ");
	scanf("%d", &A);
	printf("A = %d (using call by reference)\n", add100(&A));
	int B;
	printf("enter number (B): ");
	scanf("%d", &B);
	printf("A + B = %d (using call by value)\n", addAB(A, B));
	return(0);
}
