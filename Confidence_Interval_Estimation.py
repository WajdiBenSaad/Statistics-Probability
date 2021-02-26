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

'''
CI for the Difference in Population Proportion
===============================================
Is the population proportion of females with heart disease 
the same as the population proportion of males with heart disease? 
If they are the same, then the difference in both 
the population proportions will be zero.

==>
We will calculate a confidence interval of the difference 
in the population proportion of females and males with heart disease.
'''


p_male = 114/(114+93)  #male population proportion
n = 114+93             #total male population

#Calculate the standard error for the male population proportion
se_male = np.sqrt(p_male * (1 - p_male) / n)

#calculate the difference in the standard error of male and female population with heart disease
se_diff = np.sqrt(se_female**2 + se_male**2)

'''
Use this standard error to calculate the difference 
in the population proportion of males and females with heart disease 
and construct the CI of the difference.
'''
d = 0.55 - 0.24
lcb = d - 1.96 * se_diff  #lower limit of the CI
ucb = d + 1.96 * se_diff  #upper limit of the CI

# ==> our CI is [0.2 , 0.41]
'''
The CI is 0.18 and 0.4. This range does not have 0 in it. 
Both the numbers are above zero.
We cannot make any conclusion that the population proportion 
of females with heart disease is the same as the population 
proportion of males with heart disease. 
If the CI would be -0.12 and 0.1, we could say that the male and 
female population proportion with heart disease is the same.
'''


'''
Calculation of CI of mean
calculate the confidence interval of the mean cholesterol 
level of the female population
==========================
Let’s find the mean, standard deviation, and population size 
for the female population
'''


h.groupby("sex").agg({"chol": [np.mean, np.std, np.size]})

mean_fe = 261.75  #mean cholesterol of female
sd = 64.9         #standard deviation for female population
n = 97            #Total number of female
z = 1.96          #z-score from the z table mentioned before

#Here 1.96 is the z-score for a 95% confidence level.
#Calculate the standard error using the formula 
#for the standard error of the mean

se = sd /np.sqrt(n)

#Construct the CI

lcb = mean_fe - z* se  #lower limit of the CI
ucb = mean_fe + z* se  #upper limit of the CI
(lcb, ucb)
'''
The CI came out to be 248.83 and 274.67.
That means the true mean of the cholesterol of the female population
will fall between 248.83 and 274.67



'''
