#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdlib.h>

/**
 * struct listint_s - the singly linked list
 * @n: the integer
 * @next: point to next node
 *
 * Description: the singly linked list node of structure
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
void free_listint(listint_t *head);
int is_palindrome(listint_t **head);
listint_t *add_nodeint_end(listint_t **head, const int n);

#endif 

