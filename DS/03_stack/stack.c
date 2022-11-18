#include <stdio.h>

struct Stack{
    int top;
    int array[100];
};

int pop(struct Stack *s){
    if (s->top == -1){
        printf("stack empty!\n");
        return -1;
    }

    int element = (*s).array[(*s).top];
    (*s).array[(*s).top] = 0;
    (*s).top--;

    return element;
}

int push(struct Stack *s, int element){
    if (s->top == 99){
        printf("stack full, element not added!\n");
        return 1;
    }

    (*s).top++;
    (*s).array[(*s).top] = element;
    return 0;
}

int change(struct Stack *s, int index, int element){
    if ((s->top) + 1 < index || index <= 0){
        printf("no element at that index\n");
        return 1;
    }
    
    s->array[s->top - index + 1] = element;
    return 0;
}

int peep(struct Stack *s, int peepindex){
    if ((s->top) + 1 < peepindex){
        printf("only %d elements in stack, can't peep!\n", (s->top) + 1);
        return -1;
    }
    return s->array[(s->top) - peepindex + 1];
}

int peak(struct Stack *s){
    if (s->top < 0){
        printf("stack empty!\n");
        return -1;
    }
    return s->array[(*s).top];
}

int display(struct Stack *s){
    if (s->top == -1){
        printf("stack empty!\n");
        return 1;
    }
    
    for (int i = 0; i <= s->top; i++){
        printf("%d ", s->array[i]);
    }

    printf("\n");
    return 0;
}

int main(){
    struct Stack myStack;
    myStack.top = -1;
    printf("empty stack created!\n\n");
    
    printf("tasks I can do: \n");
    printf("1  push\n");
    printf("2  pop\n");
    printf("3  display\n");
    printf("4  change\n");
    printf("5  peak\n");
    printf("6  peep\n");
    printf("0  exit\n\n");
    
    int input;
    while(1) {
        printf("what would you like to do? ");
        scanf("%d", &input);
        switch(input){
            case 0:
            return 0;
            break;
            
            case 1:
            printf("enter number to push: ");
            int pushint;
            scanf("%d", &pushint);
            push(&myStack, pushint);
            printf("%d pushed sucessfully\n", pushint);
            break;
            
            case 2:
            printf("popping element\n");
            int popint;
            popint = pop(&myStack);
            printf("%d popped from stack\n", popint);
            break;
            
            case 3:
            display(&myStack);
            break;
            
            case 4:
            printf("current stack ...\n");
            if (display(&myStack) != 0){
                break;
            }
               
            int newElement;
            int indexToChange;
            
            printf("enter element place to change: ");
            scanf("%d", &indexToChange);
            
            printf("enter new number: ");
            scanf("%d", &newElement);
            
            if (change(&myStack, indexToChange, newElement) != 0){
                printf("index not yet used!\n");
                break;
            }
            
            printf("element changed sucessfully!\n");
            break;
            
            case 5:
            printf("peak to stack is: %d\n", peak(&myStack));
            break;
            
            case 6:
            printf("enter the place to check value: ");
            int peepplace;
            scanf("%d", &peepplace);
            int peepelement = peep(&myStack, peepplace);
            if (peepelement == -1){
                printf("can't peep!\n");
                break;
            }
            printf("peep element is %d\n", peepelement);
            break;
            
            default:
            printf("enter number from 0-6\n");
        }
        printf("\n");
    }

    return 0;
}
