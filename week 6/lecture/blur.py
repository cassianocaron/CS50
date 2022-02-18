from PIL import Image, ImageFilter


def main():
    before = Image.open("yard.bmp")
    after = before.filter(ImageFilter.BoxBlur(1))
    after.save("blur_yard.bmp")
    


if __name__ == '__main__':
    main()