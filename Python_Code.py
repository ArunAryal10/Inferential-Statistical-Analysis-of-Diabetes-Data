"""
Inferential Statistical Analysis of the Pima Indians Diabetes dataset.

Cleans the data, explores feature distributions, and runs hypothesis tests to
determine which clinical measurements differ significantly between diabetic and
non-diabetic groups.

Inputs
------
- diabetes.csv : 768 rows x 9 columns. Features: Pregnancies, Glucose,
  BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age;
  target: Outcome (1 = diabetic, 0 = non-diabetic). Path in the original
  notebook is a Windows path ('D:\\Downloads\\diabetes.csv') -- update it to
  your local path.

Data shape
----------
- df : (768, 9)

Processing
----------
- Physiologically impossible zeros in Glucose, BloodPressure, SkinThickness,
  Insulin, and BMI are set to NaN and imputed with each feature's median.

Outputs (computed / displayed)
------------------------------
- Pair plots, correlation matrix, group means by Outcome.
- Normality test (D'Agostino) on BloodPressure; 95% and 99% confidence intervals.
- One- and two-sample t-tests on BloodPressure, Glucose, and Insulin comparing
  diabetic vs non-diabetic groups (alpha = 0.01).

Dependencies
------------
pandas, numpy, matplotlib, seaborn, scipy.stats.
"""

# %%
# python libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# [notebook magic] %matplotlib inline
import scipy.stats as stats
import seaborn as sns

# %%
#Importing data into python 
df = pd.read_csv(r'D:\Downloads\diabetes.csv')
df.head(n = 10) 

# %%
df.shape

# %% [markdown]
# This dataset contains 768 measurements and 9 features.

# %%
df['Age'].mean() 

# %%
df['Outcome'].value_counts()

# %%
sns.pairplot(df)

# %% [markdown]
# Pairpot analysis: Histograms for glucose, blood pressure, skin thickness,
# insulin, and BMI seem to be bimodal distribution

# %%
df.isnull().any()

# %%
df["Glucose"] = df["Glucose"].replace(0, np.NaN)
df["BloodPressure"] = df["BloodPressure"].replace(0, np.NaN)
df["SkinThickness"] = df["SkinThickness"].replace(0, np.NaN)
df["Insulin"] = df["Insulin"].replace(0, np.NaN)
df["BMI"] = df["BMI"].replace(0, np.NaN)

# %%
sns.pairplot(df)

# %% [markdown]
# Executing the first line of given code replaced any zero values with null. Doing this basically ignored the data point while calculating mean or median. Hence, we can see a normal distribution now.

# %%
df.isnull().any()

# %%
df.isna().sum() 

# %% [markdown]
# Executing second line of code tells us that there are null values in glucose, blood pressure, skin thickness, insulin, and BMI which need to be relpaced.

# %%
df['Glucose'].fillna(df['Glucose'].median(), inplace = True)
df['BloodPressure'].fillna(df['BloodPressure'].median(),inplace=True)
df['SkinThickness'].fillna(df['SkinThickness'].median(),inplace=True)
df['Insulin'].fillna(df['Insulin'].median(),inplace=True)
df['BMI'].fillna(df['BMI'].median(),inplace=True)  

# %% [markdown]
# Executing the third line of code replaced all null values with the median of the individual feature.

# %% [markdown]
# In my opinion replacing null values with either mean or median is valid in this case because we have low number of measurements. However, if we had a large number of measurements, we could have basically dropped those null measurements.

# %%
df.corr()

# %% [markdown]
# Pregnancy has highest correlation with age (0.544341).

# %% [markdown]
# Glucose has highest correlation with outcome (0.492782).

# %%
df.groupby(['Outcome']).mean()

# %% [markdown]
# Each features has lower average value with outcome 0 (no diabetes) compared to Outcome 1 (diabetes).

# %%
sns.pairplot(df,hue = 'Outcome')

# %% [markdown]
# Part 2 – Hypothesis Generation and Testing

# %%
stats.probplot(df['BloodPressure'], plot = plt)

# %%
#normality test
#H0: Blood pressure is normally distributed
#H1: Blood pressure isn't normally distributed
# alpha = 0.01

