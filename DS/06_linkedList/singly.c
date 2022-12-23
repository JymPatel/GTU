#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

struct Node {
    int value;
    struct Node *next;
};

struct Node *createNode() {
    struct Node *node = malloc(sizeof(struct Node));
    return node;
}

struct Node *insertNode(struct Node *head, int position, int insertValue) {
    if (head == NULL){
        head = createNode();
        head->value = insertValue;
        head->next = NULL;
    }
    else if (position == 0) {
        struct Node *newNode = createNode();
        newNode->next = head;
        newNode->value = insertValue;
        head = newNode;
    }
    return head;
}

int displayLinkedList(struct Node *head) {
    if (head == NULL) {
        printf("empty linked list!\n");
        return 1;
    }
    printf("%d", head->value);
    struct Node *node = head->next;
    while (node != NULL) {
        printf(" -> %d", node->value);
        node = node->next;
    }
}


int main() {
    struct Node *head = NULL;

    printf("program started!\n\n");
    
    printf("tasks I can do: \n");
    printf("1  insert at front\n");
    printf("2  insert at end\n");
    printf("3  todo\n");
    printf("4  remove first node\n");
    printf("5  remove node before position specified\n");
    printf("6  remove node after position specified\n");
    printf("7  display linked list\n");
    printf("0  exit\n");

    int input;
    while(true) {
        printf("\n");
		printf("what would you like to do? ");
        scanf("%d", &input);
        switch (input) {
            case 0:
            return 0;
            break;

            case 1:
            printf("enter value to insert: ");
            int insertValue;
            scanf("%d", &insertValue);
            head = insertNode(head, 0, insertValue);
            break;

            case 7:
            displayLinkedList(head);
            printf('\n');
            break;
        
            default:
            printf("select from options given above!\n");
            break;
        }
    }
    return 0;
}