#NUM 1

GREEN = '\u001b[42m'
RED = '\u001b[41m'
YELLOW = '\u001b[43m'
END = '\u001b[0m'

for i in range(8):
    if i < 4:
        print(f'{GREEN}{"  " *6}{YELLOW}{"  " *8}{END}')
    else:
        print(f'{GREEN}{"  " *6}{RED}{"  " *8}{END}')

#NUM 2

RED = '\u001b[41m'
WHITE = '\u001b[47m'
END = '\u001b[0m'
for i in range(9):
    if i == 0 or i == 8:
        print(f'{WHITE}{"  "*(11)}{END}')
    elif i == 1 or i == 7:
        print(f'{WHITE}{"  "*(3)}{RED}{"  "}{WHITE}{"  "*(3)}{RED}{"  "}{WHITE}{"  "*(3)}{END}')
    elif i == 2 or i == 6:
        print(f'{WHITE}{"  "*(2)}{RED}{"  "*(3)}{WHITE}{"  "}{RED}{"  "*(3)}{WHITE}{"  "*(2)}{END}')
    elif i == 3 or i == 5:
        print(f'{WHITE}{"  "}{RED}{"  "*(9)}{WHITE}{"  "}{END}')
    elif i == 4:
        print(f'{RED}{"  "*11}{END}')

#NUM 3
RED = '\u001b[41m'
WHITE = '\u001b[47m'
END = '\u001b[0m'
for i in range(8):
    if i<7:
        print(8-(i),f'{WHITE}{"  " * (8-(i+2))}{RED}{"  " * (1)}{WHITE}{"  " * (i)}{END}')
    if i == 7:
        print(1, ' 1 2 3 4 5 6 7 ')

#NUM 4

f = open('sequence.txt')
ls = []
lsnew = []
lsneww = []
for num in f:
    ls.append(float(num))
for i in ls:
    if i > -5 and  i < 0:
        lsnew.append(i)
    elif i > 0 and i < 5:
        lsneww.append(i)
f.close()
print(len(lsneww)/len(lsnew))
