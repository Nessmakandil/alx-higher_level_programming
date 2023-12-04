#include "lists.h"

/**
 * is_palindrome - checks if a list is palindrome
 * @head: input list
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev = NULL, *mid = NULL;
	int is_palindrome = 1;

	/* Find the middle node of the list */
	while (fast && fast->next)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}

	/* Handle odd-length list by skipping the middle node */
	if (fast)
	{
		mid = slow;
		slow = slow->next;
	}

	/* Reverse the second half of the list */
	prev->next = NULL;
	reverse_list(&slow);

	/* Compare the elements of the first and reversed second half */
	is_palindrome = compare_lists(*head, slow);

	/* Restore the original list by reversing the second half again */
	reverse_list(&slow);

	/* Reconnect the list if it was odd-length */
	if (mid)
	{
		prev->next = mid;
		mid->next = slow;
	}
	else
		prev->next = slow;

	return is_palindrome;
}

/**
 * reverse_list - reverses a linked list
 * @head: input list
 */
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * compare_lists - compares two linked lists for equality
 * @list1: first list
 * @list2: second list
 * Return: 1 if lists are equal, 0 otherwise
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
	while (list1 && list2)
	{
		if (list1->n != list2->n)
			return 0;
		list1 = list1->next;
		list2 = list2->next;
	}

	if (list1 || list2)
		return 0;

	return 1;
}