# G5-bis audit: statements under review, group `pte-witnesses`

PTE witnesses: the explicit pairs of section 5, the 61 pencil witnesses, the T_3 search claim

Every result below is copied verbatim, by line range, from its source file (`review/audit-2/build_statements.py`
asserts the anchors and that no proof text is included). Items marked COMPOSED combine verbatim excerpts with
connective text in [square brackets]. **Proofs, scripts and data of the sessions that produced these results are
deliberately withheld.** You must not open any file of `theory/pte/`, `theory/revision/`, `theory/signatures/`
(other than where stated below), `review/referee-sim/` or `paper/` (the manuscript contains proofs of some of these
results). If you do open one by accident, say so in your REVIEW.md under 'contamination'.



## Context files you may read (previously audited statements, no proofs)

- review/audit/statements/signatures.md  (definitions DF.1: signature and heat coefficients; Lemma 2, 4, Theorem S)
- review/audit/statements/audibility.md  (Theorem A, Theorem C(3): what 'integer sharpness' means; items AU.1)

## External inputs

- Heat coefficients: use the definition in signatures.md DF.1 with the cone polynomials of Proposition heatinput in trace-formula.md (b_l(m) = (-1)^l p_l(m)/m, p_l from the closed form), or re-derive them from Ucar (arXiv:1711.03405, (4.25),(4.33)). Compute 'the number of shared coefficients' from the coefficients themselves, not from the P_j criterion alone, and also check it against the criterion.
- Borwein-Ingalls/BLP/Chen/CMSV solutions are inputs only as numbers: re-verify every such number exactly before using it. Their provenance belongs to the literature group.

## Fetched sources

Texts fetched headlessly by `review/audit-2/fetch_sources.sh` are in `review/audit-2/sources/` (not committed).
Never quote a source from memory: quote the fetched text, with page or section. An unreachable source is an
instrument gap, to be logged, not a confirmation.


## Group: pte-witnesses

### PW.0. Headline table (proof.md section 0, items 5 and 6)

Source: `theory/pte/proof.md` lines 32-47 (verbatim).

````
5. **Explicit witnesses (§5).** Pairs sharing exactly $L$ coefficients, verified with the actual
   cone coefficients:

   | $L$ | least area found, any pair: Area$/2\pi$ | genus pair: $\lvert U^*\rvert+\lvert V^*\rvert$ | genus 0, cone counts $n$ vs $n'$ | Thue–Morse bound on Area$/2\pi$ |
   |---|---|---|---|---|
   | 2 | $1/4$ | 6 | 3 vs 4 | 3 |
   | 3 | $22/15$ | 10 | 7 vs 8 | 15 |
   | 4 | $\approx5.000$ | 16 | 11 vs 12 | 63 |
   | 5 | $\approx7.000$ | 20 | 22 vs 23 | 255 |
   | 6 | $\approx10.000$ | 26 | 29 vs 30 | 1023 |
   | 7 | $\approx18.000$ | 40 | 35 vs 36 | 4095 |

6. **$T_3$ (§6).** $T_3\in\{8,10\}$ is not decided. An exhaustive exact search excludes every
   size-8 genus collision whose 5-element side, made primitive, has entries $\le220$. The
   collision must have shape $(3,5)$ (Theorem 2.1). Real solutions of that shape exist in
   abundance, so the obstruction, if there is one, is arithmetic.
````

### PW.1. Example (Small pairs) and Remark (first open case), as in statements.tex

Source: `theory/pte/statements.tex` lines 101-120; `theory/pte/statements.tex` lines 122-127 (verbatim).

````
\begin{example}[Small pairs]\label{ex:ptepairs}
The following pairs share exactly $L$ heat coefficients (exact computation with the cone
coefficients):
\begin{itemize}
\item $L=3$, same genus and cone count: $(0;3,10,15,30)$ and $(0;4,5,21,28)$, of area
  $2\pi\cdot\frac{22}{15}$. Previously the smallest area known to share three coefficients was
  $2\pi\cdot\frac{14}5$, for $(1;15,15,15)$ and $(0;3,3,5,7,7,21)$.
\item $L=3$, genus $0$ with $7$ and $8$ cone points: $(0;4,4,5,5,6,12,12)$ and
  $(0;2,2,2,3,10,10,10,10)$, obtained from $[1,5,5]=[2,3,6]$ \cite{chen2025survey} by the doubling
  above. This replaces $103$ vs $104$.
