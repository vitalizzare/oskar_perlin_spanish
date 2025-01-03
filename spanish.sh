while read -p '> ' a
do
    grep "$a" *.tsv
done
echo
