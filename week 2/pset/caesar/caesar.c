#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

bool validate(string key);
void encipher(int key, string plaintext);

int main(int argc, string argv[])
{
    // If the user enters more than 2 or no command-line argument at all returns an error message
    if (argc == 2)
    {
        string key = argv[1];
        if (validate(key) == true)
        {
            // Converts the command-line argument to an integer
            int k = atoi(key);
    
            // Get input from the user
            string plaintext = get_string("plaintext: ");    
            printf("ciphertext: ");
            encipher(k, plaintext);
        }
        else
        {
            printf("Key must contain only digits\n");
            return 1;
        }
    }
    else
    {
        printf("USage: ./caesar key\n");
        return 1;
    }
}

bool validate(string key)
{
    // Checks if all the characters entered are digits
    for (int i = 0, len = strlen(key); i < len; i++)
    {
        if (!isdigit(key[i]))
        {
            return false;
        }
    }
    return true;
}

void encipher(int key, string plaintext)
{
    // Iterate over each character of the plaintext
    for (int i = 0, len = strlen(plaintext); i < len; i++)
    {
        // If it is lowercase, shift the characters for the given key
        if (isupper(plaintext[i]))
        {
            printf("%c", ((plaintext[i] - 'A' + key) % 26) + 'A');
        }
        // If it is uppercase, shift the characters for the given key
        else if (islower(plaintext[i]))
        {
            printf("%c", ((plaintext[i] - 'a' + key) % 26) + 'a');
        }
        else // If the character is not an alphabetical character, leave it untouched
        {            
            printf("%c", plaintext[i]);
        }
    }
    printf("\n");
}