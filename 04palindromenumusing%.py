def palindrome(n):
    num = n             # num to store original number.             now let num = 12321
    rev_num = 0         # & rev_num to store reverse number.
    
    for _ in range(len(str(n))):
        last_digit = n % 10         # 12321 % 10 = 1    i.e last_digit = 1
        rev_num = (rev_num * 10) + last_digit   # rev_num = (0 * 10) + 1    so now rev_num = 1
        n //= 10 # it makes the number n = 12321 to 1232.1 then removes the point and assigns the remaining value to n   i.e now n = 1232

                        # The loop runs the number of times equal to the length of the input number
    return num == rev_num

number = int(input("Enter a number to check if it's a palindrome: "))
if palindrome(number):
    print(f"{number} is a palindrome!") # print(f"{number}...") its a f-string it's directly put the value for what inside of {}
else:
    print(f"{number} is not a palindrome.")  # we can also use, print(number ,"is not a palindrome.")
