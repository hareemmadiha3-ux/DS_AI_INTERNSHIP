# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 11:29:31 2026

@author: Madiha
"""
#task 1
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Sample dataset
data = {
    "Price": [200000, 220000, 250000, 270000, 300000, 320000, 350000, 400000, 450000, 600000],
    "City": ["Delhi", "Mumbai", "Delhi", "Bangalore", "Mumbai", "Delhi", "Bangalore", "Mumbai", "Delhi", "Delhi"]
}

df = pd.DataFrame(data)

# ---- Histogram with KDE ----
plt.figure(figsize=(12,4))

plt.subplot(1,2,1)
sns.histplot(df["Price"], kde=True)
plt.title("Distribution of House Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")

# ---- Count Plot for Categorical Column ----
plt.subplot(1,2,2)
sns.countplot(x=df["City"])
plt.title("Count of Houses by City")
plt.xlabel("City")
plt.ylabel("Count")

plt.tight_layout()
plt.show()

# ---- Skewness and Kurtosis ----
skewness = df["Price"].skew()
kurtosis = df["Price"].kurt()

print("Skewness:", skewness)
print("Kurtosis:", kurtosis)





#task 2
import matplotlib.pyplot as plt

# Sample data
square_footage = [800, 1000, 1200, 1500, 1800, 2000, 2200, 2500]
price = [200000, 250000, 270000, 320000, 360000, 400000, 420000, 480000]

# Categorical data for boxplot
locations = ['Urban', 'Urban', 'Suburban', 'Suburban', 'Rural', 'Urban', 'Rural', 'Suburban']
price_by_location = {
    'Urban': [200000, 250000, 400000],
    'Suburban': [270000, 320000, 480000],
    'Rural': [360000, 420000]
}

# ----- Scatter Plot -----
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.scatter(square_footage, price)
plt.xlabel("Square Footage")
plt.ylabel("Price")
plt.title("Square Footage vs Price")

# ----- Boxplot -----
plt.subplot(1,2,2)
plt.boxplot(price_by_location.values(), labels=price_by_location.keys())
plt.xlabel("Location")
plt.ylabel("Price")
plt.title("Price Distribution by Location")

plt.tight_layout()
plt.show()


#task 3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset
data = {
    "SquareFootage": [800, 900, 1000, 1200, 1500, 1800, 2000, 2200, 2500, 3000],
    "Bedrooms": [2, 2, 3, 3, 4, 4, 5, 5, 6, 7],
    "Price": [200000, 220000, 250000, 280000, 320000, 360000, 400000, 450000, 500000, 900000],
    "Age": [20, 18, 15, 12, 10, 8, 6, 5, 4, 2]
}

df = pd.DataFrame(data)

# ---- Correlation Matrix ----
corr_matrix = df.corr()

plt.figure(figsize=(6,4))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# ---- Boxplot for Outliers ----
plt.figure(figsize=(4,6))
sns.boxplot(y=df["Price"])
plt.title("Boxplot of House Prices")
plt.ylabel("Price")
plt.show()

# Print correlation values
print(corr_matrix)
