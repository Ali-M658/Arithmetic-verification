#!/bin/bash
# usage: ftsearch.sh "query" outfile  -- arXiv full-text search (search_classic, searchtype=ft), hits 1-20, parsed
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
D=$(cd "$(dirname "$0")" && pwd)
q="$1"; out="$2"
enc=$(python3 -c 'import urllib.parse,sys;print(urllib.parse.quote_plus(sys.argv[1]))' "$q")
html=$(curl -s -L -A "$UA" -X POST --data "searchtype=ft&query=$enc" https://arxiv.org/search_classic)
qid=$(echo "$html" | grep -o 'qid=[^&"]*' | head -1 | cut -d= -f2)
html2=$(curl -s -L -A "$UA" "https://search.arxiv.org/?query=$enc&qid=$qid&startat=10")
{ echo "## QUERY (arXiv full text): $q"; echo "$html" | grep -o 'Displaying hits[^<]*'
  echo "$html" | python3 "$D/parse.py"; echo "$html2" | python3 "$D/parse.py"; echo; } >> "$out"
