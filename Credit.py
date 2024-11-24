
def luhns_algorith(number):
    results_1 = [] #results_1 is every other digit starting from the second to last digit.
    results_2 = [] #results_2 are the rest of the digits.
    # Extract every other digit starting from the second-to-last digit
    result_1 = str(number)[-2::-2]
    for x in result_1:
        digit_1 = int(x) * 2
        if digit_1 > 9:
            # If the doubled digit is greater than 9, sum its digits
            digit_1 = int(str(digit_1)[0]) + int(str(digit_1)[1])
        else:
            digit_1 = digit_1
        results_1.append(digit_1)
    summed_1 = sum(results_1)
    
    #  Extract every other digit starting from the last digit
    result_2 = str(number)[-1::-2]
    for y in result_2:
        results_2.append(int(y))
    summed_2 = sum(results_2)
    #Sum the results from both lists
    lehms_algrothim = summed_1 + summed_2
    #Check if the last value of that sum is 0
    if str(lehms_algrothim)[-1] == "0":
        return True
    else:
        return False

while True:
#Mastercard validation
    try:
        number =int(input("please enter number: "))
        if len(str(number)) == 16 and (str(number)[0:2] in ["51", "52", "53", "54", "55"]):
            if luhns_algorith(number):
                print("MASTERCARD\n")
            else:
                print("INVALID\n")
        else:
            print("INVALID\n")
    except ValueError:
        print("INVALID\n")

#American Express validation
    try:
        number =int(input("please enter number: "))
        if len(str(number)) == 15 and (str(number)[0:2] in ["34", "37"]):
            if luhns_algorith(number):
                print("AMX\n")
            else:
                print("INVALID\n")
        else:
            print("INVALID\n")
    except ValueError:
        print("INVALID\n")

#Visa validation
    try:
        number =int(input("please enter number: "))
        if len(str(number)) in [13, 16] and (str(number)[0:1] in ["4"]):
            if luhns_algorith(number):
                print("VISA\n")
            else:
                print("INVALID\n")
        else:
            print("INVALID\n")
    except ValueError:
        print("INVALID\n")
