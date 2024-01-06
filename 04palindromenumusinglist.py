def palindrome(n):
    digits = list(str(n))              # Convert the number to a list of digits  

    reversed_digits = digits[::-1]     # Reverse the list of digits
    
    return digits == reversed_digits   # Check if the original and reversed lists are the same

n = int(input("Enter a number: "))     # Take input from the user

if palindrome(n):                      # Check if the number is a palindrome
    print(f"{n} is a palindrome!")
else:
    print(f"{n} is not a palindrome.")
