#fh = open('mbox-short.txt')
#
#for lx in fh:
#    ly = lx.rstrip()
#    print(ly.upper())

han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    wds = line.split()
    # guardian in a compound statement
    if len(wds) < 3 or wds[0] != 'From' :
        continue
    print(wds[2])