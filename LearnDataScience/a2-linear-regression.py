# Test scripts from A1 of https://github.com/nborwankar/LearnDataScience

import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
# we have to clean up the raw data set which we will do
# in the next lesson. But for now let's look at the cleaned up data.
# import the cleaned up dataset into a pandas data frame
df = pd.read_csv('../datasets/loansData.csv')

#Inspect the DataFrame
df.dtypes  #check column's datatype
df.describe()  # check information for numeric columns


#cleaning data exercise 
#clean interest rate
#check if all rows contains %
len(df[ ( df['Interest.Rate'].str.contains('%') == False) ] )
interest_rate_converter = lambda x: float(x.replace('%', ''))
clean_df = pd.read_csv('../datasets/loansData.csv'
	, converters={'Interest.Rate': interest_rate_converter
	,'Debt.To.Income.Ratio': interest_rate_converter})
clean_df['Interest.Rate'].head()
clean_df['Debt.To.Income.Ratio'].head()

#clean loan length
#check if all rows contains %
df[df['Loan.Length'].str.contains('months') == False].head()
loan_length_converter = lambda x: float(x.replace('months', ''))
clean_df = pd.read_csv('../datasets/loansData.csv'
	, converters={'Interest.Rate': interest_rate_converter
	,'Debt.To.Income.Ratio': interest_rate_converter
	, 'Loan.Length': loan_length_converter})
clean_df['Loan.Length'].head()
