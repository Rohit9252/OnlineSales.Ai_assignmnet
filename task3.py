# Task-3 Debugging:- Given below is a Bash / Python script that performs the following 
# computation on an integer input (n):

# ========================Solution========================


# Details:-The bugs in the script can be fixed as follows:
#  1. In the second part of the script, when calculating the factorial, 
# the range should start from 1, not from 0. This is because the factorial of 0 is 1.

#  2. In the third part of the script, the sum of integers between 1 and (n-20) 
# should be calculated using the formula for the sum of an arithmetic series, 
# which is (n * (n + 1)) / 2, not by squaring and subtracting lim.

def compute(n):
    if n < 10:
        out = n ** 2
    elif n < 20:
        out = 1
        for i in range(1, n - 9):  # Fixed the range starting from 1
            out *= i
    else:
        lim = n - 20
        out = (lim * (lim + 1)) // 2  # Fixed the calculation for sum of integers
    print(out)


n = int(input("Enter an integer: "))
compute(n)
