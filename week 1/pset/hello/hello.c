#include <stdio.h>
#include <cs50.h>

int main(void)
{
    string name = get_string("What is your name? "); // Gets input from the user
    printf("Hello, %s\n", name); // Prints Hello + name the user typed in
}