#Credit card validator
This program checks for the validity of credit card numbers using Luhn's Algorithm and identifies the type of card based on its number.

Features
Validates Card Numbers: Checks if a card number adheres to the rules of Luhn's Algorithm.
Identifies Card Type:
AMX (American Express): Recognizes valid AMX card numbers starting with 34 or 37 and having 15 digits.
MASTERCARD: Recognizes valid Mastercard numbers starting with 51, 52, 53, 54, or 55 and having 16 digits.
VISA: Recognizes valid Visa card numbers starting with 4 and having 13, 15, or 16 digits.
Handles Invalid Inputs: Returns 'INVALID' if the number doesn't meet any of the criteria.


How the program works
This program prompts the user to enter a credit card number.
It then uses Luhn's algorithm to show if the card number is valid or not.
Every other digit starting from the second-to-last is doubled.
Digits greater than 9 are split and summed.
The sum of the transformed digits and the untouched digits is calculated.
The program determines the validity of the card and identifies its type:
Valid: Returns the card type (AMX (American Express), MASTERCARD, or VISA).
Invalid: Returns 'INVALID'.

License
This project is open-source and available under the MIT License.