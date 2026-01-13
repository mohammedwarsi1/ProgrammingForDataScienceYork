import pandas as pd
from scipy.stats import mannwhitneyu

inputStat = "data/processed/exoplanets_clean.csv"

def main():
    df = pd.read_csv(inputStat)

    # Filter to two main discovery methods
    transit = df.loc[df["discoverymethod"] == "Transit", "pl_rade"].dropna()
    rv = df.loc[df["discoverymethod"] == "Radial Velocity", "pl_rade"].dropna()

    print(f"Transit sample size: {len(transit)}")
    print(f"Radial Velocity sample size: {len(rv)}")

    # Mann–Whitney U test (two-sided)
    stat, p_value = mannwhitneyu(transit, rv, alternative="two-sided")

    print("\nMann–Whitney U test results")
    print(f"U statistic: {stat:.2f}")
    print(f"p-value: {p_value:.4e}")

    # Interpretation
    alpha = 0.05
    if p_value < alpha:
        print("\nResult: Statistically significant difference in planet radii.")
    else:
        print("\nResult: No statistically significant difference in planet radii.")

if __name__ == "__main__":
    main()
