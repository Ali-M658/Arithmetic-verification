# SOURCES: third-party files fetched for the JGA manuscript

Every file below was retrieved headlessly (curl with a desktop user agent, or Python `urllib`)
on 2026-10-05. Nothing was written from memory. `link.springer.com` blocks headless requests, so
Springer pages were taken from springernature.com or from the Internet Archive. Fetched files
are kept under `paper/jga/fetched/` (git-ignored, re-created by the commands below), except the
two template files that the build needs, which are committed.

## Template and journal policy

| file | source URL | SHA-256 |
|---|---|---|
| `fetched/sn-template-v12.zip` (Springer Nature LaTeX template, "December 2024 version", v3.1) | https://cms-resources.apps.public.k8s.springernature.io/springer-cms/rest/v1/content/18782940/data/v12 (linked from https://www.springernature.com/gp/authors/campaigns/latex-author-support/see-where-our-services-will-take-you/18782940) | `812e76dcaa9c28dc1bff1fb6065d51729b67d4ea140552a05088317414a3ecae` |
| `sn-jnl.cls` (committed; extracted unchanged from the zip) | as above, `sn-article-template/sn-jnl.cls` | `36d0c3273a59d48dc6a9c7b080dfa1ec50dc10229d8751568d1f2e490ffa5ecc` |
| `sn-mathphys-num.bst` (committed; extracted unchanged from the zip) | as above, `sn-article-template/bst/sn-mathphys-num.bst` | `b3a7c7fbcc1e7f9619de634fcea2f5bb7a245818a5942bc576e40ea001633332` |
| `fetched/latex-support.html` | https://www.springernature.com/gp/authors/campaigns/latex-author-support | `9f8abd88750155289b96df8c8a12775428751438684ccc2b4a99b26e5b24a324` |
| `fetched/see-where.html` | https://www.springernature.com/gp/authors/campaigns/latex-author-support/see-where-our-services-will-take-you/18782940 | `43b6745a3e02d2ac554c266fdd933b58f0d6c66ae2e33772293083e5d3cb7b93` |
| `fetched/jga-guidelines.html` (JGA submission guidelines) | https://web.archive.org/web/20251204070959/https://link.springer.com/journal/12220/submission-guidelines | `5383097d394a25e0f55ef4075ccef562756deebea93947874b4f8722f8dac3be` |
| `fetched/sn-editorial-policies.html` | https://www.springernature.com/gp/policies/editorial-policies | `b166c2e35780ecc075fa0e4f9e9b6597ec83f9651288e09a1ca13359725021c4` |
| `fetched/sn-ai-manuscript-preparation.html` (Springer Nature, "AI use in manuscript preparation") | https://www.springernature.com/gp/policies/editorial-policies/ai-manuscript-preparation | `f3e0a593f3136a8ac79feb037426356ffed19fc598a7e3d1dbd6ca614cda7c67` |
| `fetched/springer-journal-policies.html` (Springer journal policies, section "Artificial intelligence (AI)") | https://web.archive.org/web/20260919214816/https://link.springer.com/brands/springer/journal-policies? | `a49c07e0a849eeb6ab531922b0b00904826dc118e23c03e1ef7d4cd4834705d5` |
| `fetched/MSC_2020.csv` (MSC 2020, all codes) | https://msc2020.org/MSC_2020.csv | `f7c889354c202551fe01f89bad2ae95ccadec4c57ac1f6f9de38bbd658d3c78c` |

The template class loads no font package (its `\RequirePackage[T1]{fontenc}` line is commented
out), and its user manual (section 3.2, "Fonts") states that text and mathematics are set in
Computer Modern. The manuscript loads no font package either, so it matches the figures.

The MSC codes used in the 30-35 page revision (58J53 primary; 58J50, 35K08, 57R18, 30F35, 11D72,
11G05) were each found in `MSC_2020.csv` (re-fetched 2026-10-06, same SHA-256): Isospectrality;
Spectral problems, spectral geometry, scattering theory on manifolds; Heat kernel; Topology and
geometry of orbifolds; Fuchsian groups and automorphic functions; Diophantine equations in many
variables; Elliptic curves over global fields. 11D68 and 11D45 were dropped with old Section 8.

## Texts read to check citations and quotations

