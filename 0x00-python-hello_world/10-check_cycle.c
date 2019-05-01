#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - review if linked is a list cycles
 * @list: list to review
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *list1;
	listint_t *list2;

	list1 = list;
	list2 = list;
	while (list1 != NULL && list2 != NULL && list2->next != NULL)
	{
		list1 = list1->next;
		list2 = list2->next->next;

		if (list1 == list2)
			return (1);
	}
	return (0);
}
