#!/usr/bin/env python3

def print_fibonacci(n):
    if n == 0:
        print([])
        return
    elif n == 1:
        print([0])
        return
    
    # Initialize the first two numbers of the Fibonacci sequence
    fibonacci_sequence = [0, 1]
    
    # Generate the Fibonacci sequence up to length n
    while len(fibonacci_sequence) < n:
        next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_value)
    
    print(fibonacci_sequence)