stats.normaltest(df['BloodPressure'])

# %% [markdown]
# Since, p-value is smaller than alpha, we conculde H1 i.e., Blood pressure isn't normally distributed.

# %%
df['BloodPressure'].mean() 

# %%
np.percentile(df['BloodPressure'],[2.5,97.5]) 

# %% [markdown]
# 95% confidence interval means we are 95% certain that the mean falls within this range.

# %%
np.percentile(df['BloodPressure'],[0.5,99.5]) 

# %% [markdown]
# 99% confidence interval means we are 99% certain that the mean falls within this range.

# %% [markdown]
# Yes, the mean falls within both of the confidence interval 95% and 99%.

# %%
df.head()

# %%
#3(a)

#H0: The blood pressure of people without diabetes is not significantly different than the mean BP of population
#H1: The blood pressure of people without diabetes is significantly different than the mean BP of population
# alpha = 0.01

stats.ttest_1samp(df[df['Outcome'] == 0]['BloodPressure'], popmean = 71)

# %% [markdown]
# Since p-value is higher than alpha, we fail to reject H0. i.e. we conclude the blood pressure of people without diabetes is not significantly different than the mean BP of population.

# %%
#3(b)

#H0: The blood pressure of people with diabetes is not significantly different than the mean BP of population
#H1: The blood pressure of people with diabetes is significantly different than the mean BP of population
# alpha = 0.01

stats.ttest_1samp(df[df['Outcome'] == 1]['BloodPressure'], popmean = 71)

# %% [markdown]
# Since p-value is less than alpha, we reject H0. i.e. we conclude the blood pressure of people with diabetes is significantly different than the mean BP of population.

# %%
#3(c)

#H0: mean blood pressure of people with and without diabetes in this sample is not significantly different. 
#H1: mean blood pressure of people with and without diabetes in this sample is significantly different. 
# alpha: 0.01 

stats.ttest_ind(df[df['Outcome'] == 1]['BloodPressure'], df[df['Outcome'] == 0]['BloodPressure'])

# %% [markdown]
# Since p-value is less than alpha, we reject H0. i.e. we conclude the mean blood pressure of people with and without diabetes in this sample is significantly different.

# %%
# 4. 

#H0: The glucose level of people without diabetes is not significantly different than the mean glucose level of population
#H1: The glucose level of people without diabetes is significantly different than the mean glucose level of population
# alpha = 0.01

stats.ttest_1samp(df[df['Outcome'] == 0]['Glucose'], popmean = 110)

# %% [markdown]
# Since p-value is higher than alpha, we fail to reject H0. i.e. we conclude the glucose level of people without diabetes is not significantly different than the mean glucose level of population.

# %%
#H0: The glucose level of people with diabetes is not significantly different than the mean glucose level of population
#H1: The glucose level of people with diabetes is significantly different than the mean glucose level of population
# alpha = 0.01

stats.ttest_1samp(df[df['Outcome'] == 1]['Glucose'], popmean = 110)

# %% [markdown]
# Since p-value is less than alpha, we reject H0. i.e. we conclude the glucose level of people with diabetes is significantly different than the mean glucose level of population.

# %%
#H0: mean glucose level of people with and without diabetes in this sample is not significantly different. 
#H1: mean glucose level of people with and without diabetes in this sample is significantly different. 
# alpha: 0.01 

stats.ttest_ind(df[df['Outcome'] == 1]['Glucose'], df[df['Outcome'] == 0]['Glucose'])

# %% [markdown]
# Since p-value is less than alpha, we reject H0. i.e. we conclude the mean glucose level of people with and without diabetes in this sample is significantly different.

# %%
# 5. 
# I chose insulin 

#H0: mean insulin level of people with and without diabetes in this sample is not significantly different. 
#H1: mean insulin level of people with and without diabetes in this sample is significantly different. 
# alpha: 0.01 

stats.ttest_ind(df[df['Outcome'] == 1]['Insulin'], df[df['Outcome'] == 0]['Insulin'])

# %% [markdown]
# Since p-value is less than alpha, we reject H0. i.e. we conclude the mean insulin level of people with and without diabetes in this sample is significantly different.
