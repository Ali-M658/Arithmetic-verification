# Figure references: what published papers near ours do, and what we take from them

Working notes for the figures of "How much of a hyperbolic orbifold does heat hear?" (target: The Journal of Geometric Analysis). We looked at the figures of 14 peer-reviewed papers that are close to ours in subject or in the kind of plot: computed spectra of hyperbolic surfaces and orbifolds, hyperbolic tilings, trace-formula numerics, elliptic-curve data, recent JGA and Experimental Mathematics articles, and convergence plots from numerical analysis. Every paper was retrieved headless on 2026-10-04. We used the arXiv e-print source (original figure files, rendered locally) or the arXiv PDF, and checked each citation against the arXiv API and Crossref. Downloads were kept in the git-ignored folder `figures/_fetched/refs/`. No third-party figure or image is in the repository, and the notes below describe figures in words only. Figure numbers are those of the arXiv version, which can differ from the journal version. One more paper was opened and set aside as not relevant: S. Farrington, JGA 35 (2025) 62, arXiv 2308.12245. Its only data figures are optimal shapes.

Labels F1 to F9 refer to our planned figures: F1 pillow renders, F2 triangle-group tilings, F3 number-line proof schematic, F4 coefficients needed vs area, F5 heat-trace differences, F6 eigenvalue flow, F7 drifting intervals, F8 log-log error with slopes, F9 cubic real locus and N(S).

---

## 1. Strohmaier and Uski (2013): Bolza surface spectra

A. Strohmaier, V. Uski, "An algorithm for the computation of eigenvalues, spectral zeta functions and zeta-determinants on hyperbolic surfaces", *Comm. Math. Phys.* 317(3) (2013) 827-869, DOI 10.1007/s00220-012-1557-1 (correction: 10.1007/s00220-018-3094-z). arXiv:1110.2150.

**Figures looked at**
- Fig. 3: a Y-piece glued from a right-angled octagon in the upper half-plane. The drawing uses black lines only, with sides labelled a to h.
- Fig. 4: the quantity beta(N) on a log y-axis against N, shown as dots.
- Fig. 6: the smallest singular value against lambda for the Bolza surface. Eigenvalues show up as cusps touching zero.
- Fig. 7: zeta_Delta(s) against s, drawn as a single curve.

**What works and what does not**
- Fig. 4 is a good minimal semilog plot. It has one series, dots rather than a line (N is discrete), and decade labels 10^-4 to 10^-14 that make the exponential decay obvious.
- Fig. 6 shows the method itself: you read eigenvalues where the curve touches zero. But it is a default gnuplot graph. It has a red line, a pointless legend box naming the only curve, no x-axis label, and too many y ticks (0.05 steps) with unaligned decimals.
- Fig. 7 is a default Mathematica plot. The axes cross in the middle, the tick labels are tiny, there is no frame, and the y label sits at the top of the axis. It is readable but looks unfinished at journal size.
- Fig. 3 is clean: thin black strokes and letter labels next to the arcs. A dashed arc marks the auxiliary construction.

**Adopt**
- F4, F5: when the abscissa is discrete, use dots and no connecting line. Label log axes with powers of ten only.
- F2, F3: line drawings in black with letter labels set close to the curve they name, and dashed strokes for auxiliary or hidden elements.

**Avoid**
- F4, F5, F6, F8: a legend for a plot with only one series.
- All plots: default Mathematica axes crossing at the origin, and a missing x-axis label.
- All plots: tick steps finer than about five or six labelled ticks per axis.

## 2. Levitin and Strohmaier (2021): resonances under deformation

M. Levitin, A. Strohmaier, "Computations of eigenvalues and resonances on perturbed hyperbolic surfaces with cusps", *Int. Math. Res. Not. IMRN* 2021(6) 4003-4050, DOI 10.1093/imrn/rnz157. arXiv:1812.05554.

