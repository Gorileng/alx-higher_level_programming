#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - the singly linked list
 * @p: the integer
 * @next: next node will be pointed 
 *
 * Description: the singly linked list node of structure
 * for the Holberton project
 */
typedef struct listint_s
{
	int p;
	struct listint_s *next;
} listint_t;

void free_listint(listint_t *head);
int check_cycle(listint_t *list);
size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int p);

#endif
