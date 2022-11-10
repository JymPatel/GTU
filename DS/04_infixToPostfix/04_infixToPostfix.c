#include <stdio.h>
#include <stdbool.h>
#include "04_stack.h"

int main(){
    // get stacks
    struct Stack operators;
    operators.top = -1;
    struct Stack operands;
    operands.top = -1;

    for (int i = 0; i < 100; i++){
        operands.array[i] = '\0';
        operators.array[i] = '\0';
    }


    printf("enter infix equation: ");

    while (true){

        int c = getchar();
        if (c == '\0' || c == '\12'){
            break;
        }


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
                while (peak(&operators) == '^'){
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