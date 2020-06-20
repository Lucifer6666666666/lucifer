def input_check_first():
    global num1
    while True:
        try:
            num1 = int(input('Enter the first number between 0-255: '))
            if 0 <= num1 <= 255:
                break
            elif num1 < 0:
                print("Please enter positive number within range(0-255)")
            else:
                print("Please enter number between 0-255")
        except ValueError:
            print("Provide an integer value...")
            continue
    return


def input_check_second():
    global num2
    while True:
        try:
            num2 = int(input('Enter the second number between 0-255: '))
            if 0 <= num2 <= 255:
                break
            elif num2 < 0:
                print("Please enter positive number within range(0-255)")
            else:
                print("Please enter number between 0-255")
        except ValueError:
            print("Provide an integer value...")
            continue
    return
