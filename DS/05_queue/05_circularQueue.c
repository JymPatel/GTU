#include <stdio.h>

struct Queue {
    int first;
    int last;
    char array[100];
};

int main() {
    struct Queue queue;
    queue.first = -1;
    queue.last = -1;
    return 0;
}