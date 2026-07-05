import pandas as pd
from sympy import Rational


def generate_pillow_table():
    # 1. Generate all hyperbolic triads with S1 from 10 to 18
    data = []

    for S1 in range(10, 19):
        # Enforce ordering p <= q <= r to prevent duplicate multisets
        for p in range(2, S1 // 3 + 1):
            for q in range(p, (S1 - p) // 2 + 1):
                r = S1 - p - q

                # Hyperbolicity condition: 1/p + 1/q + 1/r < 1
                R = Rational(1, p) + Rational(1, q) + Rational(1, r)
                if R < 1:
                    data.append(
                        {
                            "S1": S1,
                            "Triad": (p, q, r),
                            "R_frac": R,
                            "R_str": f"{R.p}/{R.q}",
                            "Status": "unique",
                        }
                    )

    # 2. Identify collisions within the same S1 sum group
    # A collision means the same S1 group contains identical reciprocal sums (R)
    seen_signatures = {}
    for entry in data:
        sig = (entry["S1"], entry["R_frac"])
        if sig in seen_signatures:
            # Mark both the current and original occurrences as collisions
            entry["Status"] = "collision"
            seen_signatures[sig]["Status"] = "collision"
        else:
            seen_signatures[sig] = entry

    # 3. Format the table data beautifully
    formatted_rows = []
    for entry in data:
        s1 = entry["S1"]
        triad_str = f"({entry['Triad'][0]}, {entry['Triad'][1]}, {entry['Triad'][2]})"
        r_str = entry["R_str"]
        status = entry["Status"]

        # Highlight the minimal collision pair in bold text
        if status == "collision":
            triad_str = f"\033[1m{triad_str}\033[0m"
            r_str = f"\033[1m{r_str}\033[0m"
            status_str = f"\033[1m{status}\033[0m"
        else:
            status_str = status

        formatted_rows.append(
            {"S1": s1, "Pillow (p, q, r)": triad_str, "R": r_str, "Status": status_str}
        )

    # 4. Build and render the Pandas DataFrame
    df = pd.DataFrame(formatted_rows)

    # Set up styling options for a beautiful terminal presentation
    pd.set_option("display.max_rows", None)
    pd.set_option("display.width", 1000)
    pd.set_option("display.colheader_justify", "center")

    print("\n" + "=" * 62)
    print("  TABLE 1: EXACT VERIFICATION OF ARITHMETIC INVARIANTS  ")
    print("=" * 62)
    print(df.to_string(index=False))
    print("=" * 62 + "\n")


if __name__ == "__main__":
    generate_pillow_table()
