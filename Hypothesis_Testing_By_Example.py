
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

#### Question 3 ########
########################
'''
Check if the mean RestBP is great than 135.
============================================================

So here we are going to test the mean against a known value.
our hypothesis should be:
    h0: m=135
    ha: m>153

this is a one-sided t-test. we need to confirm its hypothesis first:
   1- The sample should be a simple random sample.
   2- The data need to be normally distributed.

'''
import seaborn as sns
from scipy import stats


sns.distplot(heart['trestbps'])
## let's test the normality with shapiro test
stats.shapiro(heart['trestbps'])

#pvalue of the test is not significant


m=heart['trestbps'].mean()


'''
In scipy there is no direct way to indicate that we want to run 
a one-tailed variant of the test. 
However, to obtain the desired results we adjust the output ourselves. 
In the case of this setting, we simply need to divide the p-value by 2 
(the test statistic stays the same).

'''
from scipy import stats



t_test = stats.ttest_1samp(heart['trestbps'], 135)

## one sided t-test's p-value is:
p_val=t_test.pvalue/2    

'''

There is only a 0.05% probability that we will see the observed result is true when the null hypothesis is true.
So, we reject the null hypothesis and accept the alternative hypothesis 
based on this sample data.
'''


#### Question 4 ########
########################
'''
Hypothesis Testing for the Difference in Mean
test if there is any difference between the mean RestBP of females 
to the mean RestBP of males
============================================================
our hypothesis should be:
    
    h0: m_males = m_females
    ha: m_males <> m_females

This is a 2 sample t-test:
    
'''
females_=heart.loc[heart['sex']==1,['trestbps']]
males_=heart.loc[heart['sex']==0,['trestbps']]

t, p = stats.ttest_ind(females_, males_, equal_var=False)

'''
there is approximately 35% probability that the observed result or more extreme is true when the null hypothesis is true.

In another way, the p-value is much bigger than the significance level. 
So, we fail to reject the null hypothesis.

'''
