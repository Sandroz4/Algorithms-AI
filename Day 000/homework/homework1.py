# 1. Functionality for finding multiples of a number within a range

def hw1_try1(a, b, c):
    # Counts how many numbers between a and b are divisible by c
    return len([i for i in range(a, b) if i % c == 0])

def hw1_try2(a, b, c):
    # Calculates the number of divisible values, accounting for edge cases
    return (b - a) // c if a % c != 0 or (a % c == 0 and b % c == 0) else (b - a) // c + 1

def hw1_try2_easy_version(a, b, c):
    # Same logic as hw1_try2, written more explicitly for readability
    if a % c != 0 or (a % c == 0 and b % c == 0):
        return (b - a) // c
    else:
        return (b - a) // c + 1

# Testing 
print(hw1_try1(1, 20, 2))  # Example: counting multiples of 2 from 1 to 19
print(hw1_try2(1, 20, 2))
print(hw1_try2_easy_version(1, 20, 2))


