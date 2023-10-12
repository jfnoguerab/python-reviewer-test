import sys
import config

def main():
    ask_again = True
    while(ask_again):
        if sys.version_info.major <= 2:
            a = raw_input("Enter the numerator: ")
            b = raw_input("Enter the denominator: ")
        else:
            a = input("Enter the numerator: ")
            b = input("Enter the denominator: ")
        result = perform_division(a,b)
        if result is not None:
            print(result)
        if sys.version_info.major <= 2:
            ask_again = raw_input("Do you want to perform another operation? Enter yes or no: ")
        else:
            ask_again = input("Do you want to perform another operation? Enter yes or no: ")
        if(ask_again == 'yes'):
            ask_again = True
        else:
            ask_again = False
            print("You performed " + str(config.operations_count) + " operations, bye!")

def perform_division(a: int,b: int):
    try:
        config.operations_count += 1
        return int(a)/int(b)
    except ZeroDivisionError as e:
        print("Error: Cannot divide by zero")
    except Exception:
        print("An error occurred, remember only numbers are allowed!")
        pass

main()