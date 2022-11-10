#include <stdio.h>


struct Queue {
	int last;
	char array[100];
};

int insert(struct Queue *q, char insertElement) {
	if(q->last == 99){
		return 1;
	}

	q->array[(q->last) + 1] = insertElement;
	q->last++;
	return 0;
}


int main(){
	// initiate queue
	struct Queue queue;
	queue.last = -1;
	for (int i = 0; i < 100; i++) {
		queue.array[i] = '\0';
	}

	printf("empty queue created!\n\n");
    
    printf("tasks I can do: \n");
    printf("1  insert\n");
    printf("2  delete\n");
    printf("3  display\n");
    printf("0  exit\n\n");

	int input;
	while(1) {
		printf("what would you like to do? ");
        scanf("%d", &input);
        switch(input) {
			case 0:
			return 0;
			
			case 1:
			printf("enter character to insert: ");
			char insertElement;
			scanf("%c", &insertElement);
			int insertStatus = insert(&queue, insertElement);
			if(!insertStatus) {
				printf("%c inserted sucessfilly\n", insertElement);
			}
			else if(insertStatus == 1){
				printf("queue full element not inserted!!\n");
			}
		}
	}
	return(0);
}