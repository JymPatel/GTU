#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

struct Node {
    int value;
    struct Node *next;
};

struct Node *createNode(int nodeValue) {
    struct Node *node = malloc(sizeof(struct Node));
    node->value = nodeValue;
    return node;
}

struct Node *getLastNode(struct Node *node) {
    while(node->next != NULL) {
        node = node->next;
    }

    return node;
}

struct Node *insertNode(struct Node *head, int position, int insertValue) {
    if (head == NULL){
        head = createNode(insertValue);
        head->next = NULL;
    }
    else if (position == 0) {
        struct Node *newNode = createNode(insertValue);
        newNode->next = head;
        head = newNode;
    }
    else if (position == -1) {
        struct Node *lastNode = getLastNode(head);
        lastNode->next = createNode(insertValue);
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
    printf("3  insert node in way linked list is in ascending order\n");
    printf("4  remove first node\n");
    printf("5  remove node before position specified\n");
    printf("6  remove node after position specified\n");
    printf("7  display linked list\n");
    printf("0  exit\n");

    int input;
    int insertValue;
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
            scanf("%d", &insertValue);
            head = insertNode(head, 0, insertValue);
            break;

            case 2:
            printf("enter value to insert: ");
            scanf("%d", &insertValue);
            head = insertNode(head, -1, insertValue);
            break;

            case 7:
            displayLinkedList(head);
            printf("\n");
            break;
        
            default:
            printf("select from options given above!\n");
            break;
        }
    }
    return 0;
}