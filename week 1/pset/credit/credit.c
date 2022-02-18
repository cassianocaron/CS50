#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long input;
    input = get_long("Number: ");
    
    int length = 0;
    long n = input;
    while (n > 0)
    {
        n /= 10;
        length++;
    }
    
    if (length != 13 && length != 15 && length != 16)
    {
        printf("INVALID\n");
        return 0;
    }

    int sum1 = 0, sum2 = 0, digit1 = 0, digit2 = 0, sum_total;
    long x = input;    
    while (x > 0)
    {
        digit1 = (x % 10);
        sum1 += digit1;        
        digit2 = ((x / 10) % 10) * 2;
        if (digit2 > 9)
        {
            sum2 += (digit2 - 9);
        }
        else
        {
            sum2 += digit2;
        }
        x /= 100;
    }

    sum_total = sum1 + sum2;
    printf("%i\n", sum_total);

    if ((sum_total % 10) == 0)
    {
        long start = input; 
        while (start > 100)  
        {
            start /= 10;
        }

        if (start == 34 || start == 37)
            {
                printf("AMEX\n");
            }
        else if (start >= 51 && start <= 55)
        {
            printf("MASTERCARD\n");
        }
        else if ((start / 10) == 4)
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");        
    }
}