def main():
    # Prompts user for an input between 1 and 8 inclusive
    while True:
        try:
            height = int(input("Height: "))
            if height >= 1 and height <= 8:
                break
        # If the input is not an integer prints an error message
        except ValueError:
            print("Invalid input")
    draw(height)
    
    
# Draws the pyramid          
def draw(height):
    for i in range(height):
        for j in range(height):
            if i + j >= height - 1:
                print("#", end="")
            else:
                print(" ", end="")
        print()


if __name__ == '__main__':
    main()