**Figures looked at**
- Fig. 2: a 3D render of part of a cusp embedded in R^3 (a pseudosphere-like funnel). It has a blue-white-yellow-red colour ramp along the length, a thin black coordinate mesh, and soft lighting.
- Fig. 8: trajectories of four resonances in the complex s-plane as a parameter r varies. Each is drawn in its own colour and dash style. A filled circle marks the start and a filled square the end, and vertical reference lines are drawn at Re s = 0, 1/4, 1/2.
- Fig. 10: a fundamental domain. Identified boundary arcs share a colour and a dash pattern, the shading is two-tone grey, and arcs are labelled gamma_1 to gamma_7.
- Fig. 13a: resonances at a special parameter value, shown as dots on three vertical lines.

**What works and what does not**
- Fig. 8 is the closest published analogue to our F6, and it is very good. Each curve is doubly encoded, by colour and by dash pattern (solid, dashed, dotted, dash-dot), so it survives greyscale printing. Start and end markers give the direction of the flow without arrows. The title gives the family name, and the axes are labelled "Re s" and "Im s" at the axis ends.
- Fig. 10 doubly encodes the gluing as well (same colour plus same dash for identified sides). The paper caption says so explicitly, and that is the practice we should copy for side pairings.
- Fig. 2 shows that a stylised 3D surface reads well at small size with soft shading, a sparse mesh, and an empty background. But its rainbow-like ramp has no stated meaning in the caption. It encodes height only.
- Some tick labels carry a trailing decimal point ("0." in Fig. 8), a Mathematica artefact.

**Adopt**
- F6: distinguish branches by colour and by line style together. Mark the start and end of each branch with different marker shapes (open or filled circle at theta_0, square at theta_1) instead of arrows. Add thin vertical reference lines for distinguished parameter values.
- F2: show side pairings or reflection mirrors with matched colour plus matched dash, and say so in the caption.
- F1: a sparse thin mesh over a smoothly shaded surface on a white background, with no axes or box.

**Avoid**
- F1: a colour ramp whose meaning is not stated. If we colour by the heat-kernel diagonal, give a colour bar or say "darker = larger" in the caption.
- All plots: Mathematica tick artefacts such as "0." and "0.5" next to "0.25".

## 3. Kravchuk, Mazáč and Pal (2024): orbifold spectra and the bootstrap

P. Kravchuk, D. Mazáč, S. Pal, "Automorphic spectra and the conformal bootstrap", *Comm. Amer. Math. Soc.* 4 (2024) 1-63, DOI 10.1090/cams/26. arXiv:2111.12716.

**Figures looked at**
- Fig. 2: the conjectured set of lambda_1 values of hyperbolic orbifolds, drawn on a single horizontal number line. A thick blue bar covers the continuum [0, 15.79...], and short blue ticks mark isolated values. Each tick has a rotated orbifold signature such as [0;2,3,7] above it and a rotated numerical value below it.
- Fig. 4: "artist's impression" of a [0;k1,k2,k3] orbifold. It is a curved-sided triangle with cone tips and cross-section ellipses (solid front, dashed grey back), drawn only in thin black strokes.
- Fig. 5: an extremal functional against lambda. Short red ticks on the axis mark zeros, labelled with their numerical values.

**What works and what does not**
- Fig. 2 is the closest published analogue to our F3. One axis, an arrowhead, a single end label (lambda_1), and every element annotated in place. There is no legend, no y-axis and no frame. The rotated labels avoid collisions but cost some legibility. Stacking two signatures over one tick works.
- Fig. 4 shows that a schematic pillow-like orbifold reads well with a few strokes. "Not to scale" in the caption is honest and worth copying for F1.
- Fig. 5 puts the important x-values directly on the axis as coloured ticks with labels instead of using a legend. The y-axis label is a long formula placed at the top of the axis. It is fine in a plot with a single series.

**Adopt**
- F3: draw a single bare axis with an arrowhead and the variable name at the right end, and no frame or y-axis. Mark multiset elements as short ticks or dots with the label beside them, and stack labels where a value repeats (multiplicity). Use a thick bar for a continuum or interval.
- F1: in the caption, say plainly when a 3D render is stylised and not an isometric embedding.
- F5, F6: mark special abscissae (critical times, the parameter values where eigenvalues cross) with short coloured ticks on the axis itself.

**Avoid**
- F3: rotated labels at 45 degrees unless they are unavoidable. Use staggered horizontal labels first.

## 4. Attar and Boettcher (2022): Selberg trace formula numerics

