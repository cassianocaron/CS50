def main():
    while True:
        height = int(input("Height: "))
        if height >= 1 and height <= 10000:
            break

    for i in range(height):
        for j in range(height):
            if i + j >= height - 1:
                print("#", end="")
            else:
                print(" ", end="")
        print(" ", end="")

        for k in range(0, i + 1):
            print("#", end="")
        print()


if __name__ == '__main__':
    main()