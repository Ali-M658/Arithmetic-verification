#!/bin/bash
# G5-bis: headless retrieval of the external inputs given to the reviewers.
# PDFs and text extracts land in review/audit-2/sources/ (not committed). Every unreachable
# source is recorded in fetches.md by hand afterwards. No browser.
set -u
cd "$(dirname "$0")"
mkdir -p sources
cd sources
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15"
get() {  # file url
  curl -sL -A "$UA" --max-time 240 -o "$1" -w "$1 %{http_code} %{size_download}\n" "$2"
}
get dggw_0805.3148.pdf         https://arxiv.org/pdf/0805.3148
get ucar_1711.03405.pdf        https://arxiv.org/pdf/1711.03405
get ds_math0504571.pdf         https://arxiv.org/pdf/math/0504571v2
get schueth_1812.06119.pdf     https://arxiv.org/pdf/1812.06119
get cremona_ch3.pdf            https://johncremona.github.io/book/fulltext/chapter3.pdf
get chen_survey_2506.11429.pdf https://arxiv.org/pdf/2506.11429
get cmsv_2304.11254.pdf        https://arxiv.org/pdf/2304.11254
get croot_mao_yip_2609.05061.pdf https://arxiv.org/pdf/2609.05061
get wooley_1101.0574.pdf       https://arxiv.org/pdf/1101.0574
get wooley_1708.01220.pdf      https://arxiv.org/pdf/1708.01220
get choudhry_2207.12726.pdf    https://arxiv.org/pdf/2207.12726
get caley_1011.1262.pdf        https://arxiv.org/pdf/1011.1262
get eslpower_TarryPrb.htm      http://eslpower.org/TarryPrb.htm
get eslpower_kminus.htm        http://eslpower.org/kminus.htm
get eslpower_eslp.htm          http://eslpower.org/eslp.htm
get melzak_cmb1961.pdf         https://cms.math.ca/publications/cmb/1961/4/233.pdf
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
shasum -a 256 *.pdf *.htm > SHA256SUMS
