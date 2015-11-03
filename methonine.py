import sys

fname = sys.argv[1]

with open(fname, "r") as ins:
    array = []
    for line in ins:
        array.append(line)

#condition_y = ["ATOM", "MET"]
#condition_n = ["REMARK"]

matching = [s for s in array if "ATOM" and "MET" in s]

#matching = [s for s in array if all(condition_y) and not all(condition_n) in s]

for i in matching:
    #i = i[11:27]
    print i 
