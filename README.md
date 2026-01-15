**README**
---
Programming for Data Science Freeform Assessment - Exoplanet Analysis Project
---
**Project Overview:**
This analysis on exoplanets using data from NASA's Exoplanet Archive is to investigate whether exoplanets detected from the Transit Method have a different radii compared to those that were discovered using Radial Velocity. The project includes data cleaning and preparation, exploratory data analysis, statistical hypothesis testing and data visualisation, all done using Python.

**Research Question:**
Do planets discovered via the Transit Method have a different radii than those discovered via Radial Velocity?

**Repository Structure**

**data/raw** - contains the original exoplanet dataset sourced from NASA's Exoplanet Archive.
**data/processed** - contains the cleaned dataset generated during preprocessing.
**src/** - consists of all python scripts for this analysis
**outputs/figures** - consists of all the plots generated during visualisation
**outputs/tables** - contains all tables generated through data analysis
**presentation/** - includes the final presentation for this project

**Python Scripts**

**src/clean_load.py** - This script is to be used for data cleaning and preprocessing. It loads the raw file from NASA in, selects necessary variables, converts numeric columns to appropriate data types, fixes missingness and saves this new cleaned dataset to data/processed/exoplanets_clean.csv.
**src/2_data_analysis.py** - This script performs the initial data analysis on the cleaned dataset and generates an overview of the dataset. It provides summary statistics for numeric variables and saves the outputs to outputs/tables.
**src/3_visualisation.py** - This script generates all of the visualisations needed for this project and saves all the plots to outputs/figures.
**src/4_statstest.py** - This script performs the statistical hypothesis testing for this project using the Mann-Whitney U test.


**Python Packages Used**
The following packages are required to conduct this analysis: 
- pandas
- matplotlib
- scipy

All scripts can run on any device with python given that these packages are installed.

**Data Source:**
The raw dataset used in this project is sourced from NASA (PSCompPars table) and is included in this repo under data/raw. **NO external download is required**

**Presentation:**
The final presentation for this project is available in presentation/Programming for Data Science.pptx



