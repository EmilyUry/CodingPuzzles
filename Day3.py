file = open('input2.txt')
input = file.readlines()
print(input[0])

aline = input[0].strip()
fullline = aline * 323 * 3
print(len(fullline))
position = fullline[0]
print(position)
if position == 'X':
    print('true')
else:
    print('false')



def makemap(line):
    aline = line.strip()
    fullline = aline * 323 * 3
    return fullline


for each in input:
    makemap(each)

# print(line1x)
print(len(fulline[0]))
