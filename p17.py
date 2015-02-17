import math, sys

nums = ("zero one two three four five six seven eight nine ten "
        "eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen "
        "nineteen").split()
tens = ("twenty thirty forty fifty sixty seventy eighty ninety").split()

def letters(n):
    if n > 999: return "one thousand"
    elif n > 99:
        h = nums[n//100] + " hundred"
        if n % 100: return h + " and " + letters(n % 100)
        else: return h
    elif n > 19:
        if n % 10: return tens[n//10 - 2] + " " + nums[n%10] # hyphen to space
        else: return tens[n//10 - 2]
    else:
        return nums[n]

chars = 0
for i in range(1,1001):
    ch = len("".join(letters(i).split()))
    print("%d. %s (%d)" % (i, letters(i), ch))
    chars += ch
print(chars)
