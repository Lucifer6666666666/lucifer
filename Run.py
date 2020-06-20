import Input
import Conversion
import Module

while True:
    Input.input_check_first()
    Input.input_check_second()
    print("First Number in Decimal is : ", Input.num1)
    print("Second Number in Decimal is: ", Input.num2)
    bin1 = Conversion.decimal_to_binary(Input.num1)
    bin2 = Conversion.decimal_to_binary(Input.num2)
    print("First Number in Binary is  : ", bin1)
    print("Second Number in Binary is : ", bin2)
    binary_add = Module.add(bin1, bin2)
    if len(binary_add) <= 8:
        print("Sum of numbers in Binary   : ", binary_add)
        dec1 = Conversion.binary_to_decimal(binary_add)
        print('Sum of number in Decimal   : ', dec1)
    else:
        print('This is only 8-bit adder and cannot show value more than 8-bit binary')
    choice = input("Enter Y/y to continue to input number: ")
    if choice.lower() == "y":
        print("         !!!!!!!Peforming Addition Again!!!!!!!!")
    else: 
        break
