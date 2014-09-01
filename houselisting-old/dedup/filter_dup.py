import sys
import os

def findcol(colnames, name):
    found = []
    for i in range(len(colnames)):
        if colnames[i] == name:
            found.append(i)
    return found

if __name__ == '__main__':
    with open("../header.csv", "r") as h:
        line = h.readline()
        colnames = [c.strip() for c in line.split(',')]
        print >> sys.stderr, "columns ", len(colnames)

    rows = []
    lines = sys.stdin.readlines()
    for l in lines:
        cols = l.split(',')
        cols = [c.strip() for c in cols]
        if len(cols) != len(colnames):
            print >> sys.stderr, "invalid line ", len(cols), l
        rows.append(cols)

    skip = []
    for i in range(len(colnames)):
        found = findcol(colnames, colnames[i])
        if len(found) > 2:
            print >> sys.stderr, "found %d occurences of %s" % (len(found), colnames[i])
        elif len(found) == 2 and found[0] < found[1]:
            skip.append(found[1])
    for r in rows:
        frow = []
        for i in range(len(colnames)):
            if i not in skip:
                frow.append(r[i])
        print ",".join(frow)
