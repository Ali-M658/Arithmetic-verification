#!/usr/bin/env python3
"""Build DATA-MANIFEST.md: every committed data file with its size, SHA-256, the script and
command that generates it, and the paper element (table, figure F1-F9, theorem) that will use it.

    python3 admin/build_data_manifest.py            write DATA-MANIFEST.md
    python3 admin/build_data_manifest.py --check    assert that DATA-MANIFEST.md is current

The rule table below is the single source of truth for the "generator" and "paper element"
columns; sizes and hashes are read from the files. Both modes assert that

  * every tracked data file (csv, json, npz, txt, *_output.md, generated .tex tables, the
    solver logs) matches exactly one rule, so a new data file cannot be committed
    without being described here;
  * every rule matches at least one file, so a stale rule cannot linger.

--check additionally compares the rendered manifest with the committed one, byte for byte,
so a changed file (new hash) or an added file fails until the manifest is rebuilt.
"""
import fnmatch
import hashlib
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "DATA-MANIFEST.md"

# ------------------------------------------------------------------------------ rules
# (glob, generator script(s), command, paper element)
RULES = [
    # --- the original arithmetic harness
    ("data/degeneracies.csv", "code/enumerate_degeneracies.py", "cd code && python3 enumerate_degeneracies.py",
     "Table tab:enum (Section 5.2); Theorem 5.2 (two-coefficient degeneracies); the N(S)/S^2 values of tab:density"),
    ("data/degeneracy-groups.csv", "code/enumerate_degeneracies.py", "cd code && python3 enumerate_degeneracies.py",
     "Section 5.2 degeneracy classes; the pair/class convention of MAJ-01; reproduced row by row by theory/diophantine/enumerate_fast.py"),
    ("paper/tables/*.tex", "code/make_table.py", "cd code && python3 make_table.py",
     "Tables tab:enum and tab:density as typeset in main.tex"),
    ("code/legacy/*.txt", "code/legacy/ (the co-author's original verification scripts)", "see code/legacy/PROVENANCE.md",
     "Provenance only: the original outputs, superseded by code/run_all.sh"),
    ("review/coverage-map.csv", "code/coverage_report.py", "cd code && python3 coverage_report.py",
     "Appendix A: claim-ledger coverage of the verification harness"),
    # --- independent proof audit
    ("review/audit/**", "independent proof audit (S9a); produced by the scripts in the same review/audit/<group>/ folder",
     "see the group's README or check_*.py in that folder", "none (G5 audit evidence)"),
    # --- audibility
    ("theory/audibility/output/orlando_check.txt", "theory/audibility/orlando_check.py",
     "cd theory/audibility && python3 orlando_check.py > output/orlando_check.txt", "Theorem A (Orlando's identity, Lemma on Hurwitz determinants)"),
    ("theory/audibility/output/linear_system.txt", "theory/audibility/linear_system.py",
     "cd theory/audibility && python3 linear_system.py > output/linear_system.txt", "Theorem B (linear system, det M = c_n Delta_{n-1}/e_n)"),
    ("theory/audibility/output/verify_elimination.txt", "theory/audibility/verify_elimination.py",
     "cd theory/audibility && python3 verify_elimination.py > output/verify_elimination.txt", "Theorem A, n = 3..8 elimination (H1-H4)"),
    ("theory/audibility/output/sharpness_search_N*.txt", "theory/audibility/sharpness_search.py",
     "cd theory/audibility && python3 sharpness_search.py N > output/sharpness_search_NN.txt   (N = 60, 120)",
     "Theorem C (sharpness) and Remark on n = 5: no integer witness with all orders <= 120"),
    ("theory/audibility/sharpness_n5_N*.json", "theory/audibility/sharpness_search.py",
     "cd theory/audibility && python3 sharpness_search.py N   (N = 60, 120)", "Theorem C, n = 5 search record"),
    # --- other theory outputs
    ("theory/cone-coefficients/verify_output.txt", "theory/cone-coefficients/verify_cone_coefficients.py",
     "cd theory/cone-coefficients && python3 verify_cone_coefficients.py > verify_output.txt", "Eq. (4) and the cone polynomials p_l (Section 2.3); MIN-08"),
    ("theory/signatures/output/*.txt", "theory/signatures/{heat_structure,cone_count,genus,area_classes}.py",
     "cd theory/signatures && python3 NAME.py > output/NAME.txt", "Theorems N and S (general signatures); area_classes.txt: Figure F4 (data exists as a text transcript only)"),
    ("theory/locality/output/check_locality.txt", "theory/locality/check_locality.py",
     "cd theory/locality && python3 check_locality.py > output/check_locality.txt", "Theorem (locality) and the moduli corollary (K_iso = infinity, n >= 4)"),
    ("theory/stability/*_output.md", "theory/stability/{front_end,lipschitz_e,roots_holder,threshold}.py",
     "cd theory/stability && python3 NAME.py   (writes NAME_output.md)", "Stability theorem (Lipschitz front end, Holder roots, integer threshold)"),
    ("theory/stability/threshold_results.json", "theory/stability/threshold.py", "cd theory/stability && python3 threshold.py",
     "Stability theorem, certified thresholds delta_cert vs constructed failures delta_up; Figure F8 (thresholds only: the recovery-error sweep does not exist yet)"),
    ("theory/stability/blind/result.json", "theory/stability/blind/blind_pipeline.py", "cd theory/stability/blind && python3 blind_pipeline.py",
     "Blind recovery of the cone orders of (2,8,8) and (3,3,12) from the computed spectra; Figure F8 (the two recovery points)"),
    ("theory/stability/blind/RESULT.md", "theory/stability/blind/blind_pipeline.py", "cd theory/stability/blind && python3 blind_pipeline.py",
     "Blind recovery narrative (Section on stability, numerical illustration)"),
    ("theory/stability/attack/*_output.txt", "theory/stability/attack/*.py", "cd theory/stability/attack && python3 NAME.py > NAME_output.txt",
     "Adversarial review of the stability proofs (appendix material; not cited in the paper)"),
    ("theory/threshold/first_overlap_vs_collision.csv", "theory/threshold/threshold.py", "cd theory/threshold && python3 threshold.py",
     "Theorem (first overlap of adjacent strata, S*(p)); Figure F7 (S*(p) and first collision; the stratum intervals R^+-_{S,p} are not stored)"),
    ("theory/threshold/threshold_output.txt", "theory/threshold/threshold.py", "cd theory/threshold && python3 threshold.py > threshold_output.txt",
     "Theorem (first overlap), checks C1-C5"),
    ("theory/curvature/curvature_output.txt", "theory/curvature/curvature_checks.py",
     "cd theory/curvature && python3 curvature_checks.py > curvature_output.txt", "Section on curvature: flat and spherical comparison (Theorems F, S)"),
    ("theory/divergence/divergence_output.txt", "theory/divergence/divergence.py",
     "cd theory/divergence && python3 divergence.py > divergence_output.txt", "Theorem (divergence of the cone coefficients) and its checks D1-D6"),
    # --- Diophantine
    ("theory/diophantine/data/per_S.csv", "theory/diophantine/enumerate_fast.py (+ enumerate_core.c)",
     "cd theory/diophantine && python3 enumerate_fast.py 4800   (hours; parallel)", "Figure F9 (degeneracy growth); Table tab:density; Conjecture 5.3 (contradicted; revised to N(S) = S^(1+o(1)), kappa = 4.5 +/- 0.5)"),
    ("theory/diophantine/data/groups.csv", "theory/diophantine/enumerate_fast.py", "cd theory/diophantine && python3 enumerate_fast.py 4800",
     "Figure F9 (rational points of C_lambda, e.g. C_{27/2}); Section 5 families"),
    ("theory/diophantine/data/growth_fits.txt", "theory/diophantine/growth_fits.py", "cd theory/diophantine && python3 growth_fits.py",
     "Figure F9 (growth law fits, local exponent); Conjecture 5.3"),
    ("theory/diophantine/data/birthday.csv", "theory/diophantine/growth_fits.py", "cd theory/diophantine && python3 growth_fits.py",
     "Section 5.3 (the birthday heuristic, audit)"),
    ("theory/diophantine/data/exponent_fits.txt", "theory/diophantine/exponent_fits.py", "cd theory/diophantine && python3 exponent_fits.py",
     "Figure F9 (log-power exponent)"),
    ("theory/diophantine/data/families.txt", "theory/diophantine/families.py", "cd theory/diophantine && python3 families.py 4800 7",
     "Section 5 (parametric families, lower bound)"),
    ("theory/diophantine/data/line_families.csv", "theory/diophantine/families.py", "cd theory/diophantine && python3 families.py 4800 7",
     "Section 5 (degree-2 families)"),
    ("theory/diophantine/data/variety_checks.txt", "theory/diophantine/variety_checks.py", "cd theory/diophantine && python3 variety_checks.py",
     "Section 5 (the degeneracy variety, Beauville pencil); Figure F9 (the curve C_Lambda)"),
    ("theory/diophantine/data/ranks.txt", "theory/diophantine/ranks.py", "cd theory/diophantine && .venv-pari/bin/python ranks.py   (needs cypari2 2.2.4)",
     "Section 5 (Mordell-Weil ranks; rank C_{27/2} = 0); Figure F9"),
    # --- numerics S3
    ("numerics/data/eigenvalues_*.csv", "numerics/solve.py (solver) + numerics/validate.py (table)",
     "cd numerics && python3 solve.py suite && python3 validate.py   (writes numerics/runs/, not committed)",
     "Section on numerics; Table of first eigenvalues; input to F1, F5 and to the blind recovery"),
    ("numerics/data/convergence.csv", "numerics/validate.py", "cd numerics && python3 validate.py", "Numerics appendix: convergence in h and p"),
    ("numerics/data/weyl.csv", "numerics/validate.py", "cd numerics && python3 validate.py", "Numerics appendix: Weyl law with boundary term and constant a_0/2"),
    ("numerics/data/bolza_benchmark.csv", "numerics/validate.py", "cd numerics && python3 solve.py bench && python3 validate.py",
     "Numerics appendix: Bolza benchmark (Strohmaier-Uski)"),
    ("numerics/data/heat_trace_checks.csv", "numerics/validate.py", "cd numerics && python3 validate.py",
     "Figure F3 (quantitative companion: Z_N - Z_D against the mirror term); numerics appendix"),
    ("numerics/data/heat_trace_difference.csv", "numerics/heat_trace.py", "cd numerics && python3 heat_trace.py",
     "Figure F5 (two timescales, the S3 difference D(t)); Theorem B numerical confirmation"),
    ("numerics/data/fits.csv", "numerics/heat_trace.py", "cd numerics && python3 heat_trace.py", "Theorem B numerical confirmation (fit scan for d_3, d_4; code names c1, c2)"),
    ("numerics/data/headline.json", "numerics/heat_trace.py", "cd numerics && python3 heat_trace.py", "Theorem B numerical confirmation: d_3 = 25/12, d_4 = -1775/24 recovered, verdict"),
    ("numerics/data/heat_kernel_diagonal.npz", "numerics/heat_trace.py", "cd numerics && python3 heat_trace.py kernel   (needs the solver runs and NGSolve)",
     "Figure F1 (pillows coloured by heat-kernel diagonal, (2,8,8) and (3,3,12))"),
    ("numerics/data/rerun_double_window_comparison.json", "numerics/rerun_double_window.py",
     "cd numerics && python3 rerun_double_window.py SCRATCH_DIR   (NGSolve; about an hour)", "Numerics appendix: the production eigenvalues reproduced by the double-window solver"),
    # --- moduli experiment
    ("numerics/moduli/data/convergence.csv", "numerics/moduli/analysis.py", "cd numerics/moduli && python3 analysis.py   (needs runs/ from the server suite)",
     "Moduli experiment (Section 4 numerics): production eigenvalues of all 64 sector problems"),
    ("numerics/moduli/data/eigenvalue_flow_*.csv", "numerics/moduli/analysis.py", "cd numerics/moduli && python3 analysis.py", "Figure F6 (eigenvalue flow along the moduli family)"),
    ("numerics/moduli/data/geometries.json", "numerics/moduli/analysis.py", "cd numerics/moduli && python3 analysis.py", "Figure F6 (the family O(tau), systoles); moduli experiment table"),
    ("numerics/moduli/data/length_spectra.csv", "numerics/moduli/analysis.py", "cd numerics/moduli && python3 analysis.py", "Figures F5 and F6 (length spectra; geodesic terms)"),
    ("numerics/moduli/data/heat_traces.csv", "numerics/moduli/analysis.py", "cd numerics/moduli && python3 analysis.py", "Figure F5 (moduli traces vs the trace formula)"),
    ("numerics/moduli/data/trace_differences.csv", "numerics/moduli/analysis.py", "cd numerics/moduli && python3 analysis.py", "Figure F5 (two timescales: moduli trace differences Z_i - Z_j = H_i - H_j)"),
    ("numerics/moduli/data/weyl.csv", "numerics/moduli/analysis.py", "cd numerics/moduli && python3 analysis.py", "Moduli experiment: Weyl law with a_0 = 7/9"),
    ("numerics/moduli/data/summary.json", "numerics/moduli/analysis.py", "cd numerics/moduli && python3 analysis.py", "Moduli experiment: every number quoted in the text"),
    ("numerics/moduli/data/s3_geodesic_check.csv", "numerics/moduli/check_geodesics_s3.py", "cd numerics/moduli && python3 check_geodesics_s3.py",
     "Numerics appendix: S3 traces against the full trace formula with geodesic terms"),
    ("numerics/moduli/data/s3_repro.json", "numerics/legacy/s3_repro.py (old single-window solver, server)", "python3 numerics/legacy/s3_repro.py [threads]",
     "Numerics appendix: cross-machine reproducibility of the (3,3,12) Neumann eigenvalues (record of the old solver)"),
    ("numerics/moduli/data/heat_kernel_diagonal_moduli.npz", "numerics/moduli/kernel.py", "cd numerics/moduli && python3 kernel.py   (needs the solver runs and NGSolve)",
     "Figures F1 and F6 (heat-kernel diagonal of two contrasting members of the moduli family)"),
    ("numerics/moduli/logs/*.txt", "numerics/moduli/run_server.sh", "bash numerics/moduli/run_server.sh suite|fullquad|kernel   (on the server)",
     "Provenance of the moduli data (server logs); not cited"),
]

