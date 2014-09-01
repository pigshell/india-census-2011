
import csv
import sys
import os

reader = csv.reader(sys.stdin, quoting=csv.QUOTE_MINIMAL)
writer = csv.writer(sys.stdout, quoting=csv.QUOTE_MINIMAL, delimiter=',', lineterminator=os.linesep)

lines = []
for i in range(3):
    row = reader.next()
    lines.append([r.strip().replace('\n', ' ') for r in row])

cur = ''
curprev = ''
line = lines[0]
for i in range(len(line)):
    if line[i] == '':
        line[i] = cur
    else:
        cur = line[i]

line = lines[1]
for i in range(len(line)):
    if line[i]:
        curprev = lines[0][i]
        line[i] = curprev + ': ' + line[i]
        cur = line[i]
    else:
        if curprev == lines[0][i]:
            line[i] = cur
        else:
            line[i] = lines[0][i]
            curprev = lines[0][i]

line = lines[2]
for i in range(len(line)):
    if line[i]:
        curprev = lines[1][i]
        line[i] = curprev + ' (' + line[i] + ')'
        cur = line[i]
    else:
        if curprev == lines[1][i]:
            line[i] = cur
        else:
            line[i] = lines[1][i]
            curprev = lines[1][i]
    print "c%d,%s" % (i + 1, line[i])
