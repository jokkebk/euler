sum = 0
last = 1
num = 2
while num <= 4e6:
    print(num)
    if (num-1) & 1: sum += num
    (num, last) = (num+last, num)

print(sum)
