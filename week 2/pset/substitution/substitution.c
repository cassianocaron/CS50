#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

bool validate(string key);
void encipher(string key, string plaintext);

int main(int argc, string argv[])
{
    if (argc == 2) // Check if only one command-line argument is entered
    {
        string key = argv[1];
        if (validate(key) == true)
        {
            string plaintext = get_string("plaintext: "); // Get plaintext from the user
            printf("ciphertext: ");
            encipher(key, plaintext);
        }
    }
    else
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
}

// Validates the key
bool validate(string key)
{
    if (strlen(key) == 26)
    {
        // Array of all zeros to allow checking for duplicate characters
        int count[26] = {0};

        // Iterate over each character of the key
        for (int i = 0, len = strlen(key); i < len; i++)
        {
            // If key[i] is not an alphabetical character or it appears more than once, returns false
            if (!isalpha(key[i]) || count[toupper(key[i]) - 'A']++ != 0)
            {
                printf("Key must contain only letters and each letter exactly once\n");
                return false;
            }
        }
        return true;
    }
    else
    {
        printf("Key must contain 26 characters\n");
        return false;
    }
}

// Enciphers the plaintext for the given key
void encipher(string key, string plaintext)
{
    // Iterate over each character of the plaintext
    for (int i = 0, len = strlen(plaintext); i < len; i++)
    {
        if (isupper(plaintext[i]))
        {
            // If the character is uppercase, shift it with the corresponding uppercase letter from the key
            printf("%c", toupper(key[plaintext[i] - 'A']));
        }
        else if (islower(plaintext[i]))
        {
            // If the character is lowercase, shift it with the corresponding lowercase letter from the key
            printf("%c", tolower(key[plaintext[i] - 'a']));
        }
        else
        {
            // If the character is not alphabetical, do not change it
            printf("%c", plaintext[i]);
        }
    }
    printf("\n");
}