| file | source URL | SHA-256 | used for |
|---|---|---|---|
| `fetched/dr_1103.4372v2.pdf` | https://arxiv.org/pdf/1103.4372v2 | `3dbd2ae196e77be38f715837a905cbaafaf1a57c39a7070f93cb2d701edc599b` | the quotation in Section 1.1 (Section 3, p. 8) |
| `fetched/dggw_0805.3148v1.pdf` | https://arxiv.org/pdf/0805.3148v1 | `bda49c2124b25df3873f7d0fff5b2bc3d9ac683340646d816d7414065e89c892` | Thm 4.8, Def. 4.7, Thms 5.14-5.15, Rem. 5.16 (quotation), Prop. 5.22 |
| `fetched/ucar_1711.03405v1.pdf` | https://arxiv.org/pdf/1711.03405v1 | `b6da48a7b8add02f42b2e95dcf5077eb27aed6c133acb13f7e26e95f390c0a74` | (4.25), (4.33)-(4.35), Thm 4.20, Cors 4.21, 4.23; the author's name "Eren U\c{c}ar" from the title page |
| `fetched/pari-old.html` | https://pari.math.u-bordeaux.fr/pub/pari/OLD/2.17/ | `1c1451d303f69f9edc6bc7bcdfd3c40d22549caf8418de0b824f11ea31d3c21e` | release date of PARI/GP 2.17.2 |
| `fetched/bib/ostrowski1940_reprint.json` | https://doi.org/10.1007/978-3-0348-9355-8_50 (CSL-JSON) | `37536ab30d79caaa5b241f7bb09018981a54e4636758ecf0d4b0ce54b37c1326` | capitalisation of "Graeffe" and "Laurent" in the title of `ostrowski1940` |
| `fetched/berardwebb/zb_berard_webb.json` | https://api.zbmath.org/v1/document/_search?search_string=au%3AB%C3%A9rard%20%26%20au%3AWebb&page=0&results_per_page=20 | `83d25d6edb79036e95e4ca4e711746c8422a2622fa7cef395a47a41e56ea4762` | every zbMATH document by Bérard and Webb: exactly two, Zbl 0841.58062 (C. R. 1995) and Zbl 1481.58014 (Math. Z. 2022) |
| `fetched/berardwebb/zb_0841.58062.json` | https://api.zbmath.org/v1/document/_search?search_string=an%3A0841.58062&page=0&results_per_page=1 | `fc5721056ce8e7d4442c060fa345e418d37caa5cdf98abed84e34f2c9bf1b127` | `berardwebb1995`: French title, C. R. Sér. I 320, no. 5, 533-536; English summary (compact flat surfaces with boundary, Neumann) |
| `fetched/berardwebb/zb_1481.58014.json` | https://api.zbmath.org/v1/document/_search?search_string=an%3A1481.58014&page=0&results_per_page=1 | `e888db078d769ff0ff8c1bac71962f84548e4b36b113e9fa70f641889fb3c4ea` | `berardwebb2022`: Math. Z. 300, no. 1, 139-160; DOI, arXiv 2008.12498, review |
| `fetched/berardwebb/csl_2022.json` | https://doi.org/10.1007/s00209-021-02758-y (CSL-JSON) | `5537e10f93864264102fee78814eac26237f80402381bbb35f1ddabb5c7abe63` | Crossref metadata of `berardwebb2022` (same bytes as `fetched/bib/berardwebb2022.json`) |
| `fetched/berardwebb/arxiv_2008.12498.xml` | https://export.arxiv.org/api/query?id_list=2008.12498 | `f0c6a755192b493e4898f80d539f479b319d52b5f6e79972c911ce598b4475bc` | abstract of arXiv:2008.12498v2 ("announced in the C. R. ... volume 320 in 1995") |
| `fetched/berardwebb/arxiv_2008.12498v2.pdf` | https://arxiv.org/pdf/2008.12498v2 | `d2e94d5e595ab65de9759b7d8c610f093e5dda1e8f88323e93632f3d9335dca0` | `berardwebb2022`: Thm 3.1 (flat surfaces with boundary, Neumann isospectral, one non-orientable), Thm 3.2 and Remarks 3.3(2) (hyperbolic surfaces with geodesic boundary), Remarks 3.3(3) (Doyle-Rossetti: orientability is heard for closed hyperbolic surfaces), Section 7 (closed manifolds: open problem); ref. [6] gives the C. R. title with "pas" |
| `fetched/berardwebb/gallica_sru_text.xml` | https://gallica.bnf.fr/SRU?operation=searchRetrieve&version=1.2&query=(gallica%20all%20%22entendre%20l'orientabilit%C3%A9%22)%20and%20(dc.date%20%3D%20%221995%22)&maximumRecords=10&collapsing=false | `7ddd3d5ff834d293d97f2b76f27764d22a246de25dfaa63a53b030bf63c2e551` | locates the C. R. issue of 2 March 1995 (ark:/12148/bpt6k62036636) |
| `fetched/berardwebb/gallica_62036636_manifest.json` | https://gallica.bnf.fr/iiif/ark:/12148/bpt6k62036636/manifest.json | `bf1a2647a5da0e4e4fd8e32863ba6de037b11832d0229be30ba3b159f172a4b5` | issue identification "1995/03/02 (SER1,T320,N5)" |
| `fetched/berardwebb/gallica_62036636_pagination.xml` | https://gallica.bnf.fr/services/Pagination?ark=bpt6k62036636 | `51427fbff5daaad3540087b05d22a7986c7d33ec89692b6a6889173be05810c6` | printed pp. 533-536 are views 29-32 |
| `fetched/berardwebb/alto29.xml` | https://gallica.bnf.fr/RequestDigitalElement?O=bpt6k62036636&E=ALTO&Deb=29 | `ab850cbbd474e4ffde8f0df0e4385afa1ef2e79ac5025c4e539ed11deb175543` | OCR of p. 533: running head "C. R. Acad. Sci. Paris, t. 320, Série I, p. 533-536, 1995", title, authors, Résumé/Abstract (text in `gallica_62036636_view29.txt`) |
| `fetched/berardwebb/alto30.xml` | https://gallica.bnf.fr/RequestDigitalElement?O=bpt6k62036636&E=ALTO&Deb=30 | `f2b8f2a1b03d7b75687140b64a0984a4c532f4d09411426315949ec58794e64e` | OCR of p. 534 (`gallica_62036636_view30.txt`) |
| `fetched/berardwebb/alto31.xml` | https://gallica.bnf.fr/RequestDigitalElement?O=bpt6k62036636&E=ALTO&Deb=31 | `b65da2bd1b03660fa1164f81776220f13cf68aa549582855c8403ba6a0d04a44` | OCR of p. 535: Théorème 1 (`gallica_62036636_view31.txt`) |
| `fetched/berardwebb/alto32.xml` | https://gallica.bnf.fr/RequestDigitalElement?O=bpt6k62036636&E=ALTO&Deb=32 | `6bed207133cb7985924cb70f30fba11033c6227a755e5dc934822c1c0b78431c` | OCR of p. 536: Dirichlet spectra differ; MSRI preprint 005-95 (`gallica_62036636_view32.txt`) |

