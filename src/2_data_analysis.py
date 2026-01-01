import pandas as pd

data = "data/processed/exoplanets_clean.csv"

def main():
    analysisdf = pd.read_csv(data)

    # 1 - Overview of Dataframe
    overview = pd.DataFrame([{
        "rows": len(analysisdf),
        "unique_planets": analysisdf["pl_name"].nunique(),
        "discovery_methods": analysisdf["discoverymethod"].nunique(),
        "min_year": int(analysisdf["disc_year"].min()),
        "max_year": int(analysisdf["disc_year"].max()),
    }])
    overview.to_csv("outputs/tables/overview.csv", index=False)

    # 2 - Missingness rates
    missingrate = analysisdf.isna().mean().sort_values(ascending=False)
    missingrate.to_csv("outputs/tables/missing_rate.csv")

    # 3 - Summary statistics
    numeric_cols = ["pl_orbper", "pl_rade", "pl_bmasse", "pl_eqt", "st_teff"]
    summary = analysisdf[numeric_cols].describe().T
    summary.to_csv("outputs/tables/summary_stats.csv")

    # 4 - Discovery method counts
    method_counts = analysisdf["discoverymethod"].value_counts()
    method_counts.to_csv("outputs/tables/discovery_method_counts.csv")

    print("Exploratory Data Analysis tables saved in outputs/tables/")
    print(overview.to_string(index=False))
    print("\nTop discovery methods:")
    print(method_counts.head(10).to_string())

if __name__ == "__main__":
    main()
