pandigi = lambda s: "".join(sorted(s)) == "123456789"

(bn, bn1, tn, tn1, n) = (1, 1, 1, 1, 2) # bottom and top parts

while True:
    (bn, bn1, tn, tn1, n) = ((bn+bn1)%1000000000, bn, tn+tn1, tn, n+1)
    if pandigi(str(bn)) and pandigi(str(tn)[:9]):
        print(n)
        break
