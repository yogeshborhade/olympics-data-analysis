# --------------
#Task 1 - Data Loading
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data=pd.read_csv(path)
data.rename(columns={'Total': 'Total_Medals'}, inplace=True)
print(data.head(10))

#Task 2 - Summer or Winter
#Code starts here




data['Better_Event']=np.where(data['Total_Summer']>data['Total_Winter'],'Summer','Winter')
data['Better_Event'] =np.where(data['Total_Summer'] ==data['Total_Winter'],'Both',data['Better_Event'])
better_event=data['Better_Event'].value_counts().idxmax()
print(better_event)

#Task 3 - Top10
#Code starts here





top_countries=data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]
#print(top_countries.tail(5))
top_countries.drop([146],axis=0, inplace = True) 
#d.iloc[:3]
#print(top_countries.tail(5))
def top_ten(df,col):
    country_list=[]
    top_10=df.nlargest(10,col)
    country_list=list(top_10['Country_Name'])
    #country_list= list((data.nlargest(10,Col)['Country_Name']))
    return country_list#top_10

top_10_summer=top_ten(top_countries,'Total_Summer')
top_10_winter=top_ten(top_countries,'Total_Winter')
top_10=top_ten(top_countries,'Total_Medals')
#define common function to find common element
print(type(top_10_summer))
def common_elements(list1, list2):
    return list(set(list1) & set(list2))
#set1 = top_10_summer.intersection(top_10_winter)  
common=common_elements(top_10_summer,top_10_winter)
common=common_elements(common,top_10)
print(common)


#Task 4 - Plotting Top 10
#Code starts here
print((top_10_summer))



summer_df=data[data['Country_Name'].isin(top_10_summer)]
winter_df=data[data['Country_Name'].isin(top_10_winter)]
top_df=data[data['Country_Name'].isin(top_10)]
summer_df.plot('Country_Name','Total_Summer',kind='bar')
winter_df.plot('Country_Name','Total_Summer',kind='bar')
top_df.plot('Country_Name','Total_Summer',kind='bar')
plt.xlabel('Country')
plt.ylabel('Total Medats')
plt.legend(labels=['Summer', 'Winter2','Total'])

#Task 5 - Top performing country(Gold) 
#Code starts here




summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio=max(summer_df['Golden_Ratio'])
print(summer_max_ratio)
summer_country_gold=summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']
print(summer_country_gold)

winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio=max(winter_df['Golden_Ratio'])
print(winter_max_ratio)
winter_country_gold=winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']
print(winter_country_gold)

top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio=max(top_df['Golden_Ratio'])
print(top_max_ratio)
top_country_gold=top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']
print(top_country_gold)
#Code starts here
data_1=data[:-1]



data_1['Total_Points']=data_1['Gold_Total']*3+data_1['Silver_Total']*2+data_1['Bronze_Total']*1
print(data_1['Total_Points'].head(5))
most_points=max(data_1['Total_Points'])
best_country=data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']
print(most_points)
print(best_country)
best=data[data['Country_Name']==best_country]
best=best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar(stacked=True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)


