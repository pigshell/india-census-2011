import mechanize
import lxml.html
import sys
import os

url = "http://www.censusindia.gov.in/hlpca/default.aspx"

def get_state(state_id, tdxpath):
    br = mechanize.Browser()
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    response = br.open(url)
    rdata = response.read()
    br.select_form("form1")
    br.set_all_readonly(False)
    br["drpState"] = [state_id]
    response = br.submit()
    rdata = response.read()
    br.select_form("form1")
    br.set_all_readonly(False)
    br["drpDistrict"]=['1']
    response = br.submit()
    rdata = response.read()
    root = lxml.html.fromstring(rdata)
    table = root.xpath('//table[@id="GridData"]')
    lines = []
    for row in table[0].xpath('.//tr'):
        cells = row.xpath(tdxpath)
        if len(cells):
            column = []
            for cell in cells:
                content = cell.text_content().encode("utf8").strip()
                column.append(content)
            lines.append(",".join(column))
    return lines

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'header':
        states = range(1)
        tdxpath = './/th'
    else:
        states = range(35)
        tdxpath = './/td'
        

    for i in states:
        state_id = '%02d' % (i + 1)
        fname = state_id + '.csv' if tdxpath == './/td' else 'header.csv'
        try:
            if os.path.getsize(fname) > 0:
                print >>sys.stderr, "found %s, skipping" % fname
                continue
        except:
            pass
        with open(fname, "w") as f:
            lines = get_state(state_id, tdxpath)
            if len(lines):
                f.write('\n'.join(lines) + '\n')
                print >>sys.stderr, "wrote %d lines in %s" % (len(lines), fname)
