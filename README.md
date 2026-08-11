Arithmetic Verification for Hyperbolic Triangular Pillows:
The verification suite and latex  table makers used to work the manuscript.



* `run_all.py`  is the script executing all checks and regenerating tables.
* `advanced_pillow_verification.py` is the Diophantine bound checks and Newton–Vieta reconstructions.
* `enumerate_degeneracies.py`  makes  Table 1 (`\label{tab:enum}`).
* `generate_latex_supplementary_table.py` makes Table 2 (`\label{tab:density}`).

how to run it yourself:

```bash
pip install sympy
python run_all.py
