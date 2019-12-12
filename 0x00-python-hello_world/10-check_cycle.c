#include "lists.h"

/**
 * check_cycle - function that checks if a singly linked list has a cycle in it
 * @list: linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tort = NULL;
	listint_t *hare = NULL;

	tort = list;
	hare = list;

	if (list == NULL)
		return (0);

	do {
		if (hare->next == NULL || hare->next->next == NULL)
			return (0);

		tort = tort->next;
		hare = hare->next->next;
	} while (hare != tort);

	return (1);
}
