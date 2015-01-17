pos = ""
pre = ""
power = 0
power2 = 0
tot = 0

num = input("Please input a number to convert. (Can have decimals) ")
base = int(input("Now please input the base you want. (Max 10) "))
    
split = num.split(".")
integ = int(split[0])
if len(split) == 2:
    decim = int(split[-1])

while True:
    if (base ** power) > integ:
        break
    power += 1
power -= 1

while True:
    if len(split) == 1:
        break
    if (base ** power2) > decim:
        break
    power2 += 1
power2 -= 1

if not (num == integ):
    while power2 > -1:
        pre += str(decim//(base**power2))
        decim -= (decim//(base**power2)) * (base**power2)
        power2 -= 1

while power > -1:
    pos += str(integ//(base**power))
    integ -= (integ//(base**power)) * (base**power)
    power -= 1

tot = float(pos + "." + pre[::-1])

print("\n%s is %s when the base is of %s" % (num, tot, base))

