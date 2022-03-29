import os


def check_typing(number_of_tries, original):
    if not original:
        raise ValueError("Variable 'original' is empty. Enter password to test whether you can type it correctly")   
    correct = 0
    for i in range(number_of_tries):
        os.system('cls' if os.name == 'nt' else 'clear')
        password = input("\nEnter:\n")
        if password == original:
            correct += 1
            print("You entered the password correctly! Congratulations! Great job!")
        else:
            print(f"You haven't entered the password correctly. Now compare and find mistakes:\n{original}\n{password}")
        input("\nPress 'Enter' to continue")
    print(f"\nYou entered your password correctly {correct}/{number_of_tries} times.")
    

if __name__ == '__main__':
    number_of_tries = 4
    # in variable 'original' type your password to see whether you can type it without errors
    original = ""
    check_typing(number_of_tries, original)