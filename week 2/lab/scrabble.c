#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Get input words from both players    
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // Print the winner
    if (score1 > score2)
    {        
        printf("Player 1 wins!\n");
    }
    else if (score1 < score2)
    {        
        printf("Player 2 wins!\n");
    }
    else
    {        
        printf("Tie!\n");
    }
}

// Compute and return score for string
int compute_score(string word)
{
    int score = 0;

    // iterate through each letter of the string entered by the user
    for (int i = 0, n = strlen(word); i < n; i++)
    {
        // convert the letter to uppercase in case it is lowercase
        if (islower(word[i]))
        {
            word[i] = toupper(word[i]);
        }

        // iterate through the decimal value of each uppercase letter 
        for (int j = 65; j <= 90; j++)
        {            
            // if the ith letter matches its decimal value
            if (word[i] == j)
            {
                // then subtract 65 so we get the index from 0 to 25
                score += POINTS[j - 65];
            }
        }
    }
    return score;
}