A. Attar, I. Boettcher, "Selberg trace formula in hyperbolic band theory", *Phys. Rev. E* 106 (2022) 034114, DOI 10.1103/PhysRevE.106.034114. arXiv:2201.06587.

**Figures looked at**
- Fig. 1: the {8,3} tiling (grey) with the {8,8} lattice (orange) on top, in the Poincaré disk, plus a second disk showing generators as black arrows.
- Fig. 3: band curves E_lambda(k), drawn as a family of blue curves.
- Fig. 4: a grid of 15 small Poincaré disks, each showing one primitive closed geodesic (blue) over the fundamental octagon (orange). Row labels give n=1, 2, 3, ..., and a multiplicity such as "x8" sits at the bottom right of each disk.
- Fig. 5a: the partition function Z(beta,0) as "total" (solid blue) = "integral" (dashed orange) + "orbit sum" (dashed red), with a dotted black asymptote at 1.
- Fig. 5b: computed E_0(k) against an approximation.

**What works and what does not**
- Fig. 5a is the closest published analogue to our F5 (the identity-term part against the length-spectrum part of a trace formula). Labelling each curve in place, in its own colour, removes the legend completely and reads very well. The dotted asymptote is a good reference device. A weakness is that the orange and red dashed curves rely on hue alone: in greyscale they become two identical dashed lines.
- Fig. 4 is a strong "catalogue" layout of small multiples. Every panel uses the same frame, the geometry is in thin orange, the geodesic in thicker blue, and the counts are in small type. It explains the length spectrum at a glance.
- Fig. 1 uses line weight and colour to separate two superimposed tilings, and the shaded central cell marks the fundamental domain. Tilings are drawn out to a thin boundary circle, with edges thinning naturally toward it.
- In Fig. 3, all branches are one colour, so crossings and avoided crossings cannot be followed by eye.
- The fonts are a grey sans-serif Mathematica style that does not match the text font.

**Adopt**
- F5: label curves directly on the plot ("asymptotic series", "computed", "geodesic terms") in the curve's own colour. Draw horizontal reference levels, such as the noise floor, as dotted black lines.
- F2: show the fundamental domain as a lightly tinted region under the tiling lines. Use two line weights to separate the tiling from overlaid structure.
- F5 or a possible supplementary panel: a small-multiples grid with identical framing when showing several closed geodesics or several orbifolds.

**Avoid**
- F6: a monochrome family of eigenvalue branches when crossings matter (Fig. 3). Every branch, or at least the tracked ones, needs its own style.
- F5: two dashed curves separated only by hue.
- All figures: grey sans-serif tick fonts. Match the serif text font of the paper.

## 5. Boettcher, Gorshkov, Kollár, Maciejko, Rayan and Thomale (2022): hyperbolic tilings

I. Boettcher, A. V. Gorshkov, A. J. Kollár, J. Maciejko, S. Rayan, R. Thomale, "Crystallography of hyperbolic lattices", *Phys. Rev. B* 105 (2022) 125118, DOI 10.1103/PhysRevB.105.125118. arXiv:2105.01087.

**Figures looked at**
- Fig. 1: Euclidean {3,6}, {4,4} and {6,3} tilings and hyperbolic {7,3}, {8,3} and {8,4} tilings in the Poincaré disk, all as single-colour line art with the label below each.
- Fig. 4: the central octagon of {8,8} in the disk, with the right triangle (angles pi/p, pi/2, pi/q) highlighted in red and sides labelled A, B, C. The axes run from -1 to 1.
- Fig. 6: a 3D render of a genus-2 surface as two glued tori. The surface has a lilac shading with specular highlights, and four coloured curves mark the side pairings.

**What works and what does not**
- Fig. 1 is a clean triptych comparing tilings. Every panel has the same size and line weight, and its label is set in math type below it. The hyperbolic disks are drawn to a depth where the boundary turns into a dark rim. That rim is a typical artefact: at a uniform line weight the boundary ink saturates.
- Fig. 4 is good for showing one triangle of a triangle group: the fundamental triangle is shaded and labelled, and the polygon is in a second colour. The Cartesian axes with ticks from -1 to 1 add nothing for a disk-model picture.
- Fig. 6 is the closest published analogue to our F1 render. It uses smooth Phong-style shading and saturated curves drawn on the surface. The shading carries no data, so the colour is decorative. With our heat-kernel colouring, a strong specular highlight would bias how the colour is read.

