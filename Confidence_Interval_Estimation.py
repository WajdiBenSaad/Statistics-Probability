'''
################################################################################
# Practical examples of Confidence Interval estimation  with python
# Authod : Wajdi Ben Saad       | December 2020.  | V.01
# for citation, please link to my website :
# www.WajdiBenSaad.com 
# Not to be used for commercial purposes.
# Thanks to Google & Stackoverflow for helping to provide the matrials
################################################################################

This code covers some practical aspects of Confidence Interval estimation  using python
It is needless to say that the theoratical understanding of these concepts is crucial.
The code is extremely simplified and split to answer each question individually.
This should not be use as it is in a production context.
More work should be done into making more flexible functions and turned into hypothesis testing pipelines.
Please use this for educational purposes only!!!!

'''


import pandas as pd
'''
How to Calculate the Confidence Interval?
The calculation of the confidence interval involves 
the best estimate which is obtained by the sample and a margin of error. 

'''
heart=pd.read_table('heart.csv',sep=',')

'''
We are going to construct a CI for the female population proportion that has heart disease.

First, replace 1 and 0 with ‘Male’ and ‘Female’ in a new column ‘Sex1’.
'''

heart['Sex1'] = heart.sex.replace({1: "Male", 0: "Female"})

dx = heart[["target", "Sex1"]].dropna()

pd.crosstab(dx.target, dx.Sex1)

'''
The number of females who have heart disease is 24. 
Calculate the female population proportion with heart disease.
'''

prop_females=24/(24+72)

#The prop_females is 0.25. The size of the female population:

n = 72+24


#The size of the female population is 96. Calculate the standard error
import numpy as np
se_female = np.sqrt(prop_females * (1 - prop_females) / n)


# Now construct the CI using the formulas above. 
# The z-score is 1.96 for a 95% confidence interval.

z_score = 1.96
lcb = prop_females - z_score* se_female #lower limit of the CI
ucb = prop_females + z_score* se_female #upper limit of the CI

# ==> the confidence interval is [0.16, 0.33]
# let's calculate it with the prebuilt in function 

import statsmodels.api as sm
sm.stats.proportion_confint(n * prop_females, n)

# ==> same conf interval ! :D
