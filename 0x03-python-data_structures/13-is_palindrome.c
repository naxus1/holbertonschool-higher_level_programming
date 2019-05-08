#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *aux_head, *iter_list;
	int cont = 0, j = 0, aux_len = 0, i;

	aux_head = *head;

	while (aux_head != NULL)
	{
		cont++;
		aux_head = aux_head->next;
	}
	aux_len = cont / 2;
	aux_head = *head;
	while (j < aux_len)
	{
		i = 0;
		iter_list = aux_head;

		while (i < (cont - 1))
		{
			i++;
			iter_list = iter_list->next;
		}
		if (aux_head->n != iter_list->n )
		{
			return (0);
		}
		i = 0;
		cont = cont - 2;
		aux_head = aux_head->next;
		j++;
	}
	return (1);
}