**Adopt**
- F2: make each tiling panel the same size and line weight, with the group label in math type below it, such as (2,8,8) and (3,3,12). Shade the fundamental triangle and label its angles pi/p, pi/q, pi/r.
- F2: thin edges with depth, or stop the recursion at a fixed hyperbolic radius, so the boundary does not become a solid black ring.

**Avoid**
- F2: Cartesian axes and ticks on a disk-model or hyperboloid picture. Draw a frame only if it is a coordinate chart we discuss.
- F1: strong specular highlights on a surface whose colour carries data. Use diffuse lighting with a weak ambient term, so hue and lightness stay faithful to the colour map.

## 6. Girondo and Reyes (2019 preprint): hyperbolic polygons in black line art

E. Girondo, C. Reyes, "A brute force computer aided proof of an existence result about extremal hyperbolic surfaces", arXiv:1905.13297 (2019). Its subject and authors match E. Girondo, C. Reyes, "Multiple extremal disc-packings in compact hyperbolic surfaces", *Experimental Mathematics* 33(2) (2024) 276-300, DOI 10.1080/10586458.2022.2075491. Crossref lists no arXiv relation and no abstract, so we could not confirm that the preprint is that article. The notes below concern the arXiv version only.

**Figures looked at**
- Fig. 2: a tessellation by regular heptagons in the Poincaré disk, drawn in black. One edge e is shown in heavier weight, points A, B, C are labelled, and a thin chain of segments shows a construction.
- Fig. 7: a 14-gon fundamental region with a few adjacent tiles and three labelled points.

**What works and what does not**
- The drawing is pure black and white and fully greyscale-safe. It uses three line weights: the boundary circle, the tiling edges, and one emphasised edge, which is heavier. Points are filled dots with italic labels. Showing only a finite patch of the tiling, instead of recursing to the boundary, keeps the picture uncluttered.
- The figures are raster PNGs at about 1100 px. The outermost small polygons show jagged, hand-traced edges, and the line work looks soft at print size.

**Adopt**
- F2: a greyscale tiling hierarchy, with a thin boundary conic, medium tiling edges, and heavy emphasised mirrors or fundamental-domain edges. Draw a finite patch of tiles around the fundamental domain rather than recursing to the boundary.

**Avoid**
- F2 and all line art: raster export. Produce vector PDF, so arcs stay smooth at any zoom.

## 7. Balakrishnan, Ho, Kaplan, Spicer, Stein and Weigandt (2016): elliptic-curve statistics

J. S. Balakrishnan, W. Ho, N. Kaplan, S. Spicer, W. Stein, J. Weigandt, "Databases of elliptic curves ordered by height and distributions of Selmer groups and ranks", *LMS J. Comput. Math.* 19(A) (2016) 351-370, DOI 10.1112/S1461157016000152. arXiv:1602.01894.

**Figures looked at**
- Fig. 2: average rank against log10(naive height). A running average is drawn as a blue line, and averages over height windows as large green dots (full data) and red dots (samples).
- Fig. 6: average size of the 2-Selmer group, with the same encoding plus a purple horizontal line at the theoretical value 3.

**What works and what does not**
- These figures are the closest analogue to our F9(b): a cumulative statistic against log height, with the asymptotic prediction drawn as a reference line. Both the running statistic and the discrete window estimates are shown, which is honest about where the data are complete and where they are sampled.
- The visual execution is weak. There is a dense dotted minor grid over the whole panel, and the legend box covers data points. Red against green separates "full" from "sample", which fails for red-green colour blindness and in greyscale. The y-axis label is long, and the aspect ratio is very wide.

**Adopt**
- F9: show the cumulative count as a step or line and the fitted law as a thin reference curve of a different kind (dashed). Plot against log S when the law is in log S.
- F4: separate exhaustive data from sampled or extrapolated data by marker fill (filled against open), not by red against green.

**Avoid**
- All plots: full minor grids, and legend boxes placed over data. Put a legend outside the axes or in empty space, or label the curves directly.
- All plots: red-green as the only distinction.

