# Palette candidates (gate G6)

`contact-sheet.pdf` and `contact-sheet.png` show the candidates **A, B, C, D from top to
bottom**. Each candidate is one block of four rows: normal vision, deuteranopia, protanopia,
greyscale (CIE L*). The same blocks are in `candidate-<K>-<name>.png`. Each row has three test
panels built from committed data:

- (a) O(3,3,12), stylised, coloured by 4πt 𝔥_t(x,x) at t = 0.02. The scale is log, shared with
  O(2,8,8), and darker means larger.
- (b) (Z(t) − c₁/t − c₂)/t for O(2,8,8) (dark hue) and O(3,3,12) (light hue). Both tend to c₃
  (−1601/480 and −867/160).
- (c) the least-order strata p = 2..8 in the (S, R) plane, with lower and upper endpoint curves.
  The split disc at (18, 3/4) is the collision (2,8,8) ~ (3,3,12); open circles are the first
  collisions of the other adjacent pairs.

Rebuild with `python3 figures/src/contact_sheet.py` (Blender, about 10 s per render).

| | name | sequential map (heat, density) | (2,8,8) hue | (3,3,12) hue | L* of pair | ΔE of pair: normal / deutan / protan / tritan |
|---|---|---|---|---|---|---|
| A | batlow | Crameri batlow, reversed | batlow 0.20 `#185562` | batlow 0.70 `#e09651` | 33 / 68 | 78 / 75 / 63 / 77 |
| B | lajolla-oslo | Crameri lajolla, reversed | oslo 0.38 `#27588e` | lajolla 0.70 `#e99d53` | 37 / 71 | 93 / 96 / 85 / 78 |
| C | lipari | Crameri lipari, reversed | lipari 0.20 `#3c5478` | lipari 0.66 `#e37861` | 35 / 62 | 72 / 68 / 51 / 84 |
| D | viridis | viridis, reversed | viridis 0.18 `#433e85` | viridis 0.72 `#4ec36b` | 30 / 71 | 112 / 81 / 92 / 52 |
| **E** | **batlow-lajolla (chosen)** | Crameri lajolla, reversed (B's map) | batlow 0.20 `#185562` | batlow 0.70 `#e09651` | 33 / 68 | 78 / 75 / 63 / 77 |

All four sequential maps have monotone L* from end to end.

## Observations

- **A, batlow.** The low end of the map, which covers almost the whole pillow, is pink. It
  dominates panel (a), and the halos read as green-brown. The strata in (c) mix green, ochre
  and pink, which looks busy.
- **B, lajolla with an oslo blue.** The body is pale cream and the halos run from orange-red to
  dark brown, which reads as heat. The hue pair is blue against orange, and it has the largest
  separation under every dichromat simulation. The strata in (c) run from pale yellow to dark
  brown and stay ordered in greyscale. One weakness: the (3,3,12) orange sits inside the map's
  range, so in F7 the pillow marker sits close in hue to the middle strata. Its black outline
  and split fill keep it distinct.
- **C, lipari.** Calm, with a cream body, red halos and a navy and coral pair. Its protanopia
  separation of the pair (ΔE 51) is the weakest of the four. Its coral is also close to the
  map's middle.
- **D, viridis.** The body is a saturated yellow that competes with the halos. The green
  (3,3,12) hue is light on white (L* 71). Tritanopia separation is the weakest (ΔE 52).

## Recommendation: **B (lajolla-oslo)**

B is the most robust for colour-blind readers. It is legible in greyscale, the cone-point
halos stay visible in all four views, and the heat-like ramp fits a figure set about heat
diffusion. C is a close second if a cooler, quieter look is preferred.

To choose, set `"chosen"` in `figures/style/palette.json`, or ask for changes: different
sample positions, a different map, or a different pair.

## Decision (2026-10-05): **E**

The author chose a hybrid, E. It takes A's pillow pair (batlow 0.20 and 0.70) and B's sequential
map (lajolla, reversed). E has no block on the contact sheet. Its two parts are each shown there:
the pair in block A, the map in block B.
