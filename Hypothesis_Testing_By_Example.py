
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

#### Question 2 ########
########################
'''
test if the population proportion of females with heart disease is different 
from the population proportion of males with heart disease.
============================================================

we're going to test the difference of proportion in two populations
our hypothesis to be checked are:
    
 h0:   p_male = p_female
 ha:   p_male <> p_female

We will use a 2-sample z-test to check if the sample allows us to accept or reject the null hypothesis

'''

# spliting the data to 2 dataframes:
    
females=heart.loc[heart['sex']==1, ['target']]

males=heart.loc[heart['sex']==0,['target']]

## calculating the proportions of each group:
    
p_female= len(females[females['target']==1])/len(females)

p_male= len(males[males['target']==1])/len(males)


gender_test=pd.DataFrame( {
    'count':[males['target'].sum(), females['target'].sum()],
    'nobs':[males['target'].count(), females['target'].count()]
    }
    ,index=['males','females']
    )

proportions_ztest(gender_test['count'], gender_test['nobs'])

'''
the p value of our test is: 1.0071642033238824e-06, we can't reject the null hypothesis
The population proportion of males with heart disease is not significantly different than
the population proportion of females with heart disease.


'''
