fp = open('filename.pdb')
while 1:
    line = fp.readline()
    if not line:
        break
    print line
