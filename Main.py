import numpy as np
import pandas as pd
import scipy as sc
from plotnine.data import economics
from plotnine import *
from plotnine import save_as_pdf_pages

# Coefficient = sc.stats.variation
# Z score = sc.stats.zscore
# Standard deviation = np.std
# Variance = np.var

# Loading csv into dataFrame
df = pd.read_csv("Policie.csv")


# SS3 = np.std(np.array(df['ss3']))
# SS2 = np.std(np.array(df['ss2']))
# 
# Z =  sc.stats.zscore(df['ss3'])


#print(SS3)
#print(SS2)

#print(SS3 > SS2)
#print(SS3 < SS2)

#print(Z)

react = pd.DataFrame(df, columns=['react'])
# GGplot rendering
Total = (ggplot(react, aes(x='react'))) + geom_histogram(binwidth=0.1, fill='lightblue', color='black') + labs(title='Reaction', x='Reaction time', y='Abs Count') 

Heigh_React = (ggplot(df, aes(x='react', y='height'))) + geom_line() + labs(title='Reaction for Height', x='Reaction time', y='Height')

Height= (ggplot(df, aes(x='height'))) + geom_histogram(binwidth=10, fill='lightblue', color='black') + labs(title='Height', x='Height', y='Abs Count')

select = 'weight'

height = pd.DataFrame(df, columns=[select])

Boxplot = (
    ggplot(height, aes(x=select, y=select)) + 
    geom_boxplot(color='black', fill='lightblue') +
    labs(title='Pulse', x='', y='Pulse')
)

Histogramp = (
    ggplot(height, aes(x=select)) +
    geom_histogram(bins=5, binwidth=5, fill='pink', color='black') +
    labs(title=select, x='Abs', y=select)
)

Variability = np.var(height)
Standard = np.std(height)
Median = np.median(height)
Mode = sc.stats.mode(height)
Mean = np.mean(height)
Min = np.min(height)
Max = np.max(height)
Kurt = sc.stats.kurtosis(height)
Skew = sc.stats.skew(height)
Q1 = np.percentile(height, 25)
Q3 = np.percentile(height, 75)
IQR = Q3 - Q1

A=72
h= 5
d0 = 4
d1 = 3

print(A+h*((d0)/(d0+d1)))

print("Variability:", Variability.item())
print("Standard Deviation:", Standard.item())
print("Median:", Median)
print("Mode:", Mode[0])
print("Mean:", Mean)
print("Minimum:", Min)
print("Maximum:", Max)
print("Kurtosis:", Kurt[0])
print("Skewness:", Skew[0])
print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)


# print(Boxplot)
print(Histogramp)

#save_as_pdf_pages([Total, Heigh_React, Height, HeightBoxplot], 'react.pdf')



