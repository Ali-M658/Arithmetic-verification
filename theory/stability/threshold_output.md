# T4: exact integer recovery thresholds (from threshold.py; threshold_results.json holds the exact values)

Absolute model |H~_nu - H_nu(m)| <= delta for nu = -1..n-2. delta_thm <= delta_cert <= delta_true <= delta_up.
delta_thm and delta_cert are printed rounded down; delta_up is printed rounded up. Every printed delta_cert is re-certified exactly below.

| m | n | delta_thm | delta_cert | delta_up | failure at | delta_cert/|H_nu| | eps_cert |
|---|---|---|---|---|---|---|---|
| (2, 8, 8) | 3 | 3.802e-07 | 2.341e-03 | 2.485e-03 | 8-1/2 (real) | 1.87e-02, 1.67e-03, 7.02e-04 | 1.94e-03 |
| (3, 3, 12) | 3 | 1.189e-07 | 4.040e-03 | 4.589e-03 | 3+1/2 (real) | 3.23e-02, 2.89e-03, 7.45e-04 | 4.49e-03 |
| (3, 10, 15, 30) | 4 | 4.021e-11 | 3.660e-03 | 7.488e-03 | 10+1/2 (real) | 4.99e-03, 8.05e-04, 4.12e-05, 3.64e-07 | 8.70e-04 |
| (4, 5, 21, 28) | 4 | 3.147e-11 | 1.461e-03 | 2.018e-03 | 5-1/2 (real) | 1.99e-03, 3.21e-04, 1.64e-05, 1.72e-07 | 4.62e-04 |
| (2, 3, 7) | 3 | 4.492e-07 | 3.658e-03 | 6.587e-03 | 3-1/2 (real) | 3.07e-01, 4.00e-03, 2.70e-03 | 5.01e-03 |
| (4, 4, 4) | 3 | 9.354e-07 | 4.539e-04 | 5.036e-04 | 4+1/2 (real) | 3.63e-03, 5.06e-04, 5.43e-04 | 8.25e-04 |
| (7, 7, 7) | 3 | 9.973e-08 | 8.068e-05 | 8.273e-05 | 7-1/2 (real) | 2.82e-04, 4.98e-05, 2.36e-05 | 1.28e-04 |
| (3, 3, 4, 4) | 4 | 1.486e-09 | 9.597e-05 | 1.195e-04 | 4-1/2 (real) | 2.30e-04, 1.03e-04, 1.15e-04, 7.25e-05 | 1.18e-04 |
| (5, 5, 5, 5) | 4 | 4.743e-10 | 3.617e-05 | 3.826e-05 | 5-1/2 (real) | 6.02e-05, 2.58e-05, 1.92e-05, 6.28e-06 | 3.14e-05 |
| (2, 2, 2, 3) | 4 | 2.031e-09 | 1.858e-04 | 2.520e-04 | 3-1/2 (real) | 2.23e-03, 3.26e-04, 5.63e-04, 7.71e-04 | 4.39e-04 |
| (2, 2, 2, 2, 3) | 5 | 2.729e-12 | 7.908e-06 | 5.743e-05 | 2+1/2 (real) | 2.37e-05, 1.29e-05, 2.10e-05, 2.94e-05, 1.97e-05 | 1.46e-05 |

All printed delta_cert values re-certified exactly (Proposition S5).
