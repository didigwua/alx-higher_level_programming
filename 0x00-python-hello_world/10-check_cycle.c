#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - function in C that checks if a singly linked list has
 *  a cycle in it
 * @list: head of singly linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *check;

	if (!list)
		return (0);

	while (list)
	{
		check = list;
		list = list->next;
		if (check <= list)
			return (1);
	}
	return (0);
}
