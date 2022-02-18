#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int average;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // For each pixel, set each channel to the average of the Red, Green and Blue values
            average = round((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0);
            image[i][j].rgbtRed = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtBlue = average;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE tmp;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width - j; j++)
        {
            // Swap the first pixel with the last one, the second pixel with the second to last one and so on
            tmp = image[i][j];
            image[i][j] = image[i][(width - 1) - j];
            image[i][(width - 1) - j] = tmp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Create a copy of the original image
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    int red, green, blue, counter;

    // Loop over entire image one pixel at a time
    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width; col++)
        {
            red = 0;
            green = 0;
            blue = 0;
            counter = 0;

            // Loop over the pixels around the current pixel
            for (int sub_row = -1; sub_row < 2; sub_row++)
            {
                for (int sub_col = -1; sub_col < 2; sub_col++)
                {
                    // Check for edges and corners
                    if ((row + sub_row >= 0 && row + sub_row < height) && (col + sub_col >= 0 && col + sub_col < width))
                    {
                        // Get the RGB values from the pixels of the copied image and update the counter
                        red += copy[row + sub_row][col + sub_col].rgbtRed;
                        green += copy[row + sub_row][col + sub_col].rgbtGreen;
                        blue += copy[row + sub_row][col + sub_col].rgbtBlue;
                        counter++;
                    }
                }
            }

            // Set the current pixel in the original image to the average of the surrounding pixels
            image[row][col].rgbtRed = round(red/ (float)counter);
            image[row][col].rgbtGreen = round(green / (float)counter);
            image[row][col].rgbtBlue = round(blue / (float)counter);
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
