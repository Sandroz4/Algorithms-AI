def hw1_try1(a, b, c):
    return len([i for i in range(a, b) if i % c == 0])

def hw1_try2(a, b, c):
    return (b - a) // c if a % c != 0 or (a % c == 0 and b % c == 0) else (b - a) // c + 1

def hw1_try2_easy_version(a, b, c):
    if a % c != 0 or (a % c == 0 and b % c == 0):
        return (b - a) // c
    else:
        return (b - a) // c + 1


print(hw1_try1(1, 20, 2))  
print(hw1_try2(1, 20, 2))
print(hw1_try2_easy_version(1, 20, 2))


