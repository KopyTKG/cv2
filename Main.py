import numpy as np
import pandas as pd
from scipy.stats import variation 
from plotnine.data import economics
from plotnine import *

# Coefficient = variation
# Standard deviation = np.std
# Variance = np.var

# Loading csv into dataFrame
df = pd.read_csv("prij.csv")


SS3 = np.std(np.array(df['ss3']))
SS2 = np.std(np.array(df['ss2']))

print(SS3)
print(SS2)

print(SS3 > SS2)
print(SS3 < SS2)


# GGplot rendering
a = (ggplot(df, aes("Obor","celprij")))+ geom_point()

print(a)
