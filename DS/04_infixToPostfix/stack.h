#include <stdio.h>

struct Stack{
    int top;
    char array[100];
};

char pop(struct Stack *s){
    if (s->top == -1){
        return '\0';
    }

    char element = (*s).array[(*s).top];
    (*s).array[(*s).top] = '\0';
    (*s).top--;

    return element;
}

int push(struct Stack *s, char element){
    if (s->top == 99){
        return 1;
    }

    (*s).top++;
    (*s).array[(*s).top] = element;
    return 0;
}

int change(struct Stack *s, int index, int element){
    if ((s->top) + 1 < index || index <= 0){
        return 1;
    }
    
    s->array[s->top - index + 1] = element;
    return 0;
}

char peep(struct Stack *s, int peepindex){
    if ((s->top) + 1 < peepindex){
        return '\0';
    }
    return s->array[(s->top) - peepindex + 1];
}

char peak(struct Stack *s){
    if (s->top < 0){
        return '\0';
    }
    return s->array[(*s).top];
}

int display(struct Stack *s){
    if (s->top == -1){
        return 1;
    }
    
    for (int i = 0; i <= s->top; i++){
        printf("%c ", s->array[i]);
    }

    printf("\n");
    return 0;
}