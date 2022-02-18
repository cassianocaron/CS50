""" Implement a program that prints out a double half-pyramid of a specified height """


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
    # Draws the pyramid
    draw_pyramid(height)


def draw_pyramid(n):
    # Draws first half
    for i in range(n):
        for j in range(n):
            if i + j >= n - 1:
                print("#", end="")
            else:
                print(" ", end="")
        print("  ", end="")

        # Draws second half
        for k in range(0, i + 1):
            print("#", end="")
        print()


if __name__ == '__main__':
    main()