## 8. Cotterill and Garay López (2022): real loci of plane curves

E. Cotterill, C. Garay López, "Real inflection points of real linear series on an elliptic curve", *Experimental Mathematics* 31(2) (2022) 506-517, DOI 10.1080/10586458.2019.1655815. arXiv:1804.06524.

**Figures looked at**
- Fig. 1: a 2x2 grid of panels, a) to d), showing real loci of plane curves P_{2k}=0 as thin blue curves in a square window. Fig. 2 is similar.

**What works and what does not**
- This is the only published real-locus figure we found close to F9(a). The real branches are clear and the shared window allows comparison. But the tick labels are tiny (unreadable at print width), there are no axis names (x, y), the curve equations appear only in the caption, and the singular points are not marked. Panel letters are italic below each panel. This is a reminder that plot-tool defaults at a 2x2 grid produce text that is far too small.

**Adopt**
- F9(a): use a square, equal-aspect window, so the shape of the real locus is not distorted. Label the axes x and y.

**Avoid**
- F9(a): tick labels below about 7 pt at final size. Leaving distinguished points unmarked: our rational points must be marked and the generator labelled.

## 9. Kalvin (2021, JGA): determinant over a one-parameter family of triangle envelopes

V. Kalvin, "Spectral determinant on Euclidean isosceles triangle envelopes", *J. Geom. Anal.* 31(12) (2021) 12347-12374, DOI 10.1007/s12220-021-00717-x. arXiv:2010.02209. The arXiv title is longer: "... of fixed area as a function of angles: absolute minimum and small-angle asymptotics".

**Figures looked at**
- Fig. 2: log det Delta_beta against the angle parameter beta for unit-area envelopes (envelopes are doubled triangles, the flat analogue of our pillows). Black curve with red point markers.
- Fig. 5: the same quantity at two areas, as two panels side by side. A dashed vertical line marks the critical point beta = -2/3 (equilateral).

**What works and what does not**
- This is the JGA paper closest in subject to ours (doubled triangles with cone points, a spectral invariant along a one-parameter family). The figures are Maple EPS output. The axes cross inside the frame, the tick labels are very small, and there are no axis labels at all: the variables are named only in the caption. The red markers (presumably sample points of the computation) are so dense that they merge into a band. The dashed vertical line at the distinguished parameter is the one good device.
- The layout shows the JGA house tolerance. Figures are small, inline and captioned in full, and the caption carries the explanation. That puts the burden on our captions, not on in-figure text.

**Adopt**
- F6: a thin dashed vertical line at a distinguished parameter value (a symmetric orbifold, an eigenvalue crossing), named in the caption.
- All figures: captions that say in full what is plotted, against what, and for which orbifold, so the figure does not need in-plot titles.

**Avoid**
- F6, F4: unlabelled axes, and markers so dense they merge. If a curve is sampled, either show a sparse subset of markers or none.

## 10. Hassannezhad, Métras and Perrin (2025, JGA): schematic surfaces

A. Hassannezhad, A. Métras, H. Perrin, "Geometric bounds for low Steklov eigenvalues of finite volume hyperbolic surfaces", *J. Geom. Anal.* 35(5) (2025) 158, DOI 10.1007/s12220-025-01990-w. arXiv:2408.04534.

**Figures looked at**
- Fig. 2: a doubled hyperbolic surface with its thin part shaded light grey. Collars are drawn as short cylinders with dashed back halves, and a dashed symmetry axis runs through the middle.
- Fig. 3 (right): a surface with two cusps drawn as long spikes, with dashed hidden curves.

**What works and what does not**
- This is the current JGA schematic style: thin black outlines, dashed hidden lines, light grey fill for the region of interest, and no colour. It is drawn as vector art (Inkscape pdf_tex), so the labels are set in the paper's own font. Cusps are drawn as spikes and collars as tubes, a conventional language that readers parse instantly.
- These are schematics, not data, and they make no claim to geometric accuracy.

**Adopt**
- F3, F7: vector line art with labels set in the document font (pdf_tex or TikZ, or matplotlib with the same serif font and sizes). Light grey fill for the highlighted set.
- F1: if a stylised render is too heavy for a panel, the fallback is this line-art language, with cone points drawn as sharp tips and the seam of the doubled triangle dashed.

