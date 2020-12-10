import util

jolts = set()
max_jolt = 0
with open(util.get_input_path(10), "r") as f:
    for line in f:
        jolt = int(line.strip())
        jolts.add(jolt)
        max_jolt = max(max_jolt, jolt)

#  ways to end the sequence at j - idx
#      -3  -2  -1
ways = [0, 0, 0]
ways[-1] = 1


for j in range(1, max_jolt+1):
    w = 0
    if j in jolts:
        for diff in range(1, 4, 1):  # possible gaps between jolts
            if j - diff < 0:
                break
            w += ways[-diff]
    ways[0] = ways[1]
    ways[1] = ways[2]
    ways[2] = w


print(ways[-1])  #  your device doesn't add more ways
