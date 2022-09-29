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
        return -1;
    }
    return s->array[(*s).top];
}

int display(struct Stack *s){
    if (s->top == -1){
        printf("stack empty!\n");
        return 1;
    }

    printf("%d\n", s->array[(*s).top]);
    return 0;
}

int main(){
    struct Stack myStack;
    myStack.top = 0;
    myStack.array[0] = 5;
    display(&myStack);
    pop(&myStack);
    display(&myStack);
    push(&myStack, 8);
    display(&myStack);
    pop(&myStack);
    display(&myStack);

    pop(&myStack);
    display(&myStack);
    pop(&myStack);
    display(&myStack);

    for (int i = 0; i < 95; i++){
        push(&myStack, i);
    }
    for (int i = 0; i < 10; i++){
        push(&myStack, i);
        display(&myStack);
    }
    printf("%d\n", peek(&myStack));
    printf("%d\n", peek(&myStack));
    printf("%d\n", peek(&myStack));

    return 0;
}
