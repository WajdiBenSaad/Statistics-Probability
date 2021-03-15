from sklearn import datasets
import pandas as pd 


iris = datasets.load_iris()
species = iris.target
names = iris.feature_names

iris_df=pd.DataFrame(iris.data, columns=names)
iris_df["species"]=iris.target
iris_df['species'] = iris_df['species'].apply(lambda x: iris.target_names[x])

iris_df.columns=['sepal_length','sepal_width','petal_length','petal_width','species']
#### stat desc:

iris_df.describe()

iris_df.groupby("species")['sepal_width'].describe()

"""
Testing :
Q1. Is the mean sepal length different between setosa and versicolor ?

using T-test,Student’s t-test

-Null hypothesis (H0): u1 = u2
which translates to the mean of sample 1 is equal to the mean of sample 2
-Alternative hypothesis (H1): u1 ≠ u2
which translates to the mean of sample 1 is not equal to the mean of sample 2

If the p-value is less than what is tested at, 
most commonly 0.05, one can reject the null hypothesis.


### INDEPENDENT T-TEST ASSUMPTIONS

1-The independent variable (IV) is categorical with at least two levels (groups)

2-The dependent variable (DV) is continuous which is measured on an interval or ratio scale

3-The distribution of the two groups should follow the normal distribution

4- The variances between the two groups are equal

This can be tested using statistical tests including Levene’s test, F-test, and Bartlett’s test.

"""




'''
To make the code in the next steps a bit cleaner to read, 
I will create 2 data frames that are subsets of the original 
data where each data frame only contains data for a respective flower species.
'''
setosa=iris_df[iris_df['species']=='setosa']
versicolor=iris_df[iris_df['species']=='versicolor']
virginica=iris_df[iris_df['species']=='virginica']

'''
Before the t-test can be conducted, one needs to test the assumptions. 
First to test for the homogeneity of variances. (hyp Nb 4 )
To do this, I will use Levene’s test for homogeneity of variance. 
The method to conduct this test is stats.levene().
'''
from scipy import stats
#import matplotlib.pyplot as plt


stats.levene(setosa['sepal_width'], versicolor['sepal_width'])
''' 
Output:

LeveneResult(statistic=0.591002044989776, pvalue=0.44388064024686147)

==> p value is very high and the test is not significant:
there is homogeneity of variances and we can proceed. 
If the test were to be significant,
a viable alternative would be to conduct a Welch’s t-test.
'''

# Validating the normality of the distrib of the 2 groupes (hyp Nb 3)
stats.shapiro(setosa['petal_length'])
stats.shapiro(versicolor['petal_length'])

'''
ShapiroResult(statistic=0.9549766182899475, pvalue=0.05481043830513954)
ShapiroResult(statistic=0.9660047888755798, pvalue=0.1584833413362503)

Neither of the variables of interest violates the assumption of normality 
so we can continue with our analysis plan. 


Next to testing the assumption of normality. 
This can be done visually with a histogram and/or as a q-q plot, 
and by using the Shapiro-Wilk test which is the stats.shaprio() method.
 First, I will check them visually.

'''

stats.ttest_ind(setosa['sepal_width'], versicolor['sepal_width'])

'''
Ttest_indResult(statistic=9.454975848128596, pvalue=1.8452599454769322e-15)

The Independent t-test results are significant! 
Therefore, one can reject the null hypothesis in support of the alternative.

Another component one needs to report the findings is the degrees of freedom (df). 
This can be calculated by adding the two group Ns and subtracting 2. 
In our case, df = (50 + 50) – 2 = 98.

###################################################
INTERPRETATION OF RESULTS
###################################################

The purpose of the current study was to test if there is a significant difference in the sepal width 
between the floral species Iris-setosa and Iris-versicolor. 
Iris-setosa’s average sepal width (M= 3.418, SD= 0.381) is wider 
and has greater variation than Iris-versicolor (M= 2.770, SD= 0.314). 
Levene’s test for homogeneity of variances indicated equality of variance (F= 0.664, p=0.417); 

therefore an Independent t-test was used. 

Results indicate that there is a significant difference in the sepal width 
between Iris-setosa and Iris-versicolor (t(98)=9.282, p=4.362).


'''

'''
==> Welch’s t-test:
Welch’s t-test is a nonparametric univariate test that tests for 
a significant difference between the mean of two unrelated groups. 
It is an alternative to the independent t-test when there is 
a violation in the assumption of equality of variances.

The hypothesis being tested is:

- Null hypothesis (H0): u1 = u2
which translates to the mean of sample 1 is equal to the mean of sample 2
- Alternative hypothesis (H1): u1 ≠ u2
which translates to the mean of sample 1 is not equal to the mean of sample 2

If the p-value is less than what is tested at, most commonly 0.05, 
one can reject the null hypothesis.

## WELCH’S T-TEST ASSUMPTIONS

1-The independent variable (IV) is categorical with at least two levels (groups)
2-The dependent variable (DV) is continuous which is measured on an interval or ratio scale
3-The distribution of the two groups should follow the normal distribution
4-If any of these assumptions are violated then another test should be used.

## WELCH’S T-TEST:


To conduct a Welch’s t-test, one needs to use the stats.ttest_ind()
 method while passing “False” in the “equal_var=” argument.
'''

stats.ttest_ind(setosa['petal_length'], virginica['petal_length'], equal_var = False)
'''
The p-value is significant, 
therefore one can reject the null hypothesis in support of the alternative.
'''
## Calculate the Degrees of Freedom:

def welch_ttest(x, y): 
    ## Welch-Satterthwaite Degrees of Freedom ##
    dof = (x.var()/x.size + y.var()/y.size)**2 / ((x.var()/x.size)**2 / (x.size-1) + (y.var()/y.size)**2 / (y.size-1))
   
    t, p = stats.ttest_ind(x, y, equal_var = False)
    
    print("\n",
          f"Welch's t-test= {t:.4f}", "\n",
          f"p-value = {p:.4f}", "\n",
          f"Welch-Satterthwaite Degrees of Freedom= {dof:.4f}")

welch_ttest(setosa['petal_length'], virginica['petal_length']) 

