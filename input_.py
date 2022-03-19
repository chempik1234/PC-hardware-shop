s = ' '
a = []
while s:
    s = input()
    if s:
        a.append(s)
for i in a:
    print('parser.add_argument("' + i.split()[0] + '", required=True')