**Avoid**
- F3, F7: colour where a grey fill and one accent suffice.

## 11. Métras and Tschanz (2024, Experimental Mathematics): eigenvalue curves along a parameter

A. Métras, L. Tschanz, "Critical lengths of Steklov eigenvalues of hypersurfaces of revolution in Euclidean space", *Experimental Mathematics* 34(4) (2024) 728-744, DOI 10.1080/10586458.2024.2410967. arXiv:2401.10743.

**Figures looked at**
- Fig. 1: two families of eigenvalue curves against the length L. The decreasing curves are blue dashed, the increasing ones green dashed, and the resulting sharp bound is a thick red solid curve. Two curves are labelled in place with their formula.
- Fig. 2: a schematic of the same picture with a large "?" over the region that is not covered.
- Fig. 13 (left panel): a matplotlib version with blue and green solid families and a thick red envelope. The title reads "Finite critical length", and in-plot italic text gives the critical length and the bound.

**What works and what does not**
- These are the closest analogue to our F6: many branches, crossings, and a distinguished envelope. A thick solid red line for the quantity of interest over thinner context curves works very well, and so does putting the two families in two styles. Fig. 1 labels one representative curve per family in place, instead of using a legend.
- Fig. 1 is a raster screenshot of a graphing tool. It has a grey sans-serif font, tick labels every 0.2 that crowd the x-axis, and no y label. Fig. 13 uses matplotlib defaults throughout: DejaVu sans font, a plot title, "Value of L" as the axis label, and in-figure italic annotations that duplicate the caption. The source bundle also holds an image that the paper does not use, and in it the bound is printed as raw TeX source ("B_6^80"). The panels the paper does use render it correctly. Leaks like this are easy to miss when a script exports dozens of panels.
- Blue and green are separable in colour but nearly equal in greyscale lightness.

**Adopt**
- F6: draw the tracked or extremal branch heavy and saturated, and the other branches thin, in one or two muted styles. Label one branch per family in place.

**Avoid**
- F6: plot titles inside the figure, words like "Value of L" on axes (use the symbol), and annotations that repeat the caption.
- All figures: unrendered TeX strings. Every panel exported by a script needs a visual check.
- F6: two families that differ only by blue and green hue.

## 12. Apel and Zilk (2024): convergence rates with slope triangles

T. Apel, P. Zilk, "Isogeometric analysis of the Laplace eigenvalue problem on circular sectors: regularity properties and graded meshes", *Comput. Math. Appl.* 175 (2024) 236-254, DOI 10.1016/j.camwa.2024.09.018. arXiv:2402.16589. The arXiv title adds "& variational crimes".

**Figures looked at**
- Fig. 9 (right panel): eigenvalue error |lambda - lambda_h| against the number of degrees of freedom on log-log axes, for six discretisations. Three colours give the degree, solid lines with squares are graded meshes, and dotted lines with triangles are uniform meshes. Four grey slope triangles sit at the lower right of the curves, with integer labels on their legs. We compiled the authors' pgfplots source to look at it.

**What works and what does not**
- This is the closest analogue to F8 and mostly a good model. The axes are log-log with decade ticks only (10^-11 to 10^-1, 10^2 to 10^4). Reference rates appear as small grey slope triangles near the end of each curve, not as full-length reference lines, so the data stay dominant. Style is doubly encoded (colour for one factor, line and marker for the other).
- An accuracy problem we checked in the source: the triangles are drawn with one slope in the plotted variable (ndof) but labelled with the rate in the mesh size h. For example, a triangle drawn with slope 2 per decade of ndof is labelled "4 : 1". A reader measuring the triangle gets a different number from the label. The legend box is also large and covers part of the plotting area.

**Adopt**
- F8: decade-only ticks on both axes. Reference slopes 1, 1/2, 1/3 as small grey triangles or short grey segments placed just beside the data, with the rate as a small label at the hypotenuse or in the caption. Double encoding (colour plus marker shape) for the series.

**Avoid**
- F8: any mismatch between the drawn slope and its label. The triangle must have exactly the stated slope in the plotted coordinates, and the caption should say in which variable.
- F8: legends inside the axes when they cover data.

