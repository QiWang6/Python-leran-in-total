# @Time: 2024/11/27 
# @Author: Qi Wang
# @File: test_seaborn
# @Project: Python-leran-in-total
# @Quelle:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df1 = sns.load_dataset("penguins").query('species == "Adelie"')
s1 = df1['bill_length_mm']
sns.histplot(s1)
plt.show()