#!/bin/bash
# Headless retrieval for the literature review (P6, P7). Texts via pdftotext -layout.
cd "$(dirname "$0")/sources"
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15"
get() { curl -sL -A "$UA" --max-time 240 -o "$1" -w "$1 %{http_code} %{size_download} %{content_type}\n" "$2"; case "$1" in *.pdf) pdftotext -layout "$1" "${1%.pdf}.txt" 2>/dev/null;; esac; }
for spec in "$@"; do get ${spec%%=*} "${spec#*=}"; done
