#%%
import pandas as pd
df = pd.read_csv('survey2017.csv')
df.head(5)

#%%
df['HaveWorkedLanguage']

#%%
languages = df['HaveWorkedLanguage'].str.split(';', expand=True)
languages.head(5)

#%%
summary = languages.apply(pd.Series.value_counts)
summary.head(10)

#%%
summary = pd.DataFrame({'count': summary.sum(axis=1).groupby(lambda x: x.strip()).sum()})
summary

#%%
total = df[df['HaveWorkedLanguage'].notnull()].shape[0]
summary['percent'] = summary['count']/total*100
summary
