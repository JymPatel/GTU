#include <stdio.h>
#include "04_stack.h"

int main(){
    struct Stack operators;
    operators.top = -1;
    struct Stack operands;
    operands.top = -1;

    char string[100];
    printf("enter infix equation: ");

    for (int i = 0; i < 100; i++){
        operands.array[i] = '\0';
        operators.array[i] = '\0';
        string[i] = '\0';
    }

    scanf("%s", string);


    for (int i = 0; i < 100; i++){
        int c = string[i];


        if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z')){
            push(&operands, c);
        }

        else if (c == '+' || c == '-'){
            if (peak(&operators) == '\0'){
                push(&operators, c);
            }

            else{
                while (peak(&operators) != '\0'){
                    push(&operands, pop(&operators));
                }
                push(&operators, c);
            }
        }
        
        else if (c == '*' || c == '/'){
            if (peak(&operators) == '\0' || peak(&operators) == '+' || peak(&operators) == '-'){
                push(&operators, c);
            }

            else{
                while (peak(&operators) != '\0' && peak(&operators) != '+' && peak(&operators) != '-'){
                    push(&operands, pop(&operators));
                }
                push(&operators, c);
            }
        }
        
        else if (c == '^'){
            if (peak(&operators) != '^'){
                push(&operators, c);
            }

            else{
                while (peak(&operators) != '*' && peak(&operators) != '/' && peak(&operators) != '\0' && peak(&operators) != '+' && peak(&operators) != '-'){
                    push(&operands, pop(&operators));
                }
                push(&operators, c);
            }
        }
    }

    while (peak(&operators) != '\0'){
        push(&operands, pop(&operators));
    }

    display(&operands);
    display(&operators);

    return 0;
}