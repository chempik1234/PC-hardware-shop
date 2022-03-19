s = ' '
a = []
while s:
    s = input()
    if s:
        a.append(s)
for i in a:
    print("'Гарантия': " + i.split()[0] + ',')