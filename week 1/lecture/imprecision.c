#include <stdio.h>
#include <cs50.h>

int main(void)
{
    float x = get_float("x: ");
    float y = get_float("y: ");
    {
        printf("%.02f\n", x / y);
    }
}