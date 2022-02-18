#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    // Get a float number from user
    float dollars;
    do
    {
        dollars = get_float("Change owed: ");
    }
    while (dollars <= 0);
    
    // Convert float to int and then multiple by 100
    int cents = round(dollars * 100);
    int coins = 0;
    
    // Each while loop checks if the cents are more or equal than the value of each coin
    while (cents >= 25)
    {
        cents -= 25;
        coins++;
    }
    while (cents >= 10)
    {
        cents -= 10;
        coins++;
    }
    while (cents >= 5)
    {
        cents -= 5;
        coins++;
    }
    while (cents >= 1)
    {
        cents -= 1;
        coins++;
    }
    // Prints the number of coins needed
    printf("Coins: %i\n", coins);
}
