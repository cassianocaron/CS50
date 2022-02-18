""" Implements a program that computes the approximate grade level needed to comprehend some text """


def main():
    # Get text from the user
    text = input("Text: ")

    # Count number of letters, words and sentences
    letters = count_letters(text)
    words =count_words(text) 
    sentences = count_sentences(text)

    # Calculate the Coleman-Liau index
    index = compute_index(letters, words, sentences)

    # Print the grade
    print_grade(index)


def count_letters(text):
    letters = 0
    for char in text:
        # If the character is alphabetical, count letters
        if str.isalpha(char):
            letters += 1
    return letters;


def count_words(text):
    words = 1
    for char in text:
        if char == " ":
            words += 1
    return words


def count_sentences(text):
    sentences = 0
    for char in text:
        if char == '.' or char == '!' or char == '?':
            sentences += 1
    return sentences


def compute_index(letters, words, sentences):
    # Average number of letters per 100 words in the text
    L = (letters * 100 / words)

    # Average number of sentences per 100 words in the text
    S = (sentences * 100 / words)

    # Coleman-Liau index
    index = round(0.0588 * L - 0.296 * S - 15.8)
    return index


# Prints the grade for the given index
def print_grade(index):
    if index < 1:
        print("Before Grade 1")
    elif index < 16:
        print(f"Grade {index}")
    else:
        print("Grade 16+")


if __name__ == '__main__':
    main()