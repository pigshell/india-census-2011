Houselisting Primary Census Abstract
====================================

A painful process. 290 columns, about half of which are duplicate.

How to scrape [Houselisting primary census abstract](http://www.censusindia.gov.in/hlpca/default.aspx):

1.  Run `python hlpca_scraper.py`. You should get 01.csv through 35.csv, one
    file for each state. These are headerless CSVs. You can run this command
    multiple times to make forward progress. This is needed if the Census site
    is slow or throws 500 errors.
2.  To get the header, run `python hlpca_scraper.py header`. This will produce
    a header.csv.
3.  This header.csv is then modified so that all duplicate fields actually
    have duplicate header names (e.g. Rural/Urban and Rural_Urban are
    both changed to Rural/Urban)
4.  Run `python check.py` to ensure that the duplicate columns are indeed
    duplicate.
5.  `cd dedup` and follow the instructions there.
