# import fileinput
import fileinput

# Using fileinput.input() method
arr = []

for line in fileinput.input(files='input.txt'):
    arr.append(int(line))

for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr) - 1):
        if arr[i] + arr[j] == 2020:
            print(arr[i] * arr[j])
        for z in range(j + 1, len(arr) - 1):
            if arr[i] + arr[j] + arr[z] == 2020:
                print(arr[i] * arr[j] * arr[z])