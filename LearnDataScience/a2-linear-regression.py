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
remove_percent_converter = lambda x: float(x.replace('%', ''))
clean_df = pd.read_csv('../datasets/loansData.csv'
	, converters={'Interest.Rate': remove_percent_converter
	,'Debt.To.Income.Ratio': remove_percent_converter})
clean_df['Interest.Rate'].head()
clean_df['Debt.To.Income.Ratio'].head()

#clean loan length
#check if all rows contains %
df[df['Loan.Length'].str.contains('months') == False].head()
remove_month_converter = lambda x: float(x.replace('months', ''))
clean_df = pd.read_csv('../datasets/loansData.csv'
	, converters={'Interest.Rate': remove_percent_converter
	,'Debt.To.Income.Ratio': remove_percent_converter
	, 'Loan.Length': remove_month_converter})
clean_df['Loan.Length'].head()



#add FICO.Score column, use lower limit
len(df[ ( df['FICO.Range'].str.contains('-') == False) ] )
fico_function = lambda x: float(x.split('-')[0])
clean_df = pd.read_csv('../datasets/loansData.csv'
	, converters={'Interest.Rate': remove_percent_converter
	,'Debt.To.Income.Ratio': remove_percent_converter
	, 'Loan.Length': remove_month_converter})
clean_df['FICO.Score'] = clean_df['FICO.Range'].map(fico_function)


#finalize the result

#rename column
#clean_df = clean_df.rename(columns={'Amount.Funded.By.Investors':'Loan.Amount'})
clean_df = clean_df.rename(columns={'Amount.Requested':'Loan.Amount'})

#create a new index column
#clean_df['NewIndex'] = pd.Series(range(1, clean_df['Amount.Requested'].count()+1), index=clean_df.index)
clean_df['NewIndex'] = pd.Series(range(1, clean_df['Amount.Funded.By.Investors'].count()+1), index=clean_df.index)
#resign index
clean_df = clean_df.set_index('NewIndex')


#filter columns
final_columns = ["Interest.Rate","FICO.Score","Loan.Length","Monthly.Income","Loan.Amount"]
final_df = clean_df[final_columns]

#### Remove extremes (strange monthly income)
final_df = final_df[final_df['Monthly.Income'] < 100000]

#final_df.head()
#final_df.to_csv('../datasets/loansData_cleaned.csv')


### Get the expected rCheck if the result downloaded is the same as us
checking_df = pd.read_csv('https://cdn.rawgit.com/benedict-chan/pytest/master/datasets/loanf.csv')
checking_df = checking_df.sort_index()
checking_df.index.name = 'NewIndex'
#checking_df.to_csv('../datasets/loanf_sorted.csv')



#ne_stacked = (final_df != checking_df).stack()

#it looks like a magic!
ne_stacked = pd.concat([final_df, checking_df])
ne_stacked = ne_stacked.reset_index(drop=True)

df_gpby = ne_stacked.groupby(list(ne_stacked.columns))

idx = [x[0] for x in df_gpby.groups.values() if len(x) == 1]

ne_stacked.reindex(idx)