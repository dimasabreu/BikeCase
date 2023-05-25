import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import glob 

#create a df and read data
df = pd.concat([pd.read_csv(one_filename, 
                            usecols=['ride_id', 
                                     'rideable_type', 
                                     'started_at', 
                                     'ended_at', 
                                     'start_station_name', 
                                     'start_station_id', 
                                     'end_station_name', 
                                     'end_station_id',
                                     'start_lat',
                                     'start_lng',
                                     'end_lat',
                                     'end_lng',
                                     'member_casual'])
    for one_filename in glob.glob('cases/divvy-tripdata*.csv')])

#create a df
df = pd.DataFrame(df)

#drop nulls
df = df.dropna()

#drop duplicates
df = df.drop_duplicates()

#to group rideable by member type
df2 = df.groupby('rideable_type').member_casual.value_counts().unstack().fillna(0)

#to group by started station
df2 = df.groupby('start_station_name').member_casual.value_counts().unstack().fillna(0)

#to group by end station
df2 = df.groupby('start_station_name').member_casual.value_counts().unstack().fillna(0)

#to group by started and ended time
df2 = df.groupby(['started_at', 'ended_at']).member_casual.value_counts().unstack().fillna(0)

#to make rideable_type a index
df2 = df2.reset_index()

#convert started date from string to DATA type
df2['started_at_date'] = pd.to_datetime(df2['started_at'],format='%Y-%m-%d %H:%M:%S')

#convert ended date from string to DATA type
df2['ended_at_date'] = pd.to_datetime(df2['ended_at'],format='%Y-%m-%d %H:%M:%S')

#subtract started date from end date to get the time of the ride.
df2['RideTime'] = (df2['ended_at_date'] - df2['started_at_date'])

#creating a new df
df3 = df2

#drop members from df so we can see only casuals
df3.drop(df3.loc[df3['member']==1.0].index, inplace=True)

#drop started_at_date if it is less or igual ended_at_date
df3.drop(df3.loc[df3['started_at_date'] >= df3['ended_at_date']].index, inplace=True)

#used to get the max value
max_value_index = df3['RideTime'].idxmax()
max_value_index

#used to get the min value
min_value_index = df3['RideTime'].idxmin()
min_value_index

#puting the value inside a df
df4 = df3[df3['RideTime']==df3['RideTime'].min()]

#deleting the value from the main df so we can see the next value
df3 = df3.drop(max_value_index)

#concat 2 df and drop duplicates 
df3 = pd.concat([df3, df4]).drop_duplicates(keep=False)


df2 = df.groupby(['started_at', 'ride_id', 'rideable_type']).member_casual.value_counts().unstack().fillna(0)

df2 = df2.reset_index()

df2.set_index(['started_at', 'ride_id', 'rideable_type', 'member', 'casual'])

df2['started_at_date'] = pd.to_datetime(df2['started_at'],format='%Y-%m-%d %H:%M:%S')

df2['day_names'] = df2['started_at_date'].dt.day_name()

df2 = df2.drop(columns='started_at')

df4 = df2.groupby(['member', 'casual']).day_names.value_counts().unstack().fillna(0)

df4 = df4.reset_index(drop=True)

df4.index = ['Casual', 'Member']

df7 = df4.T

df7 = df7.reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

df7.plot(kind='bar',alpha=0.75, rot=0, fontsize='small')
plt.xlabel("")
plt.show()

df5 = df

df5['started_at_date'] = pd.to_datetime(df5['started_at'],format='%Y-%m-%d %H:%M:%S')

#convert ended date from string to DATA type
df5['ended_at_date'] = pd.to_datetime(df5['ended_at'],format='%Y-%m-%d %H:%M:%S')

df5['month_names'] = df5['started_at_date'].dt.month_name()

df5 = df5.groupby(['started_at', 'ended_at']).member_casual.value_counts().unstack().fillna(0)

df5 = df5.reset_index()

df7 = df5.groupby(['member', 'casual']).month_names.value_counts().unstack().fillna(0)

df7.reset_index()

df6 = df5.groupby(['member', 'casual']).month_names.value_counts().unstack().fillna(0)

df6 = df6.reset_index(drop=True)

df6 = df6.drop([df6.index[1], df6.index[3], df6.index[4] ])

df6.index = ['Casual', 'Member']

df7 = df6.T

df7 = df7.reindex(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

from matplotlib.pyplot import figure

df7.plot(kind='bar',alpha=0.75, rot=0, fontsize='small')
plt.rcParams["figure.figsize"] = (20,5)
plt.xlabel("Months")
plt.show()



