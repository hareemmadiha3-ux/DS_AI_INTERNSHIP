#Task 1
import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = pd.DataFrame({
    'Transmission' : ['Automatic', 'Manual', 'Automatic', 'Manual'],
    'color' : ['Red', 'Blue','Green', 'Red']
    })

le = LabelEncoder()
data['Transmission'] = le.fit_transform(data['Transmission'])
print(data)

#Task 2
# scaling_demo.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Sample numeric dataset
data = {
    'Age': [18, 22, 25, 30, 35, 40, 45, 50],
    'Salary': [15000, 20000, 25000, 30000, 40000, 50000, 60000, 70000]
}

df = pd.DataFrame(data)

# ----------- Standardization (Mean = 0, Std = 1) -----------
standard_scaler = StandardScaler()
df_standardized = pd.DataFrame(
    standard_scaler.fit_transform(df),
    columns=df.columns
)



# ----------- Normalization (Range 0 to 1) -----------
minmax_scaler = MinMaxScaler()
df_normalized = pd.DataFrame(
    minmax_scaler.fit_transform(df),
    columns=df.columns
)

# ----------- Plot histogram before and after scaling -----------
plt.figure(figsize=(10, 4))

# Before scaling
plt.subplot(1, 2, 1)
plt.hist(df['Salary'], bins=6)
plt.title("Salary - Before Scaling")
plt.xlabel("Salary values")
plt.ylabel("Frequency")

# After standardization
plt.subplot(1, 2, 2)
plt.hist(df_standardized['Salary'], bins=6)
plt.title("Salary - After Standardization")
plt.xlabel("Scaled values")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()
