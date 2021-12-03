data = open("input.txt", "r")

forward = 0
aim = 0
depth = 0

for line in data:
    line_data = line.split(" ")
    if line_data[0] == "forward":
        forward += int(line_data[1])
        if aim > 0:
            depth += aim*int(line_data[1])
        print ("forward ...")
    if line_data[0] == "down":
        aim += int(line_data[1])
        print ("down ...")
    if line_data[0] == "up":
        aim -= int(line_data[1])
        print ("up ...")

print(forward*depth)
