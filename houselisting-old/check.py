import sys
import os

def findcol(colnames, name):
    found = []
    for i in range(len(colnames)):
        if colnames[i] == name:
            found.append(i)
    return found

if __name__ == '__main__':
    with open("header.csv", "r") as h:
        line = h.readline()
        colnames = [c.strip() for c in line.split(',')]
        print "columns ", len(colnames)

    for i in range(35):
        state_id = '%02d' % (i + 1)
        fname = state_id + '.csv'
        try:
            if os.path.getsize(fname) == 0:
                print "skipping %s" % fname
                continue
        except:
            pass
        rows = []
        with open(fname, "r") as f:
            lines = f.readlines()
            for l in lines:
                cols = l.split(',')
                cols = [c.strip() for c in cols]
                if len(cols) != len(colnames):
                    print "invalid line ", len(cols), l
                rows.append(cols)

        print "fname %s rows %d" % (fname, len(rows))
        for i in range(len(colnames)):
            found = findcol(colnames, colnames[i])
            if len(found) > 2:
                print "found %d occurences of %s" % (len(found), colnames[i])
            elif len(found) == 2:
                for j in range(len(rows)):
                    try:
                        if rows[j][found[0]] != rows[j][found[1]]:
                            print "Mismatch for column %s, row %d" % (colnames[i], j)
                    except:
                        print "EXCEPTION", j, found, rows[j]
