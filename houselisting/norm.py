import csv
import sys
import os

reader = csv.reader(sys.stdin, quoting=csv.QUOTE_MINIMAL)
writer = csv.writer(sys.stdout, quoting=csv.QUOTE_MINIMAL, delimiter=',', lineterminator=os.linesep)

def convert(x):
    if x.find('.') == -1:
        return x
    try:
        f = float(x)
        return '%g' % (round(f, 4),)
    except:
        return x

for row in reader:
    out = [r.strip().replace('\n', ' ') for r in row]
    out = [convert(r) for r in out]
    out = out[0:145]
    writer.writerow(out)
