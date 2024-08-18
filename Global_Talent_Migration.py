import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Loading data
industry_migration_data = pd.read_csv('D:\DA_NCI\DAP\Project\industry_migration_public.csv')

#Exploring the data
#Head of the data
print(industry_migration_data.head())

#Information of the data
industry_migration_data.info()

#Dimension of the data
numb_row, numb_col = industry_migration_data.shape
print (f"There are {numb_row} rows and {numb_col} columns")

#Checking for missing values
print(industry_migration_data.isnull().sum())

#Transforming the data
#Dropping the null values
industry_migration_data = industry_migration_data.dropna(axis=1)

#Checking the shape of data after dropping columns
numb_row, numb_col = industry_migration_data.shape
print (f"There are {numb_row} rows and {numb_col} columns left")

#Checking unique values of data
print(industry_migration_data.nunique())

#Checking for duplicate values
print(f"Number of duplicate values: {industry_migration_data.duplicated().sum()}")

#Dropping country_code, isic_section_index and industry_id columns from data as corresponding names are present for it
industry_migration_data = industry_migration_data.drop(['country_code', 'isic_section_index', 'industry_id'], axis=1)

#Creating column for net migration values across all years
#industry_migration_data['net_migration'] = industry_migration_data[['net_per_10K_2015', 'net_per_10K_2016', 'net_per_10K_2017', 'net_per_10K_2018', 'net_per_10K_2019']].sum(axis=1)

top_industry = industry_migration_data.groupby(['industry_name'])[['net_per_10K_2015', 'net_per_10K_2016', 'net_per_10K_2017', 'net_per_10K_2018', 'net_per_10K_2019']].sum()
top_10_industries = top_industry.sort_values(by=['net_per_10K_2015', 'net_per_10K_2016', 'net_per_10K_2017', 'net_per_10K_2018', 'net_per_10K_2019'],ascending=False).head(10)
print(top_10_industries)

for industry in top_10_industries.index:
    plt.figure(figsize=(12,6))
    industry_df = industry_migration_data[industry_migration_data['industry_name'] == industry]
    plt.plot(industry_df.columns[-5:], industry_df.iloc[0,-5:], label=industry)
    plt.title(f"Net migration rates for {industry}")
    plt.xlabel("Industry")
    plt.ylabel("Net migration per 10K people")
    plt.legend()
plt.show()

#Top industries and migration across years
#top_industries = industry_migration_data.groupby('industry_name')['net_migration'].sum().nlargest(10)
#print(top_industries)

# Get the top 10 industries by sum of net migration across all years
#net_migration_top10 = industry_migration_data[industry_migration_data['industry_name'].isin(top_industries)]

#Create bar graph
#ax = top_industries.groupby(['industry_name', 'net_migration'])['net_migration'].sum().unstack().plot(kind='bar', figsize=(8, 5))

# Set chart properties
#ax.set_xlabel('Net Migration')
#ax.set_ylabel('Industry')
#ax.set_title('Top 10 Industries with Highest Net Migration')

# Add legend
#ax.legend(loc='upper right', fontsize='small')

# Show the chart
#plt.show()

#Data Visualisation
#COUNTRY MIGRATION DATA
#Get countries with high income
""" countries_high = industry_migration_data.groupby(['wb_region'])[['net_per_10K_2015', 'net_per_10K_2016', 'net_per_10K_2017', 'net_per_10K_2018', 'net_per_10K_2019']].sum()
country_growth = countries_high.sort_values(by=['net_per_10K_2015', 'net_per_10K_2016', 'net_per_10K_2017', 'net_per_10K_2018', 'net_per_10K_2019'], ascending = False).head(10)
print(country_growth)
plt.figure(figsize=(12,12))
sns.barplot(x='wb_region', y='net_per_10K_2019', data=industry_migration_data, palette='Set1')
plt.xticks(rotation=90)
plt.show() """

#Different industry growth in years
""" data_1 = industry_migration_data.groupby(['industry_name'])[['net_per_10K_2015', 'net_per_10K_2016', 'net_per_10K_2017', 'net_per_10K_2018', 'net_per_10K_2019']].sum()
industry_growth = data_1.sort_values(by=['net_per_10K_2015', 'net_per_10K_2016', 'net_per_10K_2017', 'net_per_10K_2018', 'net_per_10K_2019'], ascending = False).head(10)
print(industry_growth)
fig, ax = plt.subplots(figsize=(16,6))
sns.barplot(x='industry_name', y='net_per_10K_2019', data=industry_migration_data, palette='Set1')
ax.set_xlabel(ax.get_xlabel(), labelpad=15)
ax.set_ylabel(ax.get_ylabel(), labelpad=30)
ax.xaxis.label.set_fontsize(16)
ax.yaxis.label.set_fontsize(16)
plt.xticks(rotation=90)
plt.show() """

#plt.figure(figsize = (12,12))
#plt.title(f"Migrations in Different Countries")
#plt.xlabel("Net Migration per 10,000 People")
#plt.ylabel("Countries")
#sns.countplot(hue = 'wb_income', data = industry_migration_data, palette = 'Blues_r', order = industry_migration_data['country_name'].value_counts().nlargest(10).index)
#plt.show()

#Grouping country names and isic section name
#data_2 = industry_migration_data.groupby(['country_name', 'isic_section_name'])[['net_per_10K_2015', 'net_per_10K_2016', 'net_per_10K_2017', 'net_per_10K_2018', 'net_per_10K_2019']].sum()
#top_10_countries_isic = data_2.sort_values(by=['net_per_10K_2015', 'net_per_10K_2016', 'net_per_10K_2017', 'net_per_10K_2018', 'net_per_10K_2019'], ascending = False).head(10)
#print(top_10_countries_isic)

#Grouping country names and industry name
#data_3 = industry_migration_data.groupby(['country_name', 'industry_name'])[['net_per_10K_2015', 'net_per_10K_2016', 'net_per_10K_2017', 'net_per_10K_2018', 'net_per_10K_2019']].sum()
#top_10_countries_industry = data_3.sort_values(by=['net_per_10K_2015', 'net_per_10K_2016', 'net_per_10K_2017', 'net_per_10K_2018', 'net_per_10K_2019'], ascending = False).head(10)
#print(top_10_countries_industry)

