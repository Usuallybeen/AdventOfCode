data = open("input.txt", "r")

dataArr = []

gamma_rate = ""
epsilon_rate = ""

for line in data:
    dataArr.append(line)

for char in range(len(dataArr[0]) - 1):
    ones = 0
    zeros = 0
    for line in range(len(dataArr)):
        if dataArr[line][char] == '1':
            ones += 1
        else:
            zeros += 1
    if ones > zeros:
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'

print int(gamma_rate, 2)*int(epsilon_rate, 2)
