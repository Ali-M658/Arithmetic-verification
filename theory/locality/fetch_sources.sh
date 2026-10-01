#!/bin/bash
# Re-create theory/locality/sources_cache/ (not committed): headless retrieval of the
# sources quoted in proof.md.  Text is extracted with pymupdf for quotation.
set -u
cd "$(dirname "$0")"
mkdir -p sources_cache
cd sources_cache
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15"
get() {  # file url
  curl -sL -A "$UA" --max-time 180 -o "$1" -w "$1 %{http_code} %{size_download}\n" "$2"
}
# library.msri.org no longer resolves (HTTP 000); the SLMath mirror serves the same file
get thurston_ch13.pdf  https://library.slmath.org/books/gt3m/PDF/13.pdf
get dggw_0805.3148.pdf https://arxiv.org/pdf/0805.3148
get ds_math0504571.pdf https://arxiv.org/pdf/math/0504571
get lv_1408.2001.pdf   https://arxiv.org/pdf/1408.2001
get dr_1103.4372.pdf   https://arxiv.org/pdf/1103.4372
get ucar_1711.03405.pdf https://arxiv.org/pdf/1711.03405
get su_1110.2150.pdf   https://arxiv.org/pdf/1110.2150
get marklof_math0407288.pdf https://arxiv.org/pdf/math/0407288v2
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
