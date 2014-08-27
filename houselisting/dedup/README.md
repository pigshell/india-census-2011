Processing Houselisting Primary Census Abstract
===============================================

After following the steps indicated in the parent directory:

To remove duplicate columns,

    for i in ../*csv; do cat $i | python filter_dup.py $i > `basename $i`; done

Now we need to remove the state level information (district code 000), extract
only the "Total" rows (those who want Urban and Rural can follow the same steps,
replacing Total with Urban/Rural. There are two gotchas:

1.  A few districts are duplicated. We eliminate them with `uniq`
2.  There is a botched table - Lakshadweep has only state-level rows. District
    code 587 is missing. Since Lakshadweep has only one district, manually edit
    `31.csv` to duplicate the existing 3 rows and change district code to 587
    in the added rows.

That done, we're ready to put together the final CSV

    cat header.csv >hlpca-total.csv
    awk -F, '$3 != "000" && $10 == "Total"' ??.csv |  uniq >>hlpca-total.csv
    wc hlpca-total.csv

Finally, we have a CSV with 641 rows (640 districts + 1 header row)
