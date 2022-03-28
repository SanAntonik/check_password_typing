def check_typing(number_of_tries, original):
    correct = 0
    for i in range(number_of_tries):
        password = input("\nEnter: ")
        if password == original:
            correct += 1
            print("You entered the password correctly! Congratulations! Great job!")
        else:
            print(f"You haven't entered the correct password. Now compare and find mistakes:\n{original}\n{password}")
    print(f"You entered your password correctly {correct}/{number_of_tries} times.")
    

if __name__ == '__main__':
    number_of_tries = 4
    original = ""
    check_typing(number_of_tries, original)