# Test scripts from A1 of https://github.com/nborwankar/LearnDataScience

import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
# we have to clean up the raw data set which we will do
# in the next lesson. But for now let's look at the cleaned up data.
# import the cleaned up dataset into a pandas data frame
df = pd.read_csv('../datasets/loanf.csv')

# extract FICO Score and Interest Rate and plot them
# FICO Score on x-axis, Interest Rate on y-axis
i_rate = df['Interest.Rate']
fico = df['FICO.Score']
the_plot = plt.plot(fico,i_rate,'o')
ax = plt.gca() #get current axes handle of the plot

xt = ax.set_xlabel('FICO Score')
yt = ax.set_ylabel('Interest Rate %')
