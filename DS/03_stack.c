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
    if (s->top < index || index < 0){
        printf("no element at that index\n");
        return 1;
    }
    
    s->array[index] = element;
    return 0;
}

int peek(struct Stack *s){
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
    printf("5  peek\n");
    printf("0  exit\n\n");
    
    int input;
    while (0 == 0){
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
            printf("%d popped from stack", popint);
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
            printf("peek to stack is: %d", peek(&myStack));
            break;
            
            default:
            printf("enter number from 0-5\n");
        }
        printf("\n");
    }

    return 0;
}
