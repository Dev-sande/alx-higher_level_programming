#include "lists.h"

/**
* check_cycle - performs the same algorithm as the original version,
* but with a cleaner and more readable code structure.
* @list: pointer
* Return: 0 on failure,
* 1 on success
*/
int check_cycle(listint_t *list)
{
listint_t *p2;
listint_t *prev;

p2 = list;
prev = list;
while (list && p2 && p2->next)
{
list = list->next;
p2 = p2->next->next;

if (list == p2)
{
list = prev;
prev =  p2;
while (1)
{
p2 = prev;
while (p2->next != list && p2->next != prev)
{
p2 = p2->next;
}
if (p2->next == list)
break;

list = list->next;
}
return (1);
}
}

return (0);
}

