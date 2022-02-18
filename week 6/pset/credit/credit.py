""" Prompts the user for a credit card number and then reports whether 
    it is a valid American Express, MasterCard, or Visa card number """

import sys


def main():
    # Get number from the user
    number = input("Number: ")
    # Check for invalid card number length
    check_length(number)
    # Calculate Luhn's Algorithm
    checksum = compute_luhns_algo(number)
    # Check the starting numbers to determine the card's brand
    brand = check_start(checksum, number)
    # Prints the brand if valid, else prints invalid
    print(brand)
    

def check_length(number):
    # Number can be of length 13, 15 or 16
    if len(number) != 13 and len(number) != 15 and len(number) != 16:        
        sys.exit("INVALID")
        

def compute_luhns_algo(number):
    # Add number to a list
    number_list = []
    for digit in number:
        number_list.append(int(digit))
    
    sum1 = sum2 = sum_total = 0
    length = len(number_list)

    # Luhn's Algorithm
    for i in range(0, length, 2):
        # Last digit
        digit1 = number_list[length - (1 + i)]
        # Sum of the digits
        sum1 += digit1
        if (length % 2) == 1 and (length - 1) == i:
            break
        else:
            # Second-to-last digit multiplied by 2
            digit2 = (number_list[length - (2 + i)]) * 2
            # Sum of the digit's products
            if digit2 > 9:
                sum2 += (digit2 - 9)
            else:
                sum2 += digit2
    # Checksum
    sum_total = sum1 + sum2
    return sum_total
    

def check_start(checksum, number):
    start = int(number)
    # If checksum is valid check the starting numbers, else return invalid
    if (checksum % 10) == 0:
        while start > 100:
            start //= 10

        if start == 34 or start == 37:
            return "AMEX"
        elif start >= 51 and start <= 55:
            return "MASTERCARD"
        elif (start // 10) == 4:
            return "VISA"
        else:
            return "INVALID"
    else:
        return "INVALID"


if __name__ == '__main__':
    main()