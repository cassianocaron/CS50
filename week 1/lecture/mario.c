#include <stdio.h>
#include <cs50.h>

int main (void)
{
    // Get postive integer from the user
    int n;
    do
    {
        n = get_int("Width: ");
    }
    while (n < 1);
    
    //Print out that many questions marks
    for (int i = 0; i < n; i++)
    {
        printf("?");
    }
    printf("\n");
}