\item $L=4,5,6,7$: genus-$0$ pairs with equal cone counts and area
  $<2\pi\cdot5,\,7,\,10,\,18$. They come from pairs of odd ideal symmetric solutions of sizes $7$
  and $9$ \cite{borweiningalls1994,blp2003}, from equal sums of odd powers
  \cite{chen2025survey}, and from the size-$12$ ideal solution \cite{cmsv2024}. The
  Prouhet--Thue--Morse pairs of Theorem~\ref{thm:signonuniform} need area up to
  $2\pi(4^{L-1}-1)$.
\item Genus $1$ versus genus $0$ sharing $L=4,5,6,7$ coefficients: configurations of size
  $16,20,26,40$, against $2^{2L-1}=128,512,2048,8192$ for Thue--Morse.
\end{itemize}
\end{example}

\begin{remark}[The first open case]\label{rem:ptet3}
By Theorem~\ref{thm:ptedescartes}, a genus collision sharing three coefficients with
$|U^*|+|V^*|=8$ must have shape $(3,5)$. An exhaustive exact search excludes all such collisions
whose five-element side, made primitive, has entries $\le220$. Real solutions of this shape
exist. So whether the least size is $8$ or $10$ remains open.
\end{remark}
````

### PW.2. Improved lower bounds on f in the covered range

Source: `theory/pte/proof.md` lines 457-470 (verbatim).

````
**Improved lower bounds on $f$ in the covered range.** Let $A_L$ be the least area in the
tables above among pairs sharing $L$ coefficients. Then $f(A)\ge L+1$ for $A\ge A_L$:

| $f(A)\ge$ | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|
| for $A/2\pi\ge$ (new) | $1/4$ | $22/15$ | $5.000$ | $7.000$ | $10.000$ | $18.000$ |
| for $A/2\pi\ge$ ([Sig] N1) | 3 | 15 | 63 | 255 | 1023 | 4095 |

The exact values of $A_L$ are in `data/witnesses.json`. The $\approx$ values lie just below
the integers shown, e.g. $A_4/2\pi=4.99999\ldots$, so "$\ge5.000$" is a safe rounding up.

Over this range the best pairs have Area$/2\pi\approx T/2-2$ with $T\le4L-2$ for $L\le5$. So
for $A/2\pi\le18$, $f$ grows at least linearly: $f(A)\ge L+1$ at
$A/2\pi\approx2L-3$ for $L\le5$.
````

### PW.3. Integer sharpness witnesses for Theorem A at n=4, and the n=5 claim

Source: `theory/pte/proof.md` lines 253-265 (verbatim).

````
*Instances.* For $m=4$ the hypothesis says that $A,B$ have $e_1=0$ and equal $e_3,e_4$.
`pencil_search.py` finds 25 distinct configurations from 4-sets with entries $\le130$, and 61
with entries $\le220$ (`data/pencil_log.txt`). These include 60 integer sharpness witnesses
for Theorem A at $n=4$ beyond the one recorded in `theory/audibility`. The smallest is
$A=\{-30,-3,5,28\}$, $B=\{-21,-4,10,15\}$, which gives
$\{3,10,15,30\}\sim\{4,5,21,28\}$. That is the $n=4$ witness of `theory/audibility/proof.md`
Theorem C(3) and Chen's type $(-1,1,3)$ entry A.685. So Theorem C(3) at $n=4$ is a pencil
phenomenon.

For $m=5$ the hypothesis asks for two odd symmetric 5-sets with equal $e_4,e_5$. Such a pair
would give a balanced 4-configuration of size 10, i.e. the integer sharpness of Theorem A at
$n=5$, which is open in `theory/audibility`. Among all 1,592 primitive 5-sets with entries
$\le200$, no such pair exists.
````

### PW.4. The 18 claimed pairs (generated; recipes and Z omitted)

Source: generated (witnesses) (verbatim).

Each entry is a claim: the two orbifolds below are closed orientable hyperbolic 2-orbifolds of the signature shown (cone orders; 'g' genus), they have equal area, distinct signatures, and they share EXACTLY L heat coefficients (the first L coefficients agree, the (L+1)-st differs). 'T' is the claimed size of the cancelled configuration Z = U* + (-V*), 'cone counts' the numbers of cone points (1s removed). The claimed exact area/2pi is given.

