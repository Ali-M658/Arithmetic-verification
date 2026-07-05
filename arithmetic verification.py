from sympy import Rational
from collections import defaultdict


def verify_pillow_arithmetic():
    print("Computational Verification of Heat Trace Invariants")

    # Dictionary to group triads by their signature (S1, R)
    two_coef_map = defaultdict(list)

    # Range of cone-order sums to check (10 to 18)
    # No hyperbolic triads exist for S1 <= 9
    for S1 in range(10, 19):
        # Generate all ordered triples (p, q, r) such that 2 <= p <= q <= r and p + q + r = S1
        for p in range(2, S1 // 3 + 1):
            for q in range(p, (S1 - p) // 2 + 1):
                r = S1 - p - q

                # Check the hyperbolicity condition: 1/p + 1/q + 1/r < 1
                R = Rational(1, p) + Rational(1, q) + Rational(1, r)
                if R < 1:
                    two_coef_map[(S1, R)].append((p, q, r))

    # Part 1: Verify Theorem A (No collisions for S1 <= 17) ---
    print("--- Verifying Theorem A ---")
    collision_found_le_17 = False
    for (S1, R), triads in sorted(two_coef_map.items()):
        if S1 <= 17 and len(triads) > 1:
            collision_found_le_17 = True
            print(f"CRITICAL: Found unexpected collision at S1={S1}: {triads}")

    if not collision_found_le_17:
        print("Success: Verified Theorem A. No two-coefficient collisions exist for S1 <= 17.")
        print("Every hyperbolic pillow in this range is uniquely determined by its first 2 coefficients.\n")

    #  Part 2: Verify Theorem B (Minimal collision at S1 = 18) ---
    print("--- Verifying Theorem B ---")
    collisions_at_18 = []
    for (S1, R), triads in sorted(two_coef_map.items()):
        if S1 == 18 and len(triads) > 1:
            collisions_at_18.append(((S1, R), triads))

    if len(collisions_at_18) == 1:
        (S1, R), triads = collisions_at_18[0]
        print(f"Success: Verified Theorem B. Found exactly one minimal collision at S1 = 18.")
        print(f"  Signature (S1, R): ({S1}, {R})")
        print(f"  Colliding Pillows: {', '.join([f'O{t}' for t in triads])}")

        # Verify the specific minimal pair matching the paper
        if set(triads) == {(2, 8, 8), (3, 3, 12)}:
            print("  Pair accurately matches O(2,8,8) and O(3,3,12).\n")
    else:
        print(f"ERROR: Expected exactly 1 collision at S1=18, found {len(collisions_at_18)}.")

    # Part 3: Verify Lemma 3.1 (Structural Bounds Constraints) ---
    print("--- Verifying Lemma 3.1 Constraints on the Collision ---")
    if collisions_at_18:
        _, triads = collisions_at_18[0]
        # Label so that p < p'
        t1, t2 = sorted(triads, key=lambda x: x[0])
        p, q, r = t1
        p_prime, q_prime, r_prime = t2
        S = 18

        # Evaluate inequalities
        cond1 = p < p_prime
        cond2 = p_prime < 3 * p
        cond3 = S >= 3 * p_prime

        print(f"  Checking conditions for p={p}, p'={p_prime}, S={S}:")
        print(f"  - p < p'       : {p} < {p_prime} -> {cond1}")
        print(f"  - p' < 3p      : {p_prime} < {3 * p} -> {cond2}")
        print(f"  - S >= 3p'     : {S} >= {3 * p_prime} -> {cond3}")
        if cond1 and cond2 and cond3:
            print("  Success: Minimal collision lemma constraints strictly hold.\n")

    #  Part 4: Verify Proposition 2.5 (3rd Coefficient Breaks Collision) ---
    print("--- Verifying Proposition 2.5 (Resolution via 3rd Invariant) ---")
    if collisions_at_18:
        _, triads = collisions_at_18[0]
        t1, t2 = triads

        # Third heat invariant extracts the power sum P3 = p^3 + q^3 + r^3
        P3_t1 = t1[0] ** 3 + t1[1] ** 3 + t1[2] ** 3
        P3_t2 = t2[0] ** 3 + t2[1] ** 3 + t2[2] ** 3

        print(f"  P3 for O{t1}: {t1[0]}^3 + {t1[1]}^3 + {t1[2]}^3 = {P3_t1}")
        print(f"  P3 for O{t2}: {t2[0]}^3 + {t2[1]}^3 + {t2[2]}^3 = {P3_t2}")

        if P3_t1 != P3_t2:
            print("  Success: The third heat invariant distinguishes the two colliding pillows.")
            print("  The 3-coefficient map is completely injective in this threshold range.")


if __name__ == "__main__":
    verify_pillow_arithmetic()
