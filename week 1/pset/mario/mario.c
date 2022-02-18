#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Get input from the user and keep asking in case the user enters an invalid input
    int input;
    do
    {
        input = get_int("Height: ");
    }
    while (input < 1 || input > 8); 

    for (int i = 0; i < input; i++)
    {
        for (int j = 0; j < input; j++)
        {
            // Check if the index is greater than input, so it right alingns the pyramid
            if (i + j >= input - 1) 
            {
                printf("#");
            }
            else
            {
                printf(" ");
            }
        }
        // Prints two spaces in the middle of the pyramid
        printf("  "); 

        // Draw the right half of the pyramid
        for (int k = 0; k <= i; k++) 
        {
            printf("#");
        }

        printf("\n");
    }
}