def fibonacci(n):
    a, b = 0, 1             # a = 0 (you can also type like this)
                            # b = 1
    if n <= 0:
        print("Please enter a positive integer")
        return []           # it prints [] this square bracket only
    elif n == 1:
        return [a]          # it prints [a] i.e [0]
    elif n == 2:
        return [a, b]       # it prints [a, b] i.e [0, 1] 

    fib_sequence = [a, b]   # is's a variable in python use to store sequences,lists

    for i in range(2, n):       # range function by default creates sequence of no. from 0 to (1 number less than n)
        c = a + b               # i.e range(6) so it generate values from 0 to 5
        fib_sequence.append(c)  # append, it add new element to existing list ex. my_list=[1,2,3], my_list.append=[4], my_list=[1,2,3,4]
        a, b = b, c

    return fib_sequence

n = int(input("Enter the number of terms in the Fibonacci sequence: "))     # Taking input from the user for the number of terms to generate

fib_series = fibonacci(n)

print("Fibonacci sequence:", fib_series)            # display the fiboncci series.