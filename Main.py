import numpy as np
import pandas as pd
import scipy as sc
from plotnine.data import economics
from plotnine import *

# Coefficient = sc.stats.variation
# Z score = sc.stats.zscore
# Standard deviation = np.std
# Variance = np.var

# Loading csv into dataFrame
df = pd.read_csv("prij.csv")


SS3 = np.std(np.array(df['ss3']))
SS2 = np.std(np.array(df['ss2']))

Z =  sc.stats.zscore(df['ss3'])


print(SS3)
print(SS2)

print(SS3 > SS2)
print(SS3 < SS2)

print(Z)

# GGplot rendering
a = (ggplot(df, aes("Obor","celprij")))+ geom_point()

print(a)
