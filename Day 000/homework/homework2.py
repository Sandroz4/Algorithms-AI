def hw2_try1(num, b):
    num1 = str(num)  
    nums1 = []  
    nums2 = []  

    if "-" in num1:
        num = num1.split("-")
        part1 = num[0][::-1] 
        part2 = num[1]  

        for i in range(len(part1)):
            nums1.append(int(part1[i]) * (b ** i))

        for x in range(len(part2)):
            nums2.append(int(part2[x]) * (1 / b ** (x + 1)))

        return sum(nums1 + nums2)
    else:
        for i in range(len(num1)):
            nums1.append(int(num1[i]) * (b ** i))
        return sum(nums1)


print(hw2_try1(1001, 2))  
print(hw2_try1(520.3, 6)) 
