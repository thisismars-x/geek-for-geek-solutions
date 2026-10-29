// Retranslation!
//

#include <stdio.h>

struct LinkedList {
    struct LinkedList* next;
    int val;
};

void print_ll(struct LinkedList* ll) {

    struct LinkedList* tmp = ll;
    printf("LinkedList( ");
    while (tmp != NULL) {
        printf("%d, ", tmp->val);
        tmp = tmp->next;
    }
    printf(")\n");

}

struct LinkedList* reverse_ll(struct LinkedList* ll) {

    struct LinkedList* prev = NULL;
    struct LinkedList* curr = ll;

    while (curr != NULL) {
        struct LinkedList* curr_next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = curr_next;
    }

    return prev;

}

int main() {

    struct LinkedList head, node1, node2, node3;
    head.next = &node1;
    node1.next = &node2;
    node2.next = &node3;
    node3.next = NULL;
    head.val = 0;
    node1.val = 1;
    node2.val = 2;
    node3.val = 3;

    print_ll(&head);
    print_ll(reverse_ll(&head));

}
