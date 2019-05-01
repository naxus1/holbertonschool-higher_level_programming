#include "lists.h"
#include <stdio.h>

int check_cycle(listint_t *list)
{
        listint_t *aux_list1;
        listint_t *aux_list2;

        aux_list1 = list;
        aux_list2 = list;
        while (aux_list1 != NULL && aux_list2 != NULL && aux_list2->next != NULL)
        {
                aux_list1 = aux_list1->next;
                aux_list2 = aux_list2->next->next;

                if (aux_list1 == aux_list2)
                        return (1);
        }
        return(0);
}
