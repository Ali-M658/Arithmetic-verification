#!/bin/bash
# Build the pinned environment on the compute server (Ubuntu 24.04, x86_64).
#   bash numerics/moduli/env/setup_server.sh  [prefix, default /opt/miniforge]
# Installs Miniforge 26.7.2-0 (sha256-checked), creates env "moduli" from
# environment.yml, and records conda list / pip freeze next to this script.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
PREFIX="${1:-/opt/miniforge}"
MF=Miniforge3-26.7.2-0-Linux-x86_64.sh
URL=https://github.com/conda-forge/miniforge/releases/download/26.7.2-0
if [ ! -x "$PREFIX/bin/conda" ]; then
  cd /tmp
  curl -sSL -o "$MF" "$URL/$MF"
  curl -sSL -o "$MF.sha256" "$URL/$MF.sha256"
  sha256sum -c "$MF.sha256"
  bash "$MF" -b -p "$PREFIX"
fi
cd "$HERE"
"$PREFIX/bin/conda" env create -y -f environment.yml
ENV="$PREFIX/envs/moduli"
"$PREFIX/bin/conda" list -n moduli --explicit > conda-explicit.server.txt
"$ENV/bin/python" -m pip freeze > pip-freeze.server.txt
"$ENV/bin/python" -c "import ngsolve, numpy, scipy, mpmath; print('ngsolve', ngsolve.__version__, 'numpy', numpy.__version__, 'scipy', scipy.__version__)"