**W00** kind=genus, L=2, claimed shares exactly 2, T=6, iota=2, cone counts 4 vs 1, Area/2pi = 14/15
- O  = (g=0; 3, 3, 5, 5)
- O' = (g=1; 15)

**W01** kind=genus, L=3, claimed shares exactly 3, T=10, iota=2, cone counts 6 vs 3, Area/2pi = 14/5
- O  = (g=0; 3, 3, 5, 7, 7, 21)
- O' = (g=1; 15, 15, 15)

**W02** kind=genus, L=4, claimed shares exactly 4, T=16, iota=2, cone counts 9 vs 7, Area/2pi = 41149074301/5878522650
- O  = (g=0; 34986, 38775, 58310, 116325, 128282, 271425, 271425, 454818, 524790)
- O' = (g=1; 12925, 168025, 219725, 268226, 297275, 384846, 548114)

**W03** kind=genus, L=5, claimed shares exactly 5, T=20, iota=2, cone counts 11 vs 9, Area/2pi = 112658971081054/12517666291845
- O  = (g=0; 1517814, 2063997, 2522663, 7589070, 9861319, 10319985, 12613315, 19731582, 59194746, 77408514, 89551026)
- O' = (g=1; 687999, 4357327, 8485321, 11695983, 12154649, 34909722, 50087862, 83479770, 86515398)

**W04** kind=genus, L=6, claimed shares exactly 6, T=26, iota=2, cone counts 14 vs 12, Area/2pi = 8011672951610749084518529918806713747318107765849227714286789/667639412634229090376544159900603145300498646924203622400000
- O  = (g=0; 4093411365093597322848394806575, 7271375040829745152760217600000, 9824187276224633574836147535780, 9987923730828377467750083328043, 14793487152032929793546649600000, 48392254582073821189059379200000, 52886874837009277411201260900949, 61237434021800215949811986306362, 61932056382239553542474956800000, 77283606572967117455377693948136, 77979228886139680776152678400000, 78480703026886559752205107200000, 84160537666324360957762997223182, 90218786486662884995578621536913)
- O' = (g=1; 1755159492614076416183500800000, 22817073403982993410385510400000, 33074763829956266368615030037126, 37986857468068583156033103805016, 43377513174605031428535091200000, 67448271930455222279051673600000, 70079202570402386167164519088564, 72463013337924012039575961600000, 76137451390740910204980143402295, 80988073730620954632467251200000, 81049545028853226992398217170185, 91364941668889092245976172082754)

**W05** kind=genus, L=7, claimed shares exactly 7, T=40, iota=2, cone counts 21 vs 19, Area/2pi = 159016325127586219276587050363723886153380991692916838678380792473971519/8369280269872958909294055282301257170650883098593549936154305804369920
- O  = (g=0; 495461702484924819341859189302493184, 683624372840614274768382863229231445, 771998466662557276648943387982954496, 818087927358829352866790754429698048, 1093798996544982839629412581166770312, 1716832410936134839114814400141197312, 1855100793024951067768356499481427968, 2292950669639535791837906480725491712, 2734497491362457099073531452916925780, 3053426771128025049432388027096760320, 3237784613913113354303777492883734528, 3537366108438881849719785374787567616, 3790858142268378268917945890244657152, 6699518853838019892730152059646468161, 9160566596064231281896330367271701363, 12031788961994811235923538392834473432, 12852138209403548365645597828709551166, 16270260073606619739487512144855708391, 21055630683490919662866192187460328506, 22833054052876516777263987631856330263, 24337027673125868181754429930960639442)
- O' = (g=1; 195880207959156323925851307398660096, 1094624691536461810173874953110159360, 1117669421884597848282798636333531136, 1394206186062230305589882835013992448, 1670742950239862762896967033694453760, 2615576894513440325362838045852696576, 2915158389039208820778845927756529664, 3168650422868705239977006443213619200, 3675634490527698078373327474127798272, 3721723951223970154591174840574541824, 4648645735316177068425003469958773826, 8066767599519248442266917786104931051, 8476942223223617007127947504042469918, 10117640718041091266572066375792625386, 13672487456812285495367657264584628900, 16953884446447234014255895008084939836, 20235281436082182533144132751585250772, 23653403300285253906986047067731407997, 23926853049421499616893400213023100575)

