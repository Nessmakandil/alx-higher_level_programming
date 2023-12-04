#include "lists.h"

/**
 * is_palindrome - checks if a list is palindrome
 * @head: input list
 * Return: 0 or 1
 */

int is_palindrome(listint_t **head)
{
	int count = 0, i = 0, j, *num;
	listint_t *list = *head;


	while (list)
	{
		count++;
		list = list->next;
	}
	num = malloc(sizeof(int) * count);
	list = *head;

	while (i < count)
	{
		num[i] = list->n;
		list = list->next;
		i++;
	}
	
	free(list);
	j = count - 1;
	for (i = 0; i < round(count / 2); i++)
	{
		if (num[i] == num[j])
		{
			j--;
		}
		else
		{
			free(num);
			return (0);
		}
	}
	free(num);
	return (1);
}