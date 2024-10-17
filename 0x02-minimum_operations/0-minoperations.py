"""
In a text file, there is a single character H.
Your text editor can execute only two operations
in this file: Copy All and Paste. Given a number n, 
write a method that calculates the fewest number of 
operations needed to result in exactly n H characters
in the file.
"""

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True  # 2 is the only even prime number
    if n % 2 == 0:
        return False  # Eliminate even numbers greater than 2
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def minOperations(n):
    """
    Method that calculates the fewest number of operations needed to result in exactly n H characters in the file.
    """
    if n <= 1:
        return 0
    
    operations = 0
    
    while is_prime(n):
        n = n - 1
        operations += 1
    
    for i in range(2, n + 1):
        if n % i == 0:
            return minOperations(n // i) + i
    return n + operations