**W06** kind=balanced, L=2, claimed shares exactly 2, T=6, iota=0, cone counts 3 vs 3, Area/2pi = 1/4
- O  = (g=0; 3, 3, 12)
- O' = (g=0; 2, 8, 8)

**W07** kind=balanced, L=3, claimed shares exactly 3, T=8, iota=0, cone counts 4 vs 4, Area/2pi = 22/15
- O  = (g=0; 3, 10, 15, 30)
- O' = (g=0; 4, 5, 21, 28)

**W08** kind=balanced, L=4, claimed shares exactly 4, T=14, iota=0, cone counts 7 vs 7, Area/2pi = 118766555393933327671589/23753311078941951481650
- O  = (g=0; 74493387367, 138344862253, 217482072530, 404392674278, 532095624050, 600937305675, 703955129505)
- O' = (g=0; 74401761655, 131633886005, 255405899544, 351183111873, 542737536531, 629553367850, 686785492200)

**W09** kind=balanced, L=5, claimed shares exactly 5, T=18, iota=0, cone counts 9 vs 9, Area/2pi = 812564706402847786089918000749235251/116080672343263975087481791511661200
- O  = (g=0; 5806604053259408, 20770022346082906, 35431214590376722, 36291275332871300, 50092406834670538, 59866534997533082, 95808966878780232, 107422174985299048, 126293638158392124)
- O' = (g=0; 7941479132325817, 9774128162862544, 42150927702344721, 45727006919417838, 45816225763418175, 60477418007711991, 86373235292233694, 116857906571845586, 122664510625104994)

**W10** kind=balanced, L=6, claimed shares exactly 6, T=24, iota=0, cone counts 12 vs 12, Area/2pi = 12395899856021215350087167375045579535671/1239589985602121535014046594388561899975
- O  = (g=0; 71623872894939389150, 129265225362823216755, 138389829506081326173, 430377162090340827549, 436460231519179567161, 507595273125005236150, 563648738868870845050, 612869244955503015909, 701073751673664740283, 1061901767703231813050, 1080586256284520349350, 1267431142097405712350)
- O' = (g=0; 65392996360016450829, 115221012917945973850, 244843544510759269383, 330006516514501623951, 370575690195555969950, 509457064665244442505, 594620036668986797073, 688211996077461087050, 704115286388084110089, 968479324796789131550, 1155324210609674494550, 1254974816376546688150)

**W11** kind=balanced, L=7, claimed shares exactly 7, T=40, iota=0, cone counts 20 vs 20, Area/2pi = 14301019323811636282516882693657383028577480873602071293040986507111198588933404629842516/794501073545090904584271260758743501587638079375203534302390704062617122289416027087675
- O  = (g=0; 595958629909279070099829518275115563729823, 1030537353727106401413686917679685652027815, 1605720993016654160342256360105556713624735, 1701584932898245453497017933843201890557555, 3570931760589275670014868621727282840747545, 3858523580234049549479153342940218371546005, 4769231009109166834449388293447847552407795, 6350986017155423171502954260118992971799325, 6734441776681788344122000555069573679530605, 7236640506041245851212215579054974702433565, 7357557385912131749627950784364267329593935, 7884809055260883861979139439921315802724445, 9620475025678362131611533652155436957352857, 13877322382173212632324601639834833841137307, 14217870170692800672381647078849185591840063, 21369373729604149513579601298150572356597939, 25626221086099000014292669285829969240382389, 32607450750750554835462100785624180129788887, 34821011376127877095832896139217466509356801, 36694024212985611316146646053796401138221959)
- O' = (g=0; 407421744496762995907736688384992001964485, 2276768572187793212425587376269072952154475, 2324700542128588859002968163137895540620885, 2899884181418136617931537605563766602217805, 2979793149546395350499147591375577818649115, 3475067820707684376860107047989637663814725, 3660888726585571430613238469404281320054627, 5440278588280305886532719309611363790937535, 6063394197510649292038669538906057441000865, 6590645866859401404389858194463105914131375, 7645149205556905629092235505577202860392395, 7741013145438496922246997079314848037325215, 10642118391237126251782669969198492209461125, 12855679016614448512153465322791778589029039, 16942252478849504992838010590963999597462111, 18985539209967033233180283225050110101678647, 26988412240177352174520851041887376243193413, 31585807385191790715290964468581124877680619, 35842654741686641216004032456260521761465069, 36183202530206229256061077895274873512167825)

