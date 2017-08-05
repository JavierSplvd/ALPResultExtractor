file = open("targetfile.csv", "r")
results = open("results.txt", "w")

file.seek(0, 0)
lines = file.readlines()

canWrite = False
numberOfTable = 0

for line in lines:
    if (line.strip("\n") == "END_TABLE") & (canWrite):
        break
    if canWrite:
        results.write(line)
    if line.strip("\n") == "START_TABLE":
        numberOfTable += 1
        if numberOfTable == 2:
            canWrite = True

file.close()