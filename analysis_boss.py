import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset

# Step 1: Load the dataset
try:
    df = pd.read_csv('boss.csv')  # Example dataset file
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("Error: File not found. Please check the file path.")

# Step 2: Display the first few rows
print("\nFirst few rows of the dataset:")
print(df.head())

# Step 3: Explore the structure of the dataset (data types and missing values)
print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

# Step 4: Clean the dataset (drop rows with missing values as an example)
df_clean = df.dropna()

# Check if missing values are handled
print("\nMissing Values After Cleaning:")
print(df_clean.isnull().sum())

# Task 2: Basic Data Analysis

# Step 1: Compute basic statistics of numerical columns
print("\nBasic Statistics of Numerical Columns:")
print(df_clean.describe())

# Step 2: Perform groupings by a categorical column and compute the mean for each group
# Example: Group by 'Department' and compute the mean of 'Revenue'
if 'Department' in df_clean.columns and 'Revenue' in df_clean.columns:
    grouped_data = df_clean.groupby('Department')['Revenue'].mean()
    print("\nMean Revenue by Department:")
    print(grouped_data)

# Task 3: Data Visualization

# Step 1: Line chart showing trends over time
if 'Date' in df_clean.columns:
    df_clean['Date'] = pd.to_datetime(df_clean['Date'])  # Convert to datetime
    df_clean.set_index('Date', inplace=True)

    plt.figure(figsize=(10, 6))
    df_clean['Revenue'].plot(kind='line', marker='o')
    plt.title('Revenue Trends Over Time')
    plt.xlabel('Date')
    plt.ylabel('Revenue')
    plt.grid()
    plt.show()

# Step 2: Bar chart comparing Revenue across Departments
if 'Department' in df_clean.columns and 'Revenue' in df_clean.columns:
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Department', y='Revenue', data=df_clean, palette='viridis')
    plt.title('Average Revenue by Department')
    plt.xlabel('Department')
    plt.ylabel('Average Revenue')
    plt.xticks(rotation=45)
    plt.show()

# Step 3: Histogram of Profit distribution
if 'Profit' in df_clean.columns:
    plt.figure(figsize=(10, 6))
    sns.histplot(df_clean['Profit'], bins=20, kde=True, color='blue')
    plt.title('Distribution of Profit')
    plt.xlabel('Profit')
    plt.ylabel('Frequency')
    plt.grid()
    plt.show()

# Step 4: Scatter plot showing the relationship between Revenue and Expenses
if 'Revenue' in df_clean.columns and 'Expenses' in df_clean.columns:
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Revenue', y='Expenses', data=df_clean, color='red', alpha=0.6)
    plt.title('Relationship Between Revenue and Expenses')
    plt.xlabel('Revenue')
    plt.ylabel('Expenses')
    plt.grid()
    plt.show()
