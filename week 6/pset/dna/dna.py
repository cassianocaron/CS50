""" Implement a program that identifies a person based on their DNA """


from csv import DictReader
from re import findall
from sys import exit, argv


def main():
    # Ensure correct usage
    if len(argv) != 3:
        exit("Usage: python dna.py data.csv sequence.txt")

    database = []
    # Read database into memory from file
    with open('databases/' + argv[1], "r") as f1:
        reader = DictReader(f1)
        # Store the first line in a list
        header = reader.fieldnames
        for row in reader:
            # Cast the STRs values to int
            for i in range(1, len(header)):
                row[header[i]] = int(row[header[i]])
            # Add each line to a dictionary inside a list
            database.append(row)

    # Read sequence into memory from file
    with open('sequences/' + argv[2], "r") as f2:
        sequence = f2.read()

    # Returns a dictionary where each key is a STR and the 
    # value is the maximum number of times the STR repeats
    str_count = str_repeats(header, sequence)

    # Prints the person's name if there's a match, else prints "No match"
    print_result(str_count, header, database)


def print_result(str_count, header, database):
    for i in range(len(database)):
        count = 0
        for j in range(1, len(header)):
            # If the STR count matches with the database
            if str_count[header[j]] == database[i][header[j]]:
                # Counts how many STRs match with the database
                count += 1
                # If all STRs for the person match with the database
                if count == (len(header) - 1):
                    # Print the person's name
                    print(database[i]['name'])
                    return
    # If we get here, no matches were found
    print("No match")


def str_repeats(header, sequence):
    str_count = {}
    for i in range(1, len(header)):
        # Regular expression to find all the matches of the STR in the given sequence
        match = findall(f'(?:{header[i]})+', sequence)        
        # If no matches are found for the given STR, set count to 0
        if not match:
            count = 0
        else:
            # Find the longest repeated run
            longest = max(match, key=len)            
            # Count how many times the longest run repeats
            count = int(len(longest) / len(header[i]))            
        # Add to a dictionary the STR as keys and the count as values
        str_count[header[i]] = count
    return str_count


if __name__ == '__main__':
    main()