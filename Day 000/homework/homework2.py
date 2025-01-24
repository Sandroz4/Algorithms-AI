# 2. Functionality for converting numbers from one base to decimal

def hw2_try1(num, b):
    # Converts a number (possibly with a fractional part) in base `b` to decimal
    num1 = str(num)  # Convert the number to a string for easier processing
    nums1 = []  # Stores the integer part's contributions
    nums2 = []  # Stores the fractional part's contributions (if any)

    if "-" in num1:  # Check if the number has a fractional part
        # Split into integer (part1) and fractional (part2) parts
        num = num1.split("-")
        part1 = num[0][::-1]  # Reverse the integer part for positional calculations
        part2 = num[1]  # Keep the fractional part as is

        # Calculate the decimal value of the integer part
        for i in range(len(part1)):
            nums1.append(int(part1[i]) * (b ** i))

        # Calculate the decimal value of the fractional part
        for x in range(len(part2)):
            nums2.append(int(part2[x]) * (1 / b ** (x + 1)))

        # Return the total decimal value
        return sum(nums1 + nums2)
    else:
        # If no fractional part, calculate the decimal value directly
        for i in range(len(num1)):
            nums1.append(int(num1[i]) * (b ** i))
        return sum(nums1)

# Testing the base-to-decimal conversion function
print(hw2_try1(1001, 2))  # Convert binary 1001 to decimal
print(hw2_try1(101, 4))   # Convert base-4 101 to decimal
print(hw2_try1(520.1, 3)) # Convert base-3 number with fractional part
print(hw2_try1(1001, 16)) # Convert hexadecimal-like number 1001 to decimal
print(hw2_try1(520.3, 6)) # Convert base-6 number with fractional part
