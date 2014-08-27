Primary Census Abstract
=======================

How to scrape data from the [Primary Census Abstract](http://www.censusindia.gov.in/pca/pca.aspx):

1.  Run `python pca_scraper.py`. You should get 01.csv through 35.csv, one
    file for each state. These are headerless CSVs. You can run this command
    multiple times to make forward progress. This is needed if the census site
    is slow or throws 500 errors.
2.  To get the header, run `python pca_scraper.py header`. This will produce
    a header.csv.
3.  To make a CSV containing data for the total district population
    (eliminating Rural and Urban rows)

        cat header.csv > pca-total.csv
        cat ??.csv | awk -F, '$2 != "000" && $5 == "Total"' >>pca-total.csv

4.  To make a CSV containing all rows (Total, Rural, Urban)
        cat header.csv > pca-full.csv
        cat ??.csv | awk -F, '$2 != "000"' >>pca-full.csv