## 13. Jin, Zhou and Zou (2022): log-log convergence without reference rates

B. Jin, Z. Zhou, J. Zou, "An analysis of stochastic variance reduced gradient for linear inverse problems", *Inverse Problems* 38(2) (2022) 025009, DOI 10.1088/1361-6420/ac4428. arXiv:2108.04429.

**Figures looked at**
- Fig. 1, panel (s-phillips, top noise level): bias and two variance terms against iteration k on log-log axes. MATLAB default colours (blue, orange, yellow), solid lines, legend lower left.

**What works and what does not**
- The decade ticks on both axes and the restrained axis range read well. But the plot has no reference slope at all. The paper's rate claims cannot be checked against the figure, which is exactly the gap F8 must close. The yellow line is weak on white and the three solid lines are separated by hue alone. The y label "e" is a single letter whose meaning is in the caption. That is acceptable in JGA style.

**Adopt**
- F8: keep the y range tight around the data (no empty decades).

**Avoid**
- F8: rate plots with no reference slope. Yellow lines on white. Lines separated only by hue.

## 14. Chen, Zhang and Zou (2022): error against a parameter on linear axes

Z. Chen, W. Zhang, J. Zou, "Stochastic convergence of regularized solutions and their finite element approximations to inverse source problems", *SIAM J. Numer. Anal.* 60(2) (2022) 751-780, DOI 10.1137/21M1409779. arXiv:2104.02352.

**Figures looked at**
- Fig. 2 (left): empirical error against k for lambda_n = 10^{-k}, on linear axes, with circles joined by lines.
- Fig. 4 (left): error against lambda_n^{1/2} on linear axes. Stars are joined by lines, the axes carry offset exponents (x10^-3 and x10^-4) at the corners, and a legend gives only sigma=0.01.

**What works and what does not**
- The claim of Fig. 4 is "linear dependence". It is shown by plotting against lambda^{1/2} on linear axes. The scatter at small values is then compressed into a corner, and the exponent offsets at the axis ends make the values hard to read. A log-log plot with a slope-1/2 reference against lambda would show the same claim more convincingly.

**Avoid**
- F8, F4: offset exponents ("x10^-4") at the axis corner. Use a log axis or put the scale in the axis label.
- F8: showing a power law on linear axes after transforming the abscissa. Use log-log and a reference slope.

---

## Synthesis for F1-F9

**The author's figure rules override this list.** No in-figure text is allowed except axis
titles, tick labels and panel letters. So everything below that puts words or symbols inside a
panel is replaced by a caption statement: direct curve labels (rule 2), rate labels on slope
marks (rule 4), names of marked points (rules 6, 7), angle and group labels on tilings
(rule 8). A curve is identified by its fixed hue and line style, defined once in the caption.
A colour bar counts as an axis (title and ticks only) and is allowed.

