YEARVAR=$(date "+%Y")
DAYVAR=$(date "+%d")
# Insert your paths
PYPATH=
AOCURLPATH=
REPOPATH=
 
$PYPATH $AOCURLPATH $YEARVAR $DAYVAR;
 
mkdir $REPOPATH/day$DAYVAR && cp $REPOPATH/template/* $REPOPATH/day$DAYVAR;
echo -e ".SILENT:\nall:\n\t$PYPATH $AOCURLPATH $YEARVAR $DAYVAR -io | $PYPATH main.py" > $REPOPATH/day$DAYVAR/Makefile
