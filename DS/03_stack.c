#include <stdio.h>

struct stack{
    int top;
    int array[100];
};

int pop(struct stack *s){

    if (s->top == -1){
        printf("stack empty!\n");
        return 0;
    }

    int element = (*s).array[(*s).top];
    (*s).array[(*s).top] = 0;
    (*s).top -= 1;

    return element;
}

int 

int main(){
    struct stack ss;
    ss.top = 0;
    ss.array[0] = 5;
    printf("%d %d %d\n", pop(&ss), ss.top, ss.array[0]);
    printf("%d %d", ss.top, ss.array[0]);\
        printf("%d %d %d\n", pop(&ss), ss.top, ss.array[0]);

    return(0);
}
