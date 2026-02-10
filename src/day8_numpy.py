# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 11:40:54 2026

@author: Madiha
"""
import numpy as np

# Create a 5x3 array with random scores between 50 and 100
scores = np.random.randint(50, 101, size=(5, 3))

# Calculate column-wise mean (mean score per subject)
subject_means = scores.mean(axis=0)

# Subtract the mean from each column using broadcasting
centered_scores = scores - subject_means

# Output
print("Original Scores:\n", scores)
print("\nSubject Means:\n", subject_means)
print("\nCentered Scores (Normalized):\n", centered_scores)










import numpy as np

# Create 1D array from 0 to 23
data = np.arange(24)

# Reshape into (4, 3, 2)
reshaped = data.reshape(4, 3, 2)
print("After reshape:", reshaped.shape)

# Transpose to (4, 2, 3)
final_array = reshaped.transpose(0, 2, 1)
print("Final shape after transpose:", final_array.shape)

# Output final array
print("\nFinal array:\n", final_array)


























































































