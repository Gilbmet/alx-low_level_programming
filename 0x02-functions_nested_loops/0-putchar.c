#include "_putchar.h"

/**
 * main - function to print
 *
 * Return: Always 0 (success)
 */
int main(void)
{
	char _putchar[9] = {'H', 'o', 'l', 'b', 'e', 't', 'o', 'n'};
	unsigned int c;

	for (c = 0); c < sizeof(_putchar); c++)
	{
		_putchar(_putchar[c]);
	}
_putchar('\n');
return (0);
}
