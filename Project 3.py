import pandas as pd
file_path = '/Users/nakuldas/Documents/Project 3/housing_data.csv'
df = pd.read_csv(file_path)
print(df.head())

print(df.info())

print(df.describe())

print(df.isnull().sum())

df = df.drop_duplicates()

import seaborn as sns
import matplotlib.pyplot as plt


sns.histplot(df['SalePrice'], kde=True)
plt.title('Distribution of Sale Price')
plt.show()


sns.countplot(x='OverallQual', data=df)
plt.title('Count of Overall Quality Ratings')
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt


correlation_matrix = df[['SalePrice', 'GrLivArea']].corr()
print(correlation_matrix)


sns.scatterplot(x='GrLivArea', y='SalePrice', data=df)
plt.title('Sale Price vs. Living Area')
plt.xlabel('Living Area (sqft)')
plt.ylabel('Sale Price')
plt.show()


sns.regplot(x='GrLivArea', y='SalePrice', data=df)
plt.title('Linear Regression: Sale Price vs. Living Area')
plt.xlabel('Living Area (sqft)')
plt.ylabel('Sale Price')
plt.show()

df['PricePerSqft'] = df['SalePrice'] / df['GrLivArea']  # Price per Square Foot:

df['Age'] = df['YrSold'] - df['YearBuilt']  # Age of the House:

df['TotalSqft'] = df['GrLivArea'] + df['TotalBsmtSF'] + df['GarageArea']  # Total Square Footage:

df['Renovated'] = df['YearRemodAdd'] != df['YearBuilt']  # df['Renovated'] = df['YearRemodAdd'] != df['YearBuilt']


import seaborn as sns
import matplotlib.pyplot as plt


corr_matrix = df[['SalePrice', 'GrLivArea', 'BedroomAbvGr', 'FullBath']].corr()


sns.heatmap(corr_matrix, annot=True)
plt.title('Correlation Matrix')
plt.show()

sns.scatterplot(x='GrLivArea', y='SalePrice', data=df)
plt.title('Sale Price vs. Living Area')
plt.xlabel('Living Area (sqft)')
plt.ylabel('Sale Price')
plt.show()

import statsmodels.api as sm

X = df[['GrLivArea', 'BedroomAbvGr', 'FullBath']]
y = df['SalePrice']

X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
print(model.summary())

import matplotlib.pyplot as plt
import seaborn as sns


df_grouped = df.groupby('YearBuilt')['SalePrice'].mean().reset_index()

plt.figure(figsize=(12, 6))
sns.lineplot(x='YearBuilt', y='SalePrice', data=df_grouped)
plt.title('Average Sale Price by Year Built')
plt.xlabel('Year Built')
plt.ylabel('Average Sale Price')
plt.show()


df['Index'] = range(1, len(df) + 1)


plt.figure(figsize=(12, 6))
sns.lineplot(x='Index', y='SalePrice', data=df)
plt.title('House Price Trend Over Time (Sequential Index)')
plt.xlabel('Index')
plt.ylabel('Sale Price')
plt.show()


import seaborn as sns
import matplotlib.pyplot as plt




corr_matrix = df[['SalePrice', 'PoolArea', 'GarageArea', 'BedroomAbvGr', 'FullBath']].corr()
sns.heatmap(corr_matrix, annot=True)
plt.title('Correlation Matrix')
plt.show()


sns.scatterplot(x='GrLivArea', y='SalePrice', hue='PoolArea', data=df)
plt.title('Sale Price vs. Living Area, Colored by Pool Area')
plt.xlabel('Living Area (sqft)')
plt.ylabel('Sale Price')
plt.show()


import statsmodels.api as sm

X = df[['GrLivArea', 'BedroomAbvGr', 'FullBath', 'PoolArea', 'GarageArea']]
y = df['SalePrice']

X = sm.add_constant(X)  # Add a constant term
model = sm.OLS(y, X).fit()
print(model.summary())