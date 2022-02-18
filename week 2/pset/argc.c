#include <stdio.h>
#include <cs50.h>
#include <string.h>

typedef struct
{
    /* data */
};


// prints all characters of a giving CLA(command line argument) at index 1 in this case
int main(int argc, string argv[])
{
    for (int i = 0, n = strlen(argv[1]); i < n; i++)
    {
        printf("%c\n", argv[1][i]);
    }
    printf("\n");
}