1. **Double-encode every series.** Pair a colour with a line style (solid, dashed, dotted, dash-dot) or with a marker shape (filled or open circle, square, triangle). The best figures we saw (Levitin-Strohmaier Fig. 8, Apel-Zilk Fig. 9) all do this. The family must stay readable in greyscale, and no two series may differ by hue alone, least of all red against green or blue against green. Applies to F4, F5, F6, F8, F9.
2. **Label curves directly, not with legends.** Put a short name next to each curve, in the curve's colour (Attar-Boettcher Fig. 5a, Métras-Tschanz Fig. 1). Use a legend only when there are more than about four series, and then outside the data region. Never use a legend for a single series. Applies to F5, F6, F9.
3. **Keep tick density low.** Use about four to six labelled ticks per axis. On log axes, label only powers of ten (10^-12, 10^-8, ...) with minor ticks unlabelled. Use no grid, or at most a very light major grid, and never a full dotted minor grid. Avoid offset exponents at the axis corners. Applies to all plots.
4. **Draw reference slopes as short grey triangles or segments next to the data.** They must not be full-length lines. The drawn slope must equal the stated rate in the plotted coordinates, which Apel-Zilk get wrong by an h against ndof factor. Put rates 1, 1/2, 1/3 as small labels on the triangle or in the caption, not as long in-figure text. Applies to F8, and to F5 for the expected decay rates.
5. **Emphasise the tracked object and mute the context.** The tracked branch, envelope or computed series is heavy (about 1.5 pt) and saturated. Context branches, asymptotic series or other families are thin (about 0.6 pt) and muted. Asymptotes and noise floors are dotted black horizontal lines. Applies to F5, F6.
6. **Show flow direction with markers.** In eigenvalue-flow and drift plots, give the direction of the parameter with a start marker (circle) and an end marker (square) on each branch, not with arrows. Draw thin dashed vertical lines at distinguished parameter values (symmetric orbifolds, crossings) and name them in the caption. Applies to F6, F7.
7. **Number-line schematics are one bare axis.** Draw a single horizontal axis with an arrowhead and the variable at the right end, and no frame, y-axis or grid. Mark elements as short ticks or dots with labels beside them, stacked for multiplicities. The reflected multiset sits on the negative half in a second style (open markers). Labels are horizontal and staggered rather than rotated (after KMP Fig. 2). Applies to F3, F7.
8. **Tilings use a greyscale line-weight hierarchy.** Use three weights: a thin boundary conic, medium tile edges, and heavy mirrors or fundamental-domain edges. The fundamental triangle gets a light tint, with its angles labelled pi/p, pi/q, pi/r. Draw a finite patch or thin edges with depth so the boundary does not saturate into a black ring, and use no Cartesian axes. Same panel size and same weights for (2,8,8) and (3,3,12), with the group label below each. Export as vector. Applies to F2.
9. **3D renders are diffuse-lit and colour-faithful.** Use diffuse lighting with weak ambient light and no strong specular highlight, because highlights distort a data colour map. Use a white background and no axes or box, with an optional sparse thin mesh. Use a perceptually uniform sequential map with a small colour bar, or state "darker = larger" in the caption. Mark cone points visibly and keep the seam of the doubled triangle visible. Say in the caption that the embedding is stylised and not isometric (after KMP Fig. 4). Applies to F1.
10. **Match the paper's typography.** Set all in-figure text in the document's serif math font at 8 to 9 pt at final printed size. Use symbols, not words, on axes (lambda_j, theta, t, A), and put no plot titles inside figures. Check every exported panel for unrendered TeX strings. Applies to all.
11. **Captions carry the explanation.** JGA practice, seen in Kalvin and in Hassannezhad-Métras-Perrin, is small inline figures with full captions. Each caption states what is plotted against what, for which orbifold, and what the reference marks mean, so the figure needs no explanatory text inside the axes. Applies to all.
12. **Separate exhaustive data from sampled or extrapolated data by fill, not hue.** Use filled markers for proven or exhaustive values and open markers for sampled or numerical ones (contrast Balakrishnan et al.'s red against green). Draw bound curves as step lines (drawstyle steps) distinct from the points. Applies to F4, F9.
13. **Use honest scales.** Use equal aspect for geometric objects (the real locus of the cubic, tilings, the plane of F7). Use log axes whenever a power law or exponential is the claim, rather than a transformed linear axis. Keep the axis range tight around the data. Applies to F2, F4, F7, F8, F9.
14. **Export everything as vector PDF.** Line art and plots go out as vector PDF. Only the shaded surface of F1 may be raster, embedded at 300 dpi or more at final size and with the vector annotations kept on top. Applies to all.

## Retrieval gaps

- **Hyperboloid model.** We found no research paper with a triangle-group tiling drawn on the hyperboloid model. Every tiling figure we found uses the Poincaré disk. F2 therefore has no direct precedent, and rule 8 is carried over from disk-model figures.
- **Real cubic with rational points.** We found no peer-reviewed figure showing the real locus of a plane cubic with its rational points marked. Cotterill and Garay López give real loci without marked points, and Balakrishnan et al. give count statistics. F9(a) is built from those two.
- **Heat trace against time.** We found no figure plotting heat-trace differences against time, with closed-geodesic terms rising out of a noise floor. Attar and Boettcher Fig. 5a, a partition function split into its identity and orbit-sum parts, is the nearest.
- **Girondo and Reyes.** The link between arXiv:1905.13297 and the Experimental Mathematics article could not be confirmed from Crossref metadata.
