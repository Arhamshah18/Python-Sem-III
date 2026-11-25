
# Assignment 12: Exploratory Data Analysis on Customer Churn Dataset

# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set visualization style
sns.set(style="whitegrid")

# 1. Load Dataset
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

print("\n----- FIRST FIVE ROWS -----")
print(df.head())

# 2. Dataset Information
print("\n----- DATASET SHAPE -----")
print(df.shape)

print("\n----- DATASET INFORMATION -----")
df.info()

# 3. Data Cleaning
print("\n----- MISSING VALUES BEFORE CLEANING -----")
print(df.isnull().sum())

print("\nDuplicate Records:", df.duplicated().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert TotalCharges into numeric format
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"], errors="coerce"
)

# Replace blank spaces with NaN
df.replace(r'^\s*$', np.nan, regex=True, inplace=True)

# 4. Handle Missing Values
for col in df.select_dtypes(include=np.number).columns:
    df[col] = df[col].fillna(df[col].median())

for col in df.select_dtypes(include="object").columns:
    if df[col].notna().any():
        df[col] = df[col].fillna(df[col].mode()[0])

print("\n----- MISSING VALUES AFTER CLEANING -----")
print(df.isnull().sum())

# 5. Summary Statistics
print("\n----- NUMERICAL SUMMARY STATISTICS -----")
print(df.describe())

print("\n----- CATEGORICAL SUMMARY STATISTICS -----")
print(df.describe(include="object"))

# 6. NumPy Statistical Calculations
print("\n----- NUMPY STATISTICS -----")

print("Average Monthly Charges:",
      np.mean(df["MonthlyCharges"]))

print("Median Monthly Charges:",
      np.median(df["MonthlyCharges"]))

print("Standard Deviation:",
      np.std(df["MonthlyCharges"]))

print("Average Customer Tenure:",
      np.mean(df["tenure"]))

# 7. Customer Churn Analysis
print("\n----- CUSTOMER CHURN COUNT -----")
print(df["Churn"].value_counts())

print("\n----- CUSTOMER CHURN PERCENTAGE -----")
print(df["Churn"].value_counts(normalize=True) * 100)

# 8. Churn Based on Contract
print("\n----- CHURN BASED ON CONTRACT -----")
print(pd.crosstab(df["Contract"], df["Churn"]))

# 9. Churn Based on Internet Service
print("\n----- CHURN BASED ON INTERNET SERVICE -----")
print(pd.crosstab(df["InternetService"], df["Churn"]))

# 10. Data Visualization

# Graph 1: Customer Churn Distribution
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="Churn")
plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.show()

# Graph 2: Churn Based on Gender
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="gender", hue="Churn")
plt.title("Customer Churn Based on Gender")
plt.show()

# Graph 3: Churn Based on Contract Type
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Contract", hue="Churn")
plt.title("Customer Churn Based on Contract Type")
plt.xticks(rotation=20)
plt.show()

# Graph 4: Monthly Charges Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["MonthlyCharges"], bins=30, kde=True)
plt.title("Monthly Charges Distribution")
plt.xlabel("Monthly Charges")
plt.ylabel("Frequency")
plt.show()

# Graph 5: Tenure vs Churn
plt.figure(figsize=(7, 5))
sns.boxplot(data=df, x="Churn", y="tenure")
plt.title("Customer Tenure vs Churn")
plt.show()

# Graph 6: Correlation Heatmap
numeric_df = df.select_dtypes(include=np.number)
correlation = numeric_df.corr()

plt.figure(figsize=(10, 6))
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# 11. Final Results
print("\n----- FINAL EDA RESULTS -----")
print("Total Customers:", len(df))
print("Total Churned Customers:",
      (df["Churn"] == "Yes").sum())
print("Total Retained Customers:",
      (df["Churn"] == "No").sum())

print("\nEDA COMPLETED SUCCESSFULLY!")
