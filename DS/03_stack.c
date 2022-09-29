#include <stdio.h>

struct stack{
    int top;
    int array[100];
};

int pop(struct stack *s){
    if (s->top == -1){
        printf("stack empty!\n");
        return -1;
    }

    int element = (*s).array[(*s).top];
    (*s).array[(*s).top] = 0;
    (*s).top--;

    return element;
}


int push(struct stack *s, int element){
    if (s->top == 99){
        printf("stack full, element not added!\n");
        return 1;
    }

    (*s).top++;
    (*s).array[(*s).top] = element;
    return 0;
}


int display(struct stack *s){
    if (s->top == -1){
        printf("stack empty!\n");
        return -1;
    }

    printf("%d\n", s->array[(*s).top]);
    return s->array[(*s).top];
}


int main(){
    struct stack ss;
    ss.top = 0;
    ss.array[0] = 5;
    display(&ss);
    pop(&ss);
    display(&ss);
    push(&ss, 8);
    display(&ss);
    for(int i = 0; i < 111; i++){
        push(&ss, i);
        display(&ss);
    }
    
    return 0;
}