ENV_FILES = [
    ("requirements.txt", "exact-arithmetic suite (code/run_all.sh): sympy, mpmath, numpy, scipy"),
    ("code/requirements.txt", "the harness stages of run_all.sh (includes ../requirements.txt)"),
    ("numerics/requirements.txt", "S3 solver environment (Python 3.13, NGSolve 6.2.2607)"),
    ("numerics/moduli/env/requirements.txt", "moduli solver environment as built on the server"),
    ("numerics/moduli/env/environment.yml", "moduli conda environment"),
    ("numerics/moduli/env/conda-explicit.server.txt", "moduli conda environment, explicit package list"),
    ("numerics/moduli/env/pip-freeze.server.txt", "moduli pip freeze"),
    ("theory/diophantine/requirements-pari.txt", "PARI/GP for ranks.py (cypari2 2.2.4)"),
]

# Rules allowed to match no file yet: the file is listed as DEFERRED in the manifest.
PENDING = {"numerics/data/rerun_double_window_comparison.json"}

# Figure plan (brief): id, title, data files, status, note
FIGURES = [
    ("F1", "Pillows coloured by the heat-kernel diagonal",
     ["numerics/data/heat_kernel_diagonal.npz", "numerics/moduli/data/heat_kernel_diagonal_moduli.npz"], "EXISTS",
     "Points, triangles and K(t,x,x) at t = 0.005, 0.01, 0.02 for (2,8,8) and (3,3,12) (S3); two moduli members (S5)."),
    ("F2", "Hyperboloid tilings",
     [], "NO DATA FILE NEEDED",
     "Drawn from the exact triangle vertices of numerics/geometry.py (mpmath) and the reflection group; no stored data. The figure script does not exist yet (S10)."),
    ("F3", "Mirror-argument schematic",
     ["numerics/data/heat_trace_checks.csv"], "EXISTS (quantitative companion only)",
     "A schematic; the numbers it can quote (Z_N - Z_D against the mirror term) are in heat_trace_checks.csv."),
    ("F4", "Coefficient count vs area (signatures area_classes)",
     ["theory/signatures/output/area_classes.txt"], "PARTIAL: TEXT TRANSCRIPT ONLY; per-class table to be generated in the figure stage",
     "525 area classes and the histograms exist only as a transcript, with the 'largest max K_mult' list printed. There is no per-class table (s, class size, bound, max K_mult). To be generated in the figure stage (a CSV writer in theory/signatures/area_classes.py)."),
    ("F5", "Two timescales (S3 D(t) and moduli trace differences)",
     ["numerics/data/heat_trace_difference.csv", "numerics/moduli/data/trace_differences.csv", "numerics/moduli/data/heat_traces.csv", "numerics/moduli/data/length_spectra.csv"], "EXISTS", ""),
    ("F6", "Moduli family and eigenvalue flow",
     ["numerics/moduli/data/geometries.json", "numerics/moduli/data/eigenvalue_flow_orbifold.csv", "numerics/moduli/data/eigenvalue_flow_sectors.csv", "numerics/moduli/data/length_spectra.csv"], "EXISTS",
     "Eigenvalue flow stores the first 400 eigenvalues of each member (120 per sector)."),
    ("F7", "Stratum intervals and S*(p)",
     ["theory/threshold/first_overlap_vs_collision.csv"], "PARTIAL: S*(p) ONLY; stratum intervals to be generated in the figure stage",
     "The CSV holds S*(p), the first collision and the window sizes. The stratum intervals [R^-_{S,p}, R^+_{S,p}] themselves are computed inside threshold.py and not saved; To be generated in the figure stage (a CSV of the endpoints)."),
    ("F8", "Recovery error vs coefficient error (stability)",
     ["theory/stability/threshold_results.json", "theory/stability/blind/result.json"], "PARTIAL: THRESHOLDS AND TWO POINTS ONLY; recovery-error sweep to be generated in the figure stage",
     "threshold_results.json has the certified and constructed failure thresholds for 11 orbifolds; blind/result.json the two recovered specimens. The curve itself (recovery error against a swept coefficient perturbation) was never computed. To be generated in the figure stage (from theory/stability/stab_common.py)."),
    ("F9", "The curve C_{27/2} and degeneracy growth",
     ["theory/diophantine/data/per_S.csv", "theory/diophantine/data/groups.csv", "theory/diophantine/data/growth_fits.txt", "theory/diophantine/data/exponent_fits.txt", "theory/diophantine/data/variety_checks.txt", "theory/diophantine/data/ranks.txt"], "EXISTS",
     "The cubic is drawn from its equation (x+y+z)(xy+yz+zx) = (27/2)xyz; its rational points are the rows of groups.csv with S*R = 27/2."),
]


