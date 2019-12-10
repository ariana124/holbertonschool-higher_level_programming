#include "lists.h"

/**
 * check_cycle - function that checks if a singly linked list has a cycle in it
 * @list: linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t **head;
	listint_t *tort;
	listint_t *hare;

	head = *list;

	hare = head;

	while (tort && hare && hare != NULL)
	{
		tort = tort->next;
		hare = hare->next;
	}

	if (tort != hare)
	{
		tort = tort->next;
		hare = hare->next->next;
	}
	else
		tort = head;

	return (0);
}
