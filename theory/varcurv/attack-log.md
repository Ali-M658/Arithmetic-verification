# Attack log: theory/varcurv

**Attacker.** A separate subagent was given only `statements.tex`: no proofs, no scripts, no outputs. It
fetched Schueth 2019 and 2026, DGGW, Ucar and Vassilevich itself, and wrote its own exact code. Its files
are in `attack/`, and its full report is `attack/ATTACK-REPORT.md`.

**Its method.** It did not use the MP/Hamilton-Jacobi method of `twisted_mp.py`. Instead it rescaled the
neighbourhood of the fixed point, applied a Duhamel expansion around the flat rotation and took exact
Gaussian traces (`attack/twisted_duhamel.py`, b_0..b_5). It calibrated against Donnelly's b_0, b_1,
Schueth's Thm 3.7 and Thm 4.1, and Ucar for l <= 5, m = 2..15.

| Statement | Verdict | Disposition |
|---|---|---|
| VC1 structure | CONFIRMED for l <= 5. No C^0 term and no positive powers. m*Pi_i exact for m <= 21; degree, parity and leading coefficient checked for i <= 7. | none |
| VC1 hypothesis m >= l-1 | CONFIRMED to be necessary. At l = 4, m = 2: b_4(pi) = (7/480) h_2^2 + radial part, with h_2 the traceless Hessian of K. Non-radial Z_2/Z_4 jets do not enter b_1..b_3. | Kept the hypothesis; the m = 2 term is recorded in varcurv.tex Remark (a). |
| VC2 top coefficient | CONFIRMED. Equals the top coefficient of the attacker's b_l for l = 1..5. (i) holds for all l: the k_{l-1} coefficient is exactly 2*4^{l-1}(l-1)!. (ii) holds for l <= 12. (iii), including the l = 4 formula, is exact. (iv) reproduces Schueth's m^5 coefficient. | none |
| VC3 t^3 | CONFIRMED exactly by an independent method. A, B, D agree as rational functions and by direct averaging for m = 2..15; A matches Ucar for m = 2..30; also checked with non-radial Z_2 and Z_4 jets. | none |
| VC4 extension | CONFIRMED. Brute force over 495 signatures (kappa = +-1, L = 2..7) and over the J-version. The kappa = 0 failure holds given VC6. Noted redundancy: S_0 = chi^orb/6, so equal S_0 forces equal chi^orb. | Already phrased that way in varcurv.tex ("Then chi^orb(O) = chi^orb(O')"). |
| VC5 finite order | CONFIRMED IN PART. Necessity and the example check out. No obstruction found: the inequality int K^2 >= (int K)^2/Area bounds S_1 only from below and does not block matching. | Sufficiency is a proof, not a computation; no change. |
| VC6 all orders | CONFIRMED IN PART. The examples satisfy the hypotheses. The point at infinity is regular and the extra point is an exact flat cone with the same alpha_0 in each pair (5/4, 7/5). Flat cone points contribute 0 beyond t^0, and there are no half powers or logs (DGGW Thm 4.8). | none |
| VC5a quadratic form | VALUES CONFIRMED (F_n checked for n <= 9; F_3 = -1/140 matches Gilkey's a_6 as given in Vassilevich (4.29)). SIGN BROKEN AS WRITTEN: under the file's convention Delta = -div grad, "(-Delta_0)^{l+1}" has the wrong sign for even l. | **Fixed** in statements.tex, varcurv.tex, quadratic_form.py and paperA-insert.tex: now Delta_0^{l+1} with Delta_0 = -(d_1^2 + d_2^2) >= 0, i.e. int psi Delta_0^{l+1} psi = int abs(zeta)^{2l+2} abs(psi^)^2 / (2pi)^2. The proof of VC5 uses only F_{l+1} != 0, so it is unaffected. |

**Extra datum from the attacker.** The full radial b_4, with X = C^{-2}:

    b_4 = (1680K^4 - 904K^2 DK + 98/3 K D2K + 124/3 DK^2 - 1/3 D3K) X^5
        + (-600K^4 + 280K^2 DK - 20/3 K D2K - 10 DK^2) X^4
        + (52K^4 - 52/3 K^2 DK + 1/3 DK^2) X^3
        - (2/3) K^4 X^2.

Its X^5 part agrees with `top_coefficient.py`. The lower part was computed by one method only, and is
recorded in STATUS.md as such, not as a theorem.

**Not tested.** VC2's averaged formula on general non-radial jets beyond Z_2/Z_4 at l <= 3; a non-radial
jet at l = 4, m = 3 (safe by the weight count).