**W12** kind=cone, L=2, claimed shares exactly 2, T=8, iota=0, cone counts 4 vs 3, Area/2pi = 2/5
- O  = (g=0; 2, 2, 2, 10)
- O' = (g=0; 5, 5, 5)

**W13** kind=cone, L=3, claimed shares exactly 3, T=16, iota=0, cone counts 7 vs 8, Area/2pi = 113/30
- O  = (g=0; 4, 4, 5, 5, 6, 12, 12)
- O' = (g=0; 2, 2, 2, 3, 10, 10, 10, 10)

**W14** kind=cone, L=4, claimed shares exactly 4, T=24, iota=0, cone counts 12 vs 11, Area/2pi = 2651846/320229
- O  = (g=0; 2, 2, 3, 9, 21, 21, 26, 26, 34, 34, 46, 46)
- O' = (g=0; 6, 6, 13, 17, 18, 18, 23, 42, 42, 42, 42)

**W15** kind=cone, L=5, claimed shares exactly 5, T=46, iota=0, cone counts 23 vs 22, Area/2pi = 564239482/30342025
- O  = (g=0; 2, 2, 2, 3, 10, 12, 20, 20, 21, 31, 40, 48, 48, 49, 50, 56, 56, 84, 84, 94, 94, 102, 102)
- O' = (g=0; 4, 4, 5, 6, 6, 24, 24, 24, 28, 42, 42, 42, 47, 51, 62, 62, 80, 80, 98, 98, 100, 100)

**W16** kind=cone, L=6, claimed shares exactly 6, T=60, iota=0, cone counts 30 vs 29, Area/2pi = 49020849382437764968683088/1845726112877621686996185
- O  = (g=0; 2, 2, 6, 7, 26, 26, 134, 183, 243, 252, 252, 385, 428, 428, 430, 430, 445, 494, 621, 622, 826, 826, 828, 828, 1004, 1004, 1230, 1230, 1254, 1254)
- O' = (g=0; 12, 12, 13, 14, 14, 126, 214, 215, 268, 268, 366, 366, 413, 414, 486, 486, 502, 615, 627, 770, 770, 890, 890, 988, 988, 1242, 1242, 1244, 1244)

**W17** kind=cone, L=7, claimed shares exactly 7, T=72, iota=0, cone counts 36 vs 35, Area/2pi = 70773805781898091109456/2190539016013095022275
- O  = (g=0; 2, 2, 4, 6, 24, 24, 31, 50, 50, 58, 105, 117, 132, 132, 182, 182, 187, 199, 246, 260, 260, 273, 298, 300, 348, 348, 426, 426, 476, 476, 558, 558, 584, 584, 606, 606)
- O' = (g=0; 8, 8, 12, 12, 12, 25, 62, 62, 66, 91, 116, 116, 130, 174, 210, 210, 213, 234, 234, 238, 279, 292, 303, 374, 374, 398, 398, 492, 492, 546, 546, 596, 596, 600, 600)


### PW.5. The 61 claimed pencil configurations (generated)

Source: generated (pencil61) (verbatim).

Claim (n = 4 integer sharpness of Theorem A; see Theorem C(3) in audibility.md AU.1). Below are 61 integer 8-element multisets Z. The claim is that each Z has: no pair {z,-z}; sum z^j = 0 for j = 1, 3 and j = -1; exactly four positive and four negative entries (imbalance 0); so m = positive part and m' = (-negative part) are two DISTINCT 4-multisets of positive integers with equal R = sum 1/m_i, P_1 and P_3, i.e. two orbifolds of genus 0 with four cone points sharing I_3 = (R, P_1, P_3); the 61 are pairwise distinct modulo Z -> lambda Z (lambda rational) and Z -> -Z (which swaps m, m'); and they are ALL the configurations produced as follows: A, B primitive integer 4-sets {a,b,c,-(a+b+c)} with all entries of absolute value <= 220, A and B with equal e_3^4/e_4^3 (e_k elementary symmetric), B scaled by the rational lambda with e_3(lambda B) = e_3(A), e_4(lambda B) = e_4(A), lambda B != A as multisets, then Z = A + (-lambda B) after cancelling, scaled to primitive integers. (The first claim is checkable on the list; the 'all' claim needs your own enumeration.)

