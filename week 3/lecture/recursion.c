#include <stdio.h>

long int fact (int n);

int main(void)
{
    int n;
    printf("Factorial: ");
    scanf("%d", &n);
    printf("%d! = %ld\n", n, fact(n));
}

long int fact (int n)
{
    if (n == 1)
    {
        return 1;
    }
    else
    {
        return n * fact(n - 1);
    }
}