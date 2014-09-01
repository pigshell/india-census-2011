
    cd xlsx
    for i in *; do ~/tmp/xlsx2csv/xlsx2csv.py "$i" |python ../norm.py | awk 'f;/^1,2,3,4,5,6/{f=1}' >../csv/"$i".csv; done


    cat header/header.csv >hlpca-total.csv
    for i in csv/*csv; do cat "$i" | awk -F, '$3 != "000" && $5 == "00000" && $10 == "Total"' >>hlpca-total.csv; done

    cat header/header.csv >hlpca-full.csv
    for i in csv/*csv; do cat "$i" | awk -F, '$3 != "000" && $5 == "00000"' >>hlpca-full.csv; done