# ------------------------------------------------------------------------------ build
def tracked():
    out = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT).decode().split("\0")
    return sorted(f for f in out if f)


def is_data(f):
    if f.startswith(("research/", "refs/")):
        return False
    name = f.rsplit("/", 1)[-1]
    if f in {e for e, _ in ENV_FILES} or name.startswith("requirements") or name in ("environment.yml",) \
            or name.endswith((".server.txt",)):
        return False
    if name in ("README.md",) or name == ".gitkeep":
        return False
    return f.endswith((".csv", ".json", ".npz", ".txt")) or f.endswith("_output.md") \
        or f == "theory/stability/blind/RESULT.md" or (f.startswith("paper/tables/") and f.endswith(".tex"))


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def human(n):
    if n < 1024:
        return f"{n} B"
    if n < 1024 ** 2:
        return f"{n / 1024:.1f} KB"
    return f"{n / 1024 ** 2:.2f} MB"


def build():
    files = [f for f in tracked() if is_data(f)]
    used = {i: 0 for i in range(len(RULES))}
    rows = []
    for f in files:
        hit = [i for i, r in enumerate(RULES) if fnmatch.fnmatchcase(f, r[0])]
        assert len(hit) == 1, f"{f}: matches {len(hit)} rules (need exactly one): {hit}"
        used[hit[0]] += 1
        rows.append((f, RULES[hit[0]]))
    stale = [RULES[i][0] for i, c in used.items() if c == 0 and RULES[i][0] not in PENDING]
    assert not stale, f"rules that match no committed file: {stale}"
    pending = [RULES[i] for i, c in used.items() if c == 0]
    for fig in FIGURES:
        for p in fig[2]:
            assert p in files, f"{fig[0]}: {p} is not a tracked data file"
    for p, _ in ENV_FILES:
        assert (ROOT / p).exists(), p

    L = []
    w = L.append
    w("# DATA-MANIFEST\n")
    w("Every committed data file, with its size, SHA-256, the script and command that generates it, and the "
      "paper element that will use it. Generated by `admin/build_data_manifest.py` (rebuild with "
      "`python3 admin/build_data_manifest.py`); `code/run_all.sh` fails if this file is out of date, "
      "so a changed file or a new data file must be re-registered here.\n")
    w(f"{len(files)} data files, {sum((ROOT / f).stat().st_size for f in files) / 1e6:.1f} MB. "
      "Environment specifications are listed at the end. \"Writes\" commands overwrite the committed file: "
      "the reproduction suite never runs them in place without checking that the result is byte-identical "
      "(code/data_guard.py).\n")
    w("## Figures F1-F9\n")
    w("| Figure | Content | Data files | Status |")
    w("|---|---|---|---|")
    for fid, title, paths, status, note in FIGURES:
        pl = "<br>".join(f"`{p}`" for p in paths) if paths else "none"
        w(f"| {fid} | {title} | {pl} | **{status}**{('. ' + note) if note else ''} |")
    flagged = [f for f in FIGURES if not f[3].startswith("EXISTS")]
    w("\n**Figures whose data does not yet exist or is incomplete:** "
      + "; ".join(f"{f[0]} ({f[3].lower()})" for f in flagged) + ".\n")
    w("## Data files\n")
    cur = None
    for f, (pat, gen, cmd, elem) in rows:
        d = f.rsplit("/", 1)[0] if "/" in f else "."
        if d != cur:
            cur = d
            w(f"\n### `{d}/`\n" if d != "." else "\n### repository root\n")
            w("| File | Size | SHA-256 | Generator | Command | Paper element |")
            w("|---|---:|---|---|---|---|")
        size = (ROOT / f).stat().st_size
        name = f.rsplit("/", 1)[-1]
        w(f"| `{name}` | {human(size)} | `{sha256(ROOT / f)}` | `{gen}` | `{cmd}` | {elem} |".replace("|`", "| `"))
    if pending:
        w("\n### Deferred (not generated in this consolidation)\n")
        w("| File | Status | Generator | Command | Paper element |")
        w("|---|---|---|---|---|")
        for pat, gen, cmd, elem in pending:
            w(f"| `{pat}` | **DEFERRED: the full S3 rerun is deferred to the final submission check; T3 is verified by existing checks (heat traces match the trace formula to 7e-13, numerics/REPORT.md section 4d; the server rerun of (3,3,12) Neumann matched all 1434 committed eigenvalues, numerics/moduli/data/s3_repro.json)** | `{gen}` | `{cmd}` | {elem} |")
    w("\n## Environment specifications\n")
    w("| File | Size | SHA-256 | Purpose |")
    w("|---|---:|---|---|")
    for p, purpose in ENV_FILES:
        w(f"| `{p}` | {human((ROOT / p).stat().st_size)} | `{sha256(ROOT / p)}` | {purpose} |")
    return "\n".join(L) + "\n"


def main():
    text = build()
    if "--check" in sys.argv:
        assert OUT.exists(), "DATA-MANIFEST.md is missing"
        committed = OUT.read_text()
        if committed != text:
            import difflib
            diff = list(difflib.unified_diff(committed.splitlines(), text.splitlines(), "committed", "current", lineterm="", n=0))
            sys.stderr.write("\n".join(diff[:30]) + "\n")
            raise SystemExit("DATA-MANIFEST.md is out of date: run python3 admin/build_data_manifest.py")
        print(f"DATA-MANIFEST.md is current ({text.count(chr(10))} lines)")
    else:
        OUT.write_text(text)
        print(f"wrote {OUT} ({text.count(chr(10))} lines)")


if __name__ == "__main__":
    main()
