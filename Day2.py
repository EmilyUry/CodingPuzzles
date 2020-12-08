import re
file = open('input.txt')
input = file.readlines()


def eff(line):
    parts = re.split('-| |: ', line.strip())

    milo = int(parts[0])
    maxx = int(parts[1])
    key = parts[2]
    passcode = parts[3]

    moxie = passcode.count(key)

    if milo <= moxie <= maxx:
        return 'true'
    else:
        return 'false'


bob = 0
for each in input:
    # print(eff(each))
    if eff(each) == 'true':
        bob = bob + 1

print(bob)


# Part 2


