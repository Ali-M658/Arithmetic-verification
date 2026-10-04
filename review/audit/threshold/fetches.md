# Threshold / paper-core audit: sources used and gaps

Sources read (all from `review/audit/sources/`, no new retrieval was needed):

| source | location used | used for |
|---|---|---|
| Uçar, arXiv:1711.03405 | (4.22)-(4.25), (4.33)-(4.35), Thm 4.20 and its proof, Cor 4.21, Def 4.22, (4.38) | cone terms C_0, C_1, C_2 (symbolic in k); smooth a_0, a_1, a_2; linearity of b_1 in K (Thm 4.20 proof: phi(gamma,x) psi(gamma,x) with psi a universal curvature polynomial) |
| DGGW, arXiv:0805.3148 | 5.2-5.6, (5.7)-(5.10) | b_0(gamma^j) = 1/(4 sin^2), Lemma 5.4, degree-zero term (5.7), degree-one cone term R1212 (m^4+10m^2-11)/(360 m) |
| Schueth, arXiv:1812.06119 | Rem 3.2, eq. (17), Thm 4.1, Rem 4.2, p. 13 (expansion structure) | b_0, b_1 for a cone point; integer powers for orientable orbisurfaces (half powers only with mirror lines) |

Independent derivation (no literature input): exact small-t expansion of the heat trace of the
round spherical orbifolds S^2/G for G = C_n, D_n, T, O, I from the multiplicities
d_l = dim(H_l)^G, via Hurwitz zeta values at negative integers (`check_heat.py`, part D).

Gaps (not fetched; nothing in the verdicts depends on them):

- Donnelly 1976, Steinig 1971, Drury-Marshall 1987: accepted standing gaps.
- McKean-Singer 1967, Suleymanova 2017, "nrs2024", "schueth2025" (cited in PC.3/PC.8): not in the
  source set. The PC.3 sentence attributing the absence of half-integer/log terms to constant
  curvature is assessed against Schueth arXiv:1812.06119 p. 13 and DGGW Thm 4.8 only.
