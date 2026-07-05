from collections import defaultdict
from fractions import Fraction


def generate_mathematical_table():
    # 1. Generate all hyperbolic triads within the exact window 10 <= S1 <= 18
    all_triads = []

    for S1 in range(10, 19):
        # Enforce ordering p <= q <= r to prevent duplicate multisets
        for p in range(2, S1 // 3 + 1):
            for q in range(p, (S1 - p) // 2 + 1):
                r = S1 - p - q

                # Hyperbolicity condition: 1/p + 1/q + 1/r < 1
                R_val = Fraction(1, p) + Fraction(1, q) + Fraction(1, r)
                if R_val < 1:
                    all_triads.append(
                        {
                            "S1": S1,
                            "p": p,
                            "q": q,
                            "r": r,
                            "R_frac": R_val,
                            "Status": "unique",
                        }
                    )

    # 2. Map within-sum signatures to identify any two-coefficient collisions
    # Groups are categorized strictly by the tuple key: (S1_sum, Reciprocal_Sum)
    signature_map = defaultdict(list)
    for triad in all_triads:
        key = (triad["S1"], triad["R_frac"])
        signature_map[key].append(triad)

    for signature, matches in signature_map.items():
        if len(matches) > 1:
            for triad in matches:
                triad["Status"] = "collision"

    # 3. Print the beautifully formatted structural table output
    header = f"{'S1':<4} | {'(p, q, r)':<12} | {'R':<8} | {'Status'}"
    print("\n" + "=" * len(header))
    print(header)
    print("=" * len(header))

    last_s1 = None
    for triad in all_triads:
        # Visually group identical S1 sums together by blanking out repeats
        s1_display = str(triad["S1"]) if triad["S1"] != last_s1 else ""
        last_s1 = triad["S1"]

        triad_str = f"({triad['p']}, {triad['q']}, {triad['r']})"
        r_str = f"{triad['R_frac'].numerator}/{triad['R_frac'].denominator}"
        status_str = triad["Status"]

        # ANSI escape codes to highlight the minimal arithmetic collision in Bold Red text
        if status_str == "collision":
            triad_str = f"\033[1;31m{triad_str}\033[0m"
            r_str = f"\033[1;31m{r_str}\033[0m"
            status_str = f"\033[1;31m{status_str}\033[0m"

        print(f"{s1_display:<4} | {triad_str:<12} | {r_str:<8} | {status_str}")

    print("=" * len(header) + "\n")


if __name__ == "__main__":
    generate_mathematical_table()