## Bibliography records

`references.bib` is generated by `tools/build_bib.py` from the records below and nothing else
(re-fetched on 2026-10-06 for the 30-35 page revision; 69 entries, of which the paper cites 52 and the supplement 5).
DOIs are resolved by content negotiation (`Accept: application/vnd.citationstyles.csl+json`) at
https://doi.org; arXiv records come from the arXiv API (one batch file, hence the shared hash);
zbMATH records from the zbMATH Open API. No contact (e-mail) parameter was sent to any service.
CSL-JSON records carry an indexing timestamp, so a later fetch can have a different hash with the
same bibliographic fields. Fields not in a primary record come from a second fetched record named
in the script (`EVIDENCE`, `EVIDENCE_ZB`, `ADDRESS_ZB`, `PAGES_ZB`, `CHECK_EXTRA`), and every
sentence-cased title is asserted equal to the fetched title up to case, braces and accents.

| key | record URL | SHA-256 of the record as fetched |
|---|---|---|
| `dggw2008` | https://doi.org/10.1307/mmj/1213972406 | `5fe93eb00faa26cade2e29b5d387d261ec3e81372bbddbadbffb156c384831ef` |
| `donnelly1976` | https://doi.org/10.1007/BF01436198 | `bbc85f07a3f57613793ed07372c0c6b99f69008b8fd6beb5d5199b1b83b2f97f` |
| `ucar2017` | https://export.arxiv.org/api/query?id_list=1711.03405 | `887d721f98c1650a5d4b850c1561a89a1f8e6408a9ba2b6da9305e4a68fbe38c` |
| `schueth2019` | https://doi.org/10.5802/aif.3338 | `d9989d93b82332fdf5bcf6393b8c7e1dbd9564718147343ecb022e4442189ddf` |
| `berndtyeap2002` | https://doi.org/10.1016/S0196-8858(02)00020-9 | `fb67b5489e757aa2a7faabd94480d7f8c17cea00f020da2944f9d08bf5afc82c` |
| `adfg2008` | https://doi.org/10.1007/s10455-007-9092-6 | `4bf74b14edfc3ee8f3c5c7927e42868399e1f3f51b8cee5c69a355bd1be71fa4` |
| `drydenstrohmaier2009` | https://doi.org/10.4153/CMB-2009-008-0 | `e804657f5925b0394a6943d55138d745e13ffa208e2b754bc8c22a90dc2a955c` |
| `doylerossetti2011` | https://export.arxiv.org/api/query?id_list=1103.4372 | `887d721f98c1650a5d4b850c1561a89a1f8e6408a9ba2b6da9305e4a68fbe38c` |
| `linowitzvoight2015` | https://doi.org/10.1007/s00209-015-1500-1 | `298cabb4c0e862c5c506468c0dd896fa440c3cb27a14c9587fa93529ac2fb93c` |
| `marklof2011` | https://doi.org/10.1017/cbo9781139108782.003 | `f571f7bf8b44cd0859167e21422440483ef9909efc363db6654ceafc727a8a4d` |
| `troyanov1991` | https://doi.org/10.1090/S0002-9947-1991-1005085-9 | `0d8ed443df1778ed468f903f20b2198befbcb8cf753008b44c5195af7fdd39cd` |
| `thurston1980` | https://library.slmath.org/books/gt3m/PDF/13.pdf | `cee7a903a310621cb8f6616473696131b8c52e20957054d6242472d5dd5fb843` |
| `kac1966` | https://doi.org/10.1080/00029890.1966.11970915 | `9c060bbba66405e91bda874940fcc9c4dc8779fe05cddfe6df54acecaf8b6d27` |
| `mckeansinger1967` | https://doi.org/10.4310/jdg/1214427880 | `d00083440a5b3e5101c71833585019297ab7d9fc9904f0a06c9d3b38a2092bd0` |
| `sunada1985` | https://doi.org/10.2307/1971195 | `ddf2896844cebb714277102f96607ac8d82fb382cb658aecb7a4e39eb4e62aaa` |
| `gww1992` | https://doi.org/10.1090/S0273-0979-1992-00289-6 | `eb59280daf1324c9815ef1ee1682d25d6bd623cf728f21a8595a8d7608eba946` |
| `ssw2006` | https://doi.org/10.1007/s00013-006-1748-0 | `904f1ce04189080c1312b2aa6f369192446731c8431e41813586a30a82679d55` |
| `rsw2008` | https://doi.org/10.1007/s10455-008-9110-3 | `9d3ecd28143a3b7c8fe0d66f2c3c5f32421980c0e7c997c6aef2c1c2635bcc9d` |
| `barihunsicker2020` | https://doi.org/10.4153/S0008414X19000178 | `363ebbfff44da473ab492fdafd9077ee77e9a4d3805339f84782aac783534cdf` |
| `griesermaronna2013` | https://doi.org/10.1090/noti1063 | `e9c29988fe2596705954dd5daa2555622629141c8c3cc6034ba5f6edf552a6df` |
| `gomezserrano2021` | https://doi.org/10.1016/j.jde.2020.11.002 | `fe20c10bb5f313a694b74560a93dc109d57bbed54c572dc31af7c7316fac1ec2` |
| `holtztyaglov2012` | https://doi.org/10.1137/090781127 | `8fe0182587161ce76a61504a19f031d58058b0e7996c00047d5ad2256021af54` |
| `ostrowski1940` | https://doi.org/10.1007/bf02546330 | `352a841a8e0fc4826dc6d7f6a228f0af8203c6bd7604786ad6dc9f0a7e3a7194` |
| `steinig1971` | https://api.zbmath.org/v1/document/_search?search_string=an:0238.10007 | `5244cb8cccd4d3e748dd4887dd3ca554e1c364ade955e5d780f294f7e2694a3e` |
| `laurens2023` | https://doi.org/10.1007/s00526-023-02534-2 | `3d2cf130c87c1628d35789265a9dfd1d0cd326d8f67ac981a35a61f2cff441c2` |
| `msw2022` | https://doi.org/10.1080/10586458.2022.2061650 | `6ebbe47191a6a308d7f30f14ca67b745aba396ea8094a74485b0291bb4c2887f` |
| `korobovbugaevskaya2016` | https://doi.org/10.1090/mcom/2994 | `96eba9f2aa833a9cf265e5b4554c1f70e9167ed44ce64707adc87479d642b202` |
| `mueller2016` | https://doi.org/10.1007/s10208-014-9239-3 | `f5fd421e31fd9e077596bddc7c0b885d4c2a0874b0ea793e4bb3127864cae237` |
| `alloucheshallit1999` | https://doi.org/10.1007/978-1-4471-0551-0_1 | `33b8ac990e0f14d8ac3eaedbde2848c022b5e6712553fdda36a94accf7997882` |
| `bgn1993` | https://doi.org/10.1090/s0025-5718-1993-1189516-5 | `6a399b5df24d73540141be5d7d484650a1aa2a960881a4ea157f889aedbce93a` |
| `schinzel1996` | https://api.zbmath.org/v1/document/_search?search_string=an:0932.11019 | `fddd2f74469351c79c5e150c984988a800f638fff0c8824d2339f5a92d8cc5aa` |
| `beauville1982` | https://api.zbmath.org/v1/document/_search?search_string=an:0504.14016 | `2061e4e3233912f962968861cfc2cf6231bd7932b6100f7ed4c1d74e74cb6ab7` |
| `mazur1977` | https://doi.org/10.1007/bf02684339 | `39618c197ebfcddd78f8fc820a6b2190a799fb3f0b18ab6653228876675565dc` |
| `pari2172` | https://pari.math.u-bordeaux.fr/archives/pari-announce-25/msg00001.html | `2536b1e8a072fb8e1147c7b932491c44a9a95a71bfd9e8ed8e34f267f75735c9` |
| `strohmaieruski2013` | https://doi.org/10.1007/s00220-012-1557-1 | `b90480edde2f4b0008694f1236f0fff3d49c230d864ecc5242b6dabce550dd51` |
| `schoberl1997` | https://doi.org/10.1007/s007910050004 | `5a250e52842885817cd3b72547b2e8f283ea02a25018de846871f5401878d38d` |
| `arpack1998` | https://doi.org/10.1137/1.9780898719628 | `90f8bce56dc8f4ac1cd7a652a821dcdbe1e70f6a4dcfb48d9ca1f0ec3c9ec367` |
| `crameri2023` | https://doi.org/10.5281/zenodo.8409685 | `ac503ef9808315cae7ddf700d01edbf2b9905c04709071c6e47c30e68be09adb` |
| `crameri2020` | https://doi.org/10.1038/s41467-020-19160-7 | `71fb62f03cb4573e33fa1fbf49795e1136a3d6f46abd998c08eb1e26d6ebc061` |
| `dggw2017erratum` | https://doi.org/10.1307/mmj/1488510034 | `ac6eff24db9c602d691d783ceb79d5e0c5e549a34cbce4cb549e3389c735514f` |
| `hejhal1976` | https://api.zbmath.org/v1/document/_search?search_string=an:0347.10018 | `d866f6aa861752d6c0ab900f95626c06d2283e65c1a04d0d7fd881b4467ebb32` |
| `iwaniec2002` | https://api.zbmath.org/v1/document/_search?search_string=an:1006.11024 | `1183dbc267bc059fb2e950f148acb6baf5ad3e67f20560aea66d8ab062d3e08e` |
| `mckean1972` | https://api.zbmath.org/v1/document/_search?search_string=an:0225.30021 | `8fa19426f532803d94248c1bdea4feefe080d4b2359a3c4c2e93fbe2cb0313c9` |
| `mckean1974corr` | https://api.zbmath.org/v1/document/_search?search_string=an:0317.30018 | `e8a0c22511d7f5fa876f2df2995a4ef8540f86a9b373568c15299860dcca822a` |
| `huber1959` | https://api.zbmath.org/v1/document/_search?search_string=an:0089.06101 | `0a03e7a1ce53112fbd10fa62be27b62089474706010c81d707c7bf4b216e8db0` |
| `buser1992` | https://api.zbmath.org/v1/document/_search?search_string=an:0770.53001 | `62d8dcb585fbd53951361f1b57ecd67684b903453dead794465ddf5c50536bd8` |
| `wolpert1979` | https://api.zbmath.org/v1/document/_search?search_string=an:0441.30055 | `8c2fa822f0697a23525d3eca18fe1e88c67d8514d13d38fec2cfa3e513695d28` |
| `stanhope2005` | https://doi.org/10.1007/s10455-005-1584-7 | `0a60e5376c09f09e1fb1c0cb87203422fecee64d7470510a3f172077dccefe03` |
| `dryden2004` | https://export.arxiv.org/api/query?id_list=math/0411290 | `887d721f98c1650a5d4b850c1561a89a1f8e6408a9ba2b6da9305e4a68fbe38c` |
| `garbinjorgenson2020` | https://doi.org/10.2996/kmj/1584345689 | `77dab1d8e01336f8b50cd89a29ee88f8d8a9889ac4a80b6177c30c2981cc2cef` |
| `schueth2025` | https://doi.org/10.1007/s10455-025-10024-1 | `94c3dd1d804c9e81c8182f447780d2cf3f4e5afbc9bd16c5e7b2a77b3e7bd812` |
| `watson2005` | https://api.zbmath.org/v1/document/_search?search_string=an:1076.35042 | `81150591bdc91aa444d90d9249d134643bf9556c7c3177b0b1e4120611a244d6` |
| `philippe2008` | https://doi.org/10.5802/aif.2424 | `4668c7a1f3dc1e07edee745ed208f7c97b4a6494884d7a46417e696153c2eec4` |
| `philippe2010gd` | https://doi.org/10.1007/s10711-010-9473-z | `64cbcdffca4f876ad293f9a71ecb0db22871fc66e97fad4dc45926545c8cfffb` |
| `changdeturck1989` | https://api.zbmath.org/v1/document/_search?search_string=an:0721.58053 | `053e685ea470bc4e028c7193ec6dda34a313759b10bd52f8e63473aba106bdc4` |
| `strohmaieruski2018` | https://doi.org/10.1007/s00220-018-3094-z | `c19eb1eddcf2d8ad8e1c65a50c23af86768828ece10d3aada464e7e15486cc3a` |
| `ngsolve` | https://api.zbmath.org/v1/software/_search?search_string=NGSolve | `374450c425d25c9c9c8cd3c165588c264fbe7036bc37522a33aad570a5f43048` |
| `aby2015` | https://doi.org/10.1109/sampta.2015.7148965 | `f4732961c6a183e6457fa6375fad801bdfe9971db1a30b47dcce648c3accc537` |
| `bgy2020` | https://doi.org/10.1093/imaiai/iaaa005 | `efabe7f758b8d33910edeb09ae665ccd0fa3a0aee341139ac5eb55567e0e7d80` |
| `borweiningalls1994` | https://api.zbmath.org/v1/document/_search?search_string=an:0810.11016 | `9bc6bffe20115ab9c0c49af2e313abedc73c3de792546b6303609c6ba7307546` |
| `melzak1961` | https://doi.org/10.4153/CMB-1961-025-1 | `e55d71a0a2fa93d8f837fbfd576ba15e2f4e936b36ea34a47f68e332045404e6` |
| `blp2003` | https://doi.org/10.1090/S0025-5718-02-01504-1 | `084c850a28344aba735c8d27efbb0b20b1f73a47885f9b7e4e37b2366d79b330` |
| `cmsv2024` | https://doi.org/10.1090/mcom/3917 | `14f732522ad33a76cb8645d707431fb475183aa007ad9a468e5fd33139e67a72` |
| `chen2025survey` | https://export.arxiv.org/api/query?id_list=2506.11429 | `887d721f98c1650a5d4b850c1561a89a1f8e6408a9ba2b6da9305e4a68fbe38c` |
| `wooley2012` | https://doi.org/10.4007/annals.2012.175.3.12 | `51613348076970884c2f9f889a113b570c5dbfc5b21198c6ea58f44d88f8759e` |
| `wooley2019` | https://doi.org/10.1112/plms.12204 | `eb98a685a5b848b5e6b92d1a3e41ed063e881e8f0156d384a53d46fcdd5909de` |
| `crootmaoyip2026` | https://export.arxiv.org/api/query?id_list=2609.05061 | `887d721f98c1650a5d4b850c1561a89a1f8e6408a9ba2b6da9305e4a68fbe38c` |
| `cremona1997` | https://api.zbmath.org/v1/document/_search?search_string=an:0872.14041 | `60586fd241876ced445034bfb9e2b2dd87a5e2ea33303b7d5636e40c33bf8799` |
| `berardwebb1995` | https://api.zbmath.org/v1/document/_search?search_string=an:0841.58062 | `a7daa0298bfeb6aae5aa0f1e31831d1d2e85955f8648eaf8da4fa931d893bc47` |
| `berardwebb2022` | https://doi.org/10.1007/s00209-021-02758-y | `5537e10f93864264102fee78814eac26237f80402381bbb35f1ddabb5c7abe63` |
| `companion` | paper/arith/note.tex | `533d65cd7e6f224f566d35afa4c223937d8ee63eb5dad3b7509fb92379612276` |
| `jorgensen1976` | https://doi.org/10.2307/2373814 (Crossref record; the registry gives only the first page, 739) | `0f38cb057fcd37e7b9341763838a57dd555cda973b943d631b8f04604577c7ba` |
| `jorgensenwiki` (document) | https://en.wikipedia.org/wiki/J%C3%B8rgensen%27s_inequality, fetched 2026-10-07 with a desktop user agent; the statement of Jørgensen's inequality used in Section 4 is quoted from it, because the primary text (JSTOR) is not retrievable headless (theory/eigen/sources/README.md) | `fb2d20931d73ccb6cc88cfaf686547e477b8ce9d5df599fb997d503bdb592658` |

