// Detects if a file is a JPEG

#include <stdio.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    
    // Check usage
    if (argc != 2)
    {
        printf("Usage: ./jpeg image\n");
        return 1;
    }

    // Open file
    FILE *file = fopen(argv[1], "r");
    if (!file)
    {
        printf("Could not open file\n");
        return 1;
    }
    
    // Read first three bytes
    BYTE bytes[4];
    fread(bytes, sizeof(BYTE), 4, file);
    
    // Check first three bytes
    if (bytes[0] == 0xff && bytes[1] == 0xd8 && bytes[2] == 0xff && (bytes[3] & 0xf0) == 0xe0)
    {
        printf("Yes\n");
    }
    else
    {
        printf("No\n");
    }
    
    // Close file
    fclose(file);
}
