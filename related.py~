import sys

fname = sys.argv[1]

with open(fname, "r") as ins:
    array = []
    for line in ins:
        array.append(line)

matching = [s for s in array if "REMARK" and "RELATED" in s]

for i in matching:
    i = i[11:27]
    print i 
