#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = "HI!";
    printf("%c\n", *s);
    printf("%c\n", *(s+1));
    printf("%c\n", *(s+2));
    printf("%i\n", *(s+100000));
}