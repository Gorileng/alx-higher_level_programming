#include "lists.h"

/**
 * check_cycle - check whether the linked list have the cycle
 * @list: the linked list to be checked 
 *
 * Return: 1 when the list have the cycle, 0 when it does not
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}

