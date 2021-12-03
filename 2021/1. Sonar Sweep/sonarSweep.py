input_file = open("input.txt", "r")

depth_increased = 0
arr = []
measurement_arr = []

for line in input_file:
    arr.append(int(line))

for i in range(len(arr) - 2):
    measurement_arr.append(arr[i] + arr[i + 1] + arr[i + 2])
    if len(measurement_arr) >= 2:
        if measurement_arr[i] > measurement_arr[i - 1]:
            depth_increased += 1

print depth_increased
