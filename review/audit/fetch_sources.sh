#!/bin/bash
# G5 audit: headless retrieval of the external inputs given to the reviewers.
# PDFs and text extracts land in review/audit/sources/ (not committed; see .gitignore).
# Every unreachable source is recorded in review/audit/fetches.md.
set -u
cd "$(dirname "$0")"
mkdir -p sources
cd sources
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15"
get() {  # file url
  curl -sL -A "$UA" --max-time 240 -o "$1" -w "$1 %{http_code} %{size_download}\n" "$2"
}
get dggw_0805.3148.pdf        https://arxiv.org/pdf/0805.3148
get ucar_1711.03405.pdf       https://arxiv.org/pdf/1711.03405
get ds_math0504571.pdf        https://arxiv.org/pdf/math/0504571v2
get thurston_ch13.pdf         https://library.slmath.org/books/gt3m/PDF/13.pdf
get marklof_math0407288.pdf   https://arxiv.org/pdf/math/0407288v2
get mueller_1311.5493.pdf     https://arxiv.org/pdf/1311.5493
get kokotov_0906.0717.pdf     https://arxiv.org/pdf/0906.0717
get schueth_1812.06119.pdf    https://arxiv.org/pdf/1812.06119
get lv_1408.2001.pdf          https://arxiv.org/pdf/1408.2001
get dr_1103.4372.pdf          https://arxiv.org/pdf/1103.4372
get holtz_tyaglov_0912.4703.pdf https://arxiv.org/pdf/0912.4703
get ostrowski_1940.pdf        "https://projecteuclid.org/journals/acta-mathematica/volume-72/issue-none/Recherches-sur-la-m%c3%a9thode-de-graeffe-et-les-z%c3%a9ros-des/10.1007/BF02546330.pdf"
get bgn_mcom1993.pdf          https://www.ams.org/journals/mcom/1993-61-203/S0025-5718-1993-1189516-5/S0025-5718-1993-1189516-5.pdf
get schinzel_serdica1996.pdf  http://www.math.bas.bg/serdica/1996/1996-587-588.pdf
get pari_elliptic.html        https://pari.math.u-bordeaux.fr/dochtml/html/Elliptic_curves.html
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
