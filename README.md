# Inferential Statistical Analysis of Diabetes Data

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?logo=scipy&logoColor=white)
![seaborn](https://img.shields.io/badge/seaborn-4C72B0)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=white)

A hypothesis-testing study that asks which clinical measurements differ **significantly** between people with and without type-2 diabetes — i.e., which features could serve as diagnostic signals rather than just descriptive summaries.

## Motivation

Inferential statistics is used extensively in biomedical research to *explain* observed phenomena rather than merely summarize them. In diagnostics, this reveals which signs accompany or indicate a disease. This project tests whether feature differences between diabetic and non-diabetic groups are statistically significant enough to support diagnosis of type-2 diabetes.

## Dataset

The **Pima Indians Diabetes** dataset — **768 participants, 9 features**. To reduce confounds, all participants are female, at least 21 years old, and of Pima Indian heritage.

| Feature | Meaning |
|---------|---------|
| Pregnancies | Number of times pregnant |
| Glucose | Plasma glucose (mg/dL) |
| BloodPressure | Diastolic blood pressure (mm Hg) |
| SkinThickness | Triceps skin-fold thickness (mm) |
| Insulin | Serum insulin (µU/mL) |
| BMI | Body-mass index (kg/m²) |
| DiabetesPedigree | Genetic diabetes-history score |
| Age | Age (years) |
| Outcome | 1 = diabetic, 0 = non-diabetic |

## What the analysis does

- **Data cleaning** — physiologically impossible zero values (e.g., zero glucose or blood pressure) are treated as missing and imputed with the feature median, which restores approximately normal distributions.
- **Exploratory analysis** — several features (glucose, blood pressure, skin thickness, insulin, BMI) show bimodal distributions, examined via pair plots and histograms.
- **Inferential testing** — statistical tests compare the diabetic and non-diabetic groups feature by feature to determine which differences are significant.

## Repository contents

| File | Description |
|------|-------------|
| `Python_Code.ipynb` | Full cleaning, EDA, and hypothesis-testing workflow |

## Tech stack

Python · pandas · NumPy · SciPy (`scipy.stats`) · seaborn · matplotlib
