// Recovers JPG files from a SD card image

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

// Number of bytes of each block to read
const int BLOCK = 512;
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // Check for incorrect usage
    if (argc != 2)
    {
        printf("Usage: ./recover image\n");
        return 1;
    }

    // Open the input file
    FILE *card = fopen(argv[1], "r");
    if (argv[1] == NULL)
    {        
        printf("Could not open file\n");
        return 1;
    }

    // Create a buffer to store the data read from the input file
    BYTE buffer[BLOCK];
    // String to store the filenames
    char filename[8];
    // Initialize the output file
    FILE *image = NULL;
    // Update the number of jpgs found so far
    int jpg_counter = 0;

    // Repeat until the end of input file
    while (fread(buffer, sizeof(buffer), 1, card) == 1)
    {
        // If the header is the start of a jpg
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // If is the first jpg found so far
            if (jpg_counter == 0)
            {
                // Create the first file
                sprintf(filename, "%03i.jpg", jpg_counter);
                // Open the file
                image = fopen(filename, "w");
                // Write the first block
                fwrite(buffer, sizeof(buffer), 1, image);
                // Update counter
                jpg_counter++;
            }
            // If already found a jpg
            else
            {
                // Close the previous file
                fclose(image);
                // Create a new file with the next name (000.jpg, 001.jpg, 002.jpg...)
                sprintf(filename, "%03i.jpg", jpg_counter);
                // Open the file
                image = fopen(filename, "w");
                // Write the first block
                fwrite(buffer, sizeof(buffer), 1, image);
                //Update counter
                jpg_counter++;
            }
        }
        // If the header is not the start of a new jpg
        else if (jpg_counter > 0)
        {
            // Keep writing blocks
            fwrite(buffer, sizeof(buffer), 1, image);
        }
    }
    // Close files
    fclose(image);
    fclose(card);
    return 0;
}