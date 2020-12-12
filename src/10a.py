import util


maximum = 0
length = 0
with open(util.get_input_path(10), "r") as f:
    for line in f:
        jolt = int(line.strip())
        maximum = max(maximum, jolt)
        length += 1

# for the device itself
length += 1
maximum += 3

#  num_of_three_jolts * 3 + num_of_one_jolts = maximum
#  num_of_three_jolts + num_of_of_one_jolts = length
three_jolts = (maximum - length) / 2
print(three_jolts * (length - three_jolts))