```
[-28, -21, -5, -4, 3, 10, 15, 30]
[-72, -56, -10, -9, 7, 15, 50, 75]
[-75, -50, -15, -12, 10, 21, 44, 77]
[-72, -56, -12, -9, 7, 21, 44, 77]
[-77, -44, -21, -13, 12, 26, 39, 78]
[-75, -50, -15, -13, 10, 26, 39, 78]
[-72, -56, -13, -9, 7, 26, 39, 78]
[-77, -63, -18, -14, 11, 33, 44, 84]
[-91, -78, -14, -7, 6, 22, 63, 99]
[-99, -63, -22, -15, 14, 25, 60, 100]
[-91, -78, -15, -7, 6, 25, 60, 100]
[-100, -60, -25, -17, 15, 34, 51, 102]
[-99, -63, -22, -17, 14, 34, 51, 102]
[-91, -78, -17, -7, 6, 34, 51, 102]
[-130, -117, -65, -45, 42, 84, 91, 140]
[-140, -105, -20, -18, 15, 26, 99, 143]
[-126, -117, -39, -26, 22, 66, 77, 143]
[-143, -99, -26, -25, 18, 50, 75, 150]
[-153, -136, -11, -9, 8, 13, 132, 156]
[-143, -130, -22, -13, 10, 55, 78, 165]
[-156, -132, -29, -13, 11, 58, 87, 174]
[-153, -136, -29, -9, 8, 58, 87, 174]
[-174, -87, -58, -30, 29, 70, 75, 175]
[-156, -132, -30, -13, 11, 70, 75, 175]
[-153, -136, -30, -9, 8, 70, 75, 175]
[-187, -102, -28, -21, 16, 64, 66, 192]
[-182, -140, -42, -13, 12, 65, 105, 195]
[-175, -165, -33, -11, 10, 50, 126, 198]
[-195, -130, -39, -35, 26, 84, 85, 204]
[-209, -152, -33, -25, 24, 35, 150, 210]
[-210, -150, -36, -35, 25, 68, 117, 221]
[-209, -152, -36, -33, 24, 68, 117, 221]
[-221, -117, -68, -37, 36, 74, 111, 222]
[-210, -150, -37, -35, 25, 74, 111, 222]
[-209, -152, -37, -33, 24, 74, 111, 222]
[-208, -156, -42, -26, 21, 91, 96, 224]
[-198, -189, -54, -32, 28, 77, 144, 224]
[-220, -120, -8, -4, 3, 25, 99, 225]
[-224, -144, -21, -18, 14, 32, 133, 228]
[-225, -180, -33, -25, 20, 51, 154, 238]
[-238, -154, -51, -41, 33, 82, 123, 246]
[-225, -180, -41, -25, 20, 82, 123, 246]
[-246, -123, -82, -42, 41, 91, 114, 247]
[-238, -154, -51, -42, 33, 91, 114, 247]
[-225, -180, -42, -25, 20, 91, 114, 247]
[-231, -210, -34, -11, 10, 51, 170, 255]
[-255, -170, -51, -39, 34, 65, 156, 260]
[-231, -210, -39, -11, 10, 65, 156, 260]
[-260, -156, -65, -45, 39, 95, 126, 266]
[-255, -170, -51, -45, 34, 95, 126, 266]
[-231, -210, -45, -11, 10, 95, 126, 266]
[-270, -108, -27, -15, 12, 65, 70, 273]
[-304, -208, -57, -50, 39, 90, 175, 315]
[-315, -175, -90, -53, 50, 106, 159, 318]
[-304, -208, -57, -53, 39, 106, 159, 318]
[-340, -204, -85, -56, 51, 105, 184, 345]
[-342, -176, -22, -19, 12, 96, 99, 352]
[-366, -183, -122, -63, 61, 144, 161, 368]
[-390, -195, -130, -66, 65, 138, 187, 391]
[-385, -220, -105, -66, 60, 138, 187, 391]
[-438, -219, -146, -75, 73, 165, 200, 440]
```

Further claim: with m = 5 (odd symmetric 5-sets {e_1 = e_3 = 0}, primitive, entries <= 200; there are 1,592 of them), no two have equal e_4^5/e_5^4 giving a pencil pair, i.e. no integer sharpness witness of Theorem A at n = 5 arises this way.
