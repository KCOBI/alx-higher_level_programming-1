#include <stdio.h>
#include <stdlib.h>

/**
  * insert_node - inserts a number into a sorted singly linked list.
  * @head: pointer to the pointer of the list.
  * @number: number to be inserted.
  *
  * Return: address f the new node or NULL if it failed.
  */
 typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *before, *new_Node;

	new_Node = malloc(sizeof(listint_t));
	if (new_Node != NULL)
	{
		new_Node->n = number;
		if (*head == NULL || (*head)->n >= new_Node->n)
		{
			new_Node->next = *head;
			*head = new_Node;
			return (new_Node);
		}
		else
		{
			before = *head;
			while (before->next != NULL && before->next->n < new_Node->n)
				before = before->next;
			new_Node->next = before->next;
			before->next = new_Node;
			return (new_Node);
		}
	}
	return (NULL);
}



size_t print_listint(const listint_t *h)
{
    const listint_t *current;
    unsigned int n; /* number of nodes */

    current = h;
    n = 0;
    while (current != NULL)
    {
        printf("%i\n", current->n);
        current = current->next;
        n++;
    }

    return (n);
}

listint_t *add_nodeint_end(listint_t **head, const int n)
{
    listint_t *new;
    listint_t *current;

    current = *head;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = n;
    new->next = NULL;

    if (*head == NULL)
        *head = new;
    else
    {
        while (current->next != NULL)
            current = current->next;
        current->next = new;
    }

    return (new);
}

void free_listint(listint_t *head)
{
    listint_t *current;

    while (head != NULL)
    {
        current = head;
        head = head->next;
        free(current);
    }
}

int main(void)
{
    listint_t *head;

    head = NULL;
    add_nodeint_end(&head, 0);
    add_nodeint_end(&head, 1);
    add_nodeint_end(&head, 2);
    add_nodeint_end(&head, 3);
    add_nodeint_end(&head, 4);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 402);
    add_nodeint_end(&head, 1024);
    print_listint(head);

    printf("-----------------\n");

    insert_node(&head, 27);

    print_listint(head);

    free_listint(head);

    return (0);
}