import pandas as pd
import matplotlib.pyplot as plt

inputpath = "data/processed/exoplanets_clean.csv"
output_path = "outputs/figures/"

def savefig(name: str):
    plt.tight_layout()
    plt.savefig(output_path + name, dpi=200)
    plt.close()

def main():
    df = pd.read_csv(inputpath)

    # 1) Discoveries per year (trend)
    plt.figure()
    df["disc_year"].value_counts().sort_index().plot()
    plt.xlabel("Discovery year")
    plt.ylabel("Number of exoplanets")
    plt.title("Exoplanet discoveries per year")
    savefig("figure1_discoveries_per_year.png")

    # 2) Discovery method distribution
    plt.figure()
    df["discoverymethod"].value_counts().head(10).plot(kind="bar")
    plt.xlabel("Discovery method")
    plt.ylabel("Number of exoplanets")
    plt.title("Top discovery methods (top 10)")
    plt.xticks(rotation=30, ha="right")
    savefig("figure2_discovery_methods.png")

    # 3) Planet radius distribution (histogram)
    plt.figure()
    r = df["pl_rade"].dropna()
    plt.hist(r, bins=60)
    plt.xlabel("Planet radius (Earth radii)")
    plt.ylabel("Count")
    plt.title("Distribution of exoplanet radii")
    savefig("figure3_radius_distribution.png")

    # 4) Orbital period vs radius (log–log scatter)
    plt.figure()
    plt.scatter(df["pl_orbper"], df["pl_rade"], s=8, alpha=0.6)
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Orbital period (days)")
    plt.ylabel("Planet radius (Earth radii)")
    plt.title("Orbital period vs planet radius (log–log)")
    savefig("figure4_period_vs_radius_loglog.png")

    # 5) Radius by method (boxplot)
    top_methods = df["discoverymethod"].value_counts().head(5).index.tolist()
    data = [
        df.loc[df["discoverymethod"] == m, "pl_rade"].dropna().values
        for m in top_methods
    ]

    plt.figure()
    plt.boxplot(data, labels=top_methods, showfliers=False)
    plt.yscale("log")
    plt.ylabel("Planet radius (Earth radii)")
    plt.title("Planet radius by discovery method (top 5)")
    plt.xticks(rotation=30, ha="right")
    savefig("figure5_radius_by_method.png")


if __name__ == "__main__":
    main()
