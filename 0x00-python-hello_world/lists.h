#ifndef LISTS
#define LISTS

#include <stdlib.h>
/**
* struct listint_s - function name -singly linked list
* @n: integer
* @next: points to the next node
* Description: prints all the values stored in the list
* and returns the number of nodes in the list.
*/
typedef struct listint_s
{
int n;
struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif

