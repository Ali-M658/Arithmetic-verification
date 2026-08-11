#!/usr/bin/env python3
"""Runs all the verification suites + regenerates both LaTeX tables."""
import sys
import time

import advanced_pillow_verification
import enumerate_degeneracies
import generate_latex_supplementary_table


def main():
    start = time.time()
    print("running full verification + table regen\n")

    print(">>> step 1: pillow verification checks")
    try:
        advanced_pillow_verification.run_verification()
        print("step 1 ok\n")
    except Exception as e:
        print(f"validation failed: {e}")
        sys.exit(1)

    print(">>> step 2: table 1 (tab:enum)")
    try:
        enumerate_degeneracies.generate_table1_latex()
        print("\nstep 2 ok\n")
    except Exception as e:
        print(f"table 1 generation failed: {e}")
        sys.exit(1)

    print(">>> step 3: table 2 (tab:density)")
    try:
        generate_latex_supplementary_table.generate_table2_latex()
        print("\nstep 3 ok\n")
    except Exception as e:
        print(f"table 2 generation failed: {e}")
        sys.exit(1)

    print(f"done in {time.time() - start:.3f}s")


if __name__ == "__main__":
    main()
