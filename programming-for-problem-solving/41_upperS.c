#include <stdio.h>
#include <string.h>

int main(){
	char stringS[20];
    printf("enter string: ");
    scanf("%s", stringS);
    for (int i = 0; i < 20; i++){
        if (stringS[i] <= 122 && stringS[i] >= 97){
            stringS[i] -= 32;
        }
    }
    printf("%s\n", stringS);
	return 0;
}
