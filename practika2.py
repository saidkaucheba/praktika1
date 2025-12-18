"""ЗАДАНИЕ 1"""

"""
with open('39762.txt', 'r') as f:
    n = f.readlines()
    n = [int(e1) for e1 in n]
co = 0
max_sum = 0
for i in range(len(n) - 1):
    a = n[i]
    b = n[i + 1]
    if (a * b) % 15 == 0 and (a + b) % 7 == 0:
        co += 1
        if (a + b) > max_sum:
            max_sum = a + b
print(co)
print(max_sum)
"""


"""ЗАДАНИЕ 2"""

"""
with open("68279.txt", "r") as f:
    n = [int(el) for el in f]
    max_el = 0

    for el in n:
        if str(el)[-3:] == "562":
            if max_el < el:
                max_el = el

    c = 0
    s = []
    max_sum = 0
    for i in range(len(n) - 3):
        l = [n[i], n[i + 1], n[i + 2], n[i + 3]]
        l5 = [el for el in l if len(str(el)) == 5]
        lnot5 = [el for el in l if len(str(el)) != 5]
        lcrat3 = [el for el in l if el % 3 == 0]
        lcrat7 = [el for el in l if el % 7 == 0]
        if len(l5) >= 1 and len(lnot5) >= 2:
            if len(lcrat3) < len(lcrat7):
                if sum(l) > max_el and sum(l) < max_el*2:
                    c += 1
                    if max_sum < sum(l):
                        max_sum = sum(l)
    print(c, max_sum)
"""


"""ЗАДАНИЕ 3"""

"""
with open('40992.txt', 'r') as f:
    n = f.readlines()
    n = [int(e1) for e1 in n]
co = 0
max_sum = 0
sred_arif = 0
kol = 0
for i in n:
    if i % 2 != 0:
        sred_arif += i
        kol += 1
sred_arifmen = sred_arif // kol
for i in range(len(n) - 1):
    a = n[i]
    b = n[i + 1]
    if ((a % 5 == 0) or (b % 5 == 0)) and ((a < sred_arifmen) or (b < sred_arifmen)):
        co += 1
        if (a + b) > max_sum:
            max_sum = a + b
print(co)
print(max_sum)
"""