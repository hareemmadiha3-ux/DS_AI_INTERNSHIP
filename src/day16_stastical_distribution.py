# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 11:55:47 2026

@author: Madiha
"""
#Task 1
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

# Generate datasets
heights = np.random.normal(loc=170, scale=10, size=1000)          # Normal
income = np.random.exponential(scale=50000, size=1000)           # Right-skewed
scores = np.random.beta(a=5, b=1, size=1000) * 100               # Left-skewed

# Create subplots
plt.figure(figsize=(18, 5))

# Plot 1: Normal Distribution
plt.subplot(1, 3, 1)
sns.histplot(heights, kde=True)
plt.title("Human Heights (Normal)")
plt.axvline(np.mean(heights), linestyle='--', label='Mean')
plt.axvline(np.median(heights), linestyle='-', label='Median')
plt.legend()

# Plot 2: Right-Skewed
plt.subplot(1, 3, 2)
sns.histplot(income, kde=True)
plt.title("Household Income (Right-Skewed)")
plt.axvline(np.mean(income), linestyle='--', label='Mean')
plt.axvline(np.median(income), linestyle='-', label='Median')
plt.legend()

# Plot 3: Left-Skewed
plt.subplot(1, 3, 3)
sns.histplot(scores, kde=True)
plt.title("Easy Exam Scores (Left-Skewed)")
plt.axvline(np.mean(scores), linestyle='--', label='Mean')
plt.axvline(np.median(scores), linestyle='-', label='Median')
plt.legend()

plt.tight_layout()
plt.show()


#Task 2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

heights = np.random.normal(loc=170, scale=10, size=1000)
df = pd.DataFrame({"height": heights})

mu = df["height"].mean()
sigma = df["height"].std()

df["z_score"] = (df["height"] - mu) / sigma
outliers = df[np.abs(df["z_score"]) > 3]

plt.figure(figsize=(10,6))
plt.scatter(df.index, df["height"])
plt.scatter(outliers.index, outliers["height"])
plt.axhline(mu, linestyle="--")
plt.title("Z-Score Outlier Detection (|Z| > 3)")
plt.xlabel("Index")
plt.ylabel("Height")
plt.show()



#Task 3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

# Step 1: Create a heavily right-skewed dataset (Income-like)
population = np.random.exponential(scale=50000, size=100000)

# Step 2: Take 1000 samples of size 30 and compute means
sample_means = []

for i in range(1000):
    sample = np.random.choice(population, size=30)
    sample_means.append(np.mean(sample))

sample_means = np.array(sample_means)

# Step 3: Plot Original Distribution vs Sample Means
plt.figure(figsize=(14,5))

# Original skewed population
plt.subplot(1,2,1)
sns.histplot(population, bins=50, kde=True)
plt.title("Original Population (Right-Skewed)")

# Distribution of sample means
plt.subplot(1,2,2)
sns.histplot(sample_means, bins=30, kde=True)
plt.title("Distribution of Sample Means (n=30)")

plt.tight_layout()
plt.show()
