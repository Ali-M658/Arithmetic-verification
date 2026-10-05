#!/bin/bash
# Re-create theory/revision/sources_cache/ (not committed): headless retrieval of the sources
# quoted in the fragments of theory/revision/.  Text is extracted with pymupdf for quotation.
set -u
cd "$(dirname "$0")"
mkdir -p sources_cache
cd sources_cache
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15"
get() {  # file url
  curl -sL -A "$UA" --max-time 180 -o "$1" -w "$1 %{http_code} %{size_download}\n" "$2"
}
get ds_math0504571.pdf https://arxiv.org/pdf/math/0504571          # Dryden-Strohmaier, eq. (1)
get cremona_ch3.pdf    https://johncremona.github.io/book/fulltext/chapter3.pdf   # Cremona 2nd ed., ch. III
PY=${PY:-/opt/homebrew/Caskroom/miniforge/base/bin/python3}
"$PY" - <<'PYEOF'
import glob, pymupdf
for f in sorted(glob.glob("*.pdf")):
    try:
        d = pymupdf.open(f)
    except Exception as e:
        print("NOT A PDF:", f, e); continue
    open(f[:-4] + ".txt", "w").write("\n\f".join(p.get_text() for p in d))
    print(f, d.page_count, "pages")
PYEOF
shasum -a 256 *.pdf
