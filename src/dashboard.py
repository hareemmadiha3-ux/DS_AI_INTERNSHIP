# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 19:09:46 2026

@author: Madiha
"""

import matplotlib.pyplot as plt

plt.subplot(1,2,1)
plt.bar(['Electronics','Clothing','Home'],[300,450,200])
plt.title("Bar chart")
plt.subplot(1,2,2)
plt.plot([1,2,3],[1,4,9])
plt.title("Line plot")
plt.show()