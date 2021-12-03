data = open("input.txt", "r")

oxygen_generator_rating = []
CO2_scrubber_rating = []

for line in data:
    oxygen_generator_rating.append(line)
    CO2_scrubber_rating.append(line)

lineLength = len(oxygen_generator_rating[0]) - 1

for char in range(lineLength):
    if len(oxygen_generator_rating) > 1:
        ones = []
        zeros = []
        for line in range(len(oxygen_generator_rating)):
            if oxygen_generator_rating[line][char] == '1':
                ones.append(oxygen_generator_rating[line])
            else:
                zeros.append(oxygen_generator_rating[line])
        if len(ones) < len(zeros):
            oxygen_generator_rating = zeros
        else:
            oxygen_generator_rating = ones

    if len(CO2_scrubber_rating) > 1:
        ones = []
        zeros = []

        for line in range(len(CO2_scrubber_rating)):
            if CO2_scrubber_rating[line][char] == '1':
                ones.append(CO2_scrubber_rating[line])
            else:
                zeros.append(CO2_scrubber_rating[line])
        if len(ones) < len(zeros) or len(zeros) == 0:
            CO2_scrubber_rating = ones
        else:
            CO2_scrubber_rating = zeros

print int(oxygen_generator_rating[0], 2)*int(CO2_scrubber_rating[0], 2)
