# Sources for the moduli dimension of cone spheres

Fetched 2026-10-01 by headless curl with a desktop User-Agent. Nothing below is recalled from memory.

## Troyanov, Trans. Amer. Math. Soc. 324 (1991), 793-821, DOI 10.1090/S0002-9947-1991-1005085-9

Route: `https://www.ams.org/journals/tran/1991-324-02/S0002-9947-1991-1005085-9/S0002-9947-1991-1005085-9.pdf` (HTTP 200, 29 pp.). Page 1 (printed p. 793), Theorem A, verbatim from the extracted text (the text layer reads "conformai" for "conformal" and "6" for theta; left as printed):

> Theorem A. Let S be a compact Riemann surface. Let p_1, p_2, ..., p_n be points of S and theta_1, theta_2, ..., theta_n be positive numbers. Assume
> 2 pi chi(S) + sum_{i=1}^{n} (theta_i - 2 pi) < 0.
> Then any smooth negative function on S is the curvature of a unique conformal metric having at p_i a conical singularity of angle theta_i.

Use made of it: taking the negative function to be the constant -1 and theta_i = 2 pi / m_i, a hyperbolic cone metric on the sphere with cone angles 2 pi / m_i is the same datum as a conformal structure on the sphere with n marked points labelled by the orders m_i. The hypothesis reads sum_i (1 - 1/m_i) > 2, which is the hyperbolicity condition of the manuscript.

## Thurston, Geom. Topol. Monogr. 1 (1998), 511-549, DOI 10.2140/gtm.1998.1.511 (arXiv:math/9801088v2)

Route: `https://arxiv.org/pdf/math/9801088v2` (HTTP 200, 41 pp.); arXiv API record agrees with the journal reference. Abstract, verbatim (page 1):

> The space of shapes of a polyhedron with given total angles less than 2 pi at each of its n vertices has a Kaehler metric, locally isometric to complex hyperbolic space CH^{n-3}.

Scope caveat: this is the *Euclidean* (flat, positive-curvature-at-vertices) cone-metric statement. It gives complex dimension n-3, i.e. real dimension 2n-6, for that moduli space. The hyperbolic case used in the manuscript is obtained from Troyanov's Theorem A (above) together with the dimension count for n marked points on the Riemann sphere; the abstract of Thurston is the fetched evidence for the count n-3 in the flat analogue, which parametrises the same underlying conformal data. No fetched source states "real dimension 2n-6" for hyperbolic cone spheres in one sentence; that is a two-step deduction, flagged as such in `definitions.tex`.

## Not fetched

The dimension 6g-6+2n for signature (g; m_1, ..., m_n) with g >= 1 is not supported by a fetched record here, so `definitions.tex` states it only for g = 0 and carries a comment marking the general-genus statement as needing a source.

## Discarded guess

An arXiv identifier guessed from memory for Thurston's paper (math/9809110) was fetched and turned out to be an unrelated paper; it was discarded. The identifier above comes from the arXiv API search by title and author.