Documents without a registry record: `thurston1980` (the chapter's title page: "Electronic version
1.1 - March 2002", "electronic edition of the 1980 notes distributed by Princeton University"),
`pari2172` (the release announcement https://pari.math.u-bordeaux.fr/archives/pari-announce-25/msg00001.html:
"Done for version 2.17.2 (released 05/03/2025)"; the 2.17 changelog says 01/03/2025, and
`review/literature-pass/CITATIONS.md` section 4 prescribes the announcement), `ngsolve` (swMATH
software record 13154 via the zbMATH Open API), and `companion` (the authors' own manuscript
`paper/arith/note.tex`, checked for its title and the six author names).

## Re-creating the fetched files

```
python3 paper/jga/tools/build_bib.py --fetch      # bibliography records
```

and the `curl` commands implied by the URLs above for the template, guidelines, policies, MSC
list and texts.

## 2026-10-08. Round 4: new and repaired references

Found and read on 2026-10-08 (curl or Python `urllib`, desktop user agent; no e-mail address sent).
Bibliographic records are fetched by `python3 paper/jga/tools/build_bib.py --fetch` (URLs and SHA-256 of
every record in `fetched/bib_log.json`; all records were re-fetched on this date). Texts are copied to the
git-ignored `fetched/round4/`. The publishers' pages of Wiley, IOP, Elsevier, AMS and Springer return bot
checks to headless requests; Internet Archive copies were used where they exist.

| key | identifier | fetched (URL; SHA-256) | what was read / quoted |
|---|---|---|---|
| `doylerossetti2008` (new) | zbMATH 1146.58026 (New York J. Math. 14 (2008) 193-204; no DOI); arXiv:math/0605765v2 | zbMATH `916b1a76...e8c8`; https://arxiv.org/pdf/math/0605765 (`73cf715a...1b90`) | Abstract (v2, "Version dated 29 April 2008"), quoted in the report. Dryden-Strohmaier p. 2 (`review/literature-pass/_fetched/txt/drydenstrohmaier2009_cmb.txt`): "Shortly after preparing this manuscript, we learned that P. Doyle and J. P. Rossetti had proven this result independently (cf. [1])", [1] = arXiv math/0605765. arXiv journal_ref gives "193-2004" (typo); zbMATH 193-204 used. |
| `doylerossetti2011` (existing) | arXiv:1103.4372 | https://arxiv.org/abs/1103.4372 (`d2c96491...cd57`) | Title confirmed; abstract quoted in the report. |
| `proctorstanhope2010` (new) | doi:10.1016/j.difgeo.2009.03.015 | CSL `2582df8c...b6d1`; arXiv:0811.0797v2 (`d7335958...ac19`) | Abstract and Main Theorems 1-2 (arXiv). Published in vol. 28 (2010), not 2009. |
| `rsw2008` (existing) | doi:10.1007/s10455-008-9110-3 | CSL `9d3ecd28...cc9d`; https://export.arxiv.org/api/query?id_list=0710.2432 (`154d2ca1...1785`) | Title confirmed ("Isospectral orbifolds with different maximal isotropy orders", AGAG 34 (2008) 351-366; arXiv journal_ref agrees). Abstract (arXiv) quoted in the report. |
| `gittins2024` (new) | doi:10.1307/mmj/20216126 | CSL `d1aa8c76...11ba`; arXiv:2106.07882v2 (`cc25e578...301e`) | Abstract (= OpenAlex abstract), §1.1. Michigan Math. J. 74 (2024), no. 3, 571-598 (not 2023). |
| `nrs2019` (new) | doi:10.1007/978-3-030-04161-8_18; zbMATH 1447.35230 | CSL `c2dad2eb...fe81`; book record `1f68a723...7108`; zbMATH `0347fd2b...9d0a`; arXiv:2012.03366 (`d3f0fc88...095e`) | Abstract and p. 3. Planar/polygonal domains; conical singularities only in the locality discussion. |
| `nrs2025` (new) | doi:10.1007/s40316-024-00237-4 | CSL `cd4ba0ce...e9a0`; arXiv:1905.00259v2 (`bac70129...03e9`) | Abstract; Remark 6.6 (cone-point term (π² − α²)/(12πα) for opening angle 2α). Online 2024, vol. 49 no. 1 (2025). |
| `akr2026` (new) | doi:10.1007/s40316-025-00263-w | CSL `148471be...338e`; arXiv:2010.02776v3 (`128e9651...bcba`) | Abstract. Online 2025-09-17; print vol. 50 no. 1 (2026), pp. 35-72. Title "Polyakov formulas for conical singularities in two dimensions". |
| `cheeger1983` (new) | doi:10.4310/jdg/1214438175; zbMATH 0529.58034 | CSL `aeb646d1...05ff`; zbMATH `cf9dfd1c...c90e`; Project Euclid PDF (`711ba78d...a7bd`) | Thm 4.4, Example 4.1, (4.41), (4.42) on pp. 604-605 (read from the page images); Sommerfeld/Carslaw remark p. 589. Pages 575-657 from zbMATH. |
| `bruningseeley1987` (new) | doi:10.1016/0022-1236(87)90073-5; zbMATH 0625.47040 | CSL `c8e9fee2...9c8a` | Record and zbMATH review only (Elsevier; the Augsburg OPUS page has no full text). |
| `dowker1977` (new) | doi:10.1088/0305-4470/10/1/023 | CSL `7f45e537...bb9d` | Abstract only (OpenAlex); IOP full text behind a bot check. |
| `dowker1989` (new) | doi:10.1063/1.528395 | CSL `2dbd7e05...a7b1` | Abstract only (OpenAlex); AIP full text not tried successfully. |
| `bkd1996` (new) | doi:10.1007/bf02517895; zbMATH 0872.58065 | CSL `b19e8882...046c`; arXiv:hep-th/9602089v2 (`2cdb942e...3e05`) | Abstract; §6, eq. (6.4) and the sentence after it. Pages: Crossref 371-393, zbMATH 371-394 (Crossref used). |
| `ostrowski1940a` (new), `ostrowski1940` (existing) | doi:10.1007/bf02546329 (pp. 99-155), doi:10.1007/bf02546330 (pp. 157-257) | CSL `9a828fa7...ebc6`, `352a841a...7194`; Project Euclid PDFs of both parts (`53db1def...3d63`, `d095f7ca...d93e`) | Théorème XXX and (71,1) are in the **second** part, p. 212 (read from the page image); quoted in the report. The existing key `ostrowski1940` is that part. |
| `changdeturck1989` (repaired) | doi:10.1090/S0002-9939-1989-0953738-7 (was 10.2307/2047071) | CSL `8286e750...6c44` (content negotiation on 10.2307/2047071 returns the same record, whose DOI field is the AMS DOI); zbMATH `df35fe8c...56ac`; AMS PDF via the Internet Archive, https://web.archive.org/web/20190504123058/https://www.ams.org/journals/proc/1989-105-04/S0002-9939-1989-0953738-7/S0002-9939-1989-0953738-7.pdf (`03087f07...b98f`) | Full text. Proposition (p. 1034), Theorem 1 (p. 1036), Theorem 2 (p. 1037). **No angle condition**: N depends only on λ₁, λ₂ of T₀, and the conclusion is isospectrality. Pages 1033-1038 (zbMATH and the PDF; Crossref gives 1033 only). |
| `melzak1961` (existing) | doi:10.4153/CMB-1961-025-1 | CSL `e55d71a0...04e6` (unchanged) | Record confirmed: Canad. Math. Bull. 4(3) (1961) 233-237. |
| `mckean1974corr` (existing) | zbMATH 0317.30018; doi:10.1002/cpa.3160270109 | zbMATH `029e8b15...ec35`; Crossref CSL of the DOI | Confirmed it is the correction: CPAM 27 (1974), no. 1, p. 134; Crossref title "Correction to: Silberg' trace formua as applied to a compact riemann surface by H. P. Mckean, comm. pure appl. math. 25, pp. 225-246, 1972" (misspellings in the registry). Text not obtained (Wiley bot check). |
| `richardsonstanhope2020` (existing) | doi:10.1016/j.difgeo.2019.101577 | arXiv:1910.03224v1 (`704c7ea9...8149`) | §1: "The question of detecting the orientability, in the standard sense, of a manifold or orbifold from its Laplace spectrum is still unresolved in the closed setting." On p. 2 of arXiv v1; the journal pagination was not checked (Elsevier bot check). |
| Wróblewski (not added) | — | Chen survey arXiv:2506.11429 (`3273f806...eb8e`); Wayback copies of http://www.math.uni.wroc.pl/~jwr/eslp/ (`46392148...0d60`) and `.../eslp/tables.htm` (`512e67a0...6f63`) | Chen A.1.33 cites "[91] Jarosław Wróblewski. A Collection of Numerical Solutions of Multigrade Equations Related to the Prouhet-Tarry-Escott Problem, Version 12. 2009. http://www.math.uni.wroc.pl/~jwr/eslp/" (pp. 21-24). The archived pages contain congruence-solution files and tables, not that document; the live site did not answer. No citable fetched record: cite via Chen's survey. |
