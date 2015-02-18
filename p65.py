def calc(s):
    (denum, num) = (1, 0)
    for el in s[-1:0:-1]:
        (num, denum) = (denum, num)
        denum += el * num
    num += s[0] * denum
    return (num, denum)

e = [2]

for i in range(2,102,2): e.extend([1,i,1])

print(sum(int(c) for c in str(calc(e[:100])[0])))
