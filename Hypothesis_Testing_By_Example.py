
#### Question 1 ########
########################
'''
The population proportion of Ireland having heart disease is 42%.
Are more people suffering from heart disease in the US”?
============================================================

 '''
 
import pandas as pd
 
heart=pd.read_table('heart.csv',sep=',')

'''
Ho: p = 0.42  #null hypothesis
H1: p > 0.42  #alternative hypothesis
'''

p_us=len(heart[heart['target']==0])/  len(heart['target'])

'''
population proportion having heart disease in the US is 46%

'''
from statsmodels.stats.proportion import proportions_ztest


stat, p_value = proportions_ztest(count=len(heart[heart['target']==0]), 
                                  nobs=len(heart['target']), value=0.42, alternative='larger')
