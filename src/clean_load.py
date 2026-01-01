
import pandas as pd

rawPath = "data/raw/exoplanets.csv"
outputPath = "data/processed/exoplanets_clean.csv"

keepColumns = [
    "pl_name",
    "discoverymethod",
    "disc_year",
    "pl_orbper", #orbital period (days)
    "pl_rade", #planet radius (earth radii)
    "pl_bmasse", #planet mass (earth masses)
    "pl_eqt", #equilibrium temperature (Kelvin (k))
    "st_teff" #host star effective temperature (Kelvin (k))
]

def main():
    raw_df = pd.read_csv(rawPath, comment="#"
)

    missing = [c for c in keepColumns if c not in raw_df.columns]
    if missing:
        raise ValueError(f"Missing columns in file: {missing}")

    copydf = raw_df[keepColumns].copy()

    numeric_cols = [
        "disc_year",
        "pl_orbper",
        "pl_rade",
        "pl_bmasse",
        "pl_eqt",
        "st_teff"
    ]

    for c in numeric_cols:
        copydf[c] = pd.to_numeric(copydf[c], errors="coerce")

    df_clean = copydf.dropna(
        subset=["pl_name", "discoverymethod", "disc_year", "pl_orbper", "pl_rade"]
    )

    df_clean = df_clean[
        (df_clean["pl_orbper"] > 0) & (df_clean["pl_rade"] > 0)
    ]

    df_clean.to_csv(outputPath, index=False)

    print("Saved cleaned dataset:", outputPath)
    print("Rows:", len(df_clean))
    print(df_clean.head())

if __name__ == "__main__":
    main()
