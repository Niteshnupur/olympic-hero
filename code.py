# --------------
# Data Loading
# Data Loading
# Let's start with the simple task of loading the data and do a little bit of renaming


#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path


# Load the dataframe from the path using pd.read_csv() and store the dataframe in a variable called 'data'.


data = pd.read_csv(path)



# In the dataframe, rename the column Total to Total_Medals

data.rename(columns = {"Total": "Total_Medals"} , inplace=True)

print(data.head(10))


#Code starts here



# --------------
# Summer or Winter
# Summer or Winter
# Some Countries love Summer, some Winter. We think it has to do something with their Olympic performance.

# For this task we will try to figure out which olympic event does a country perform better in.




#Code starts here


# Create a new column Better_Event that stores 'Summer','Winter' or 'Both' based on the comparision between the total medals won in Summer event and Winter event (i.e. comparision between the Total_Summer and Total_Winter columns) using "np.where()"function.


data["Better_Event"] = np.where(data['Total_Summer']>data['Total_Winter'],'Summer',np.where(data['Total_Summer']==data['Total_Winter'],'Both','Winter'))


# Find out which has been a better event with respect to all the performing countries by using value_counts() function and store it in a new variable called 'better_event'.


better_event = data['Better_Event'].value_counts().idxmax()

print(better_event)






# --------------
# Top10
# Top 10
# So we figured out which is a better event for each country. Let's move on to finding out the best performing countries across all events

# In this task we will try to find

# Which are the top 10 performing teams at summer event (with respect to total medals), winter event and overall?
# How many teams are present in all of the three lists above?




# Code starts here


# Create a new dataframe subset called 'top_countries' with the columns ['Country_Name','Total_Summer', 'Total_Winter','Total_Medals'] only


top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]

print(top_countries)

type(top_countries)



# Drop the last row from 'top_countries'(The last row contains the sum of the medals)

top_countries = top_countries[:-1]


# Create a function called 'top_ten' that:

# Takes the dataframe 'top_countries' and a column name as parameters.

# Creates a new empty list called 'country_list'

# Find the top 10 values for that particular column(for e.g. 'Total_Summer') using "nlargest()" function

# From the dataframe returned by nlargest function, slices the Country_Name column and stores it in the 'country_list' list

# Returns the 'country_list'


def top_ten(data,col):
    country_list=[]
    country_list= list((data.nlargest(10,col)['Country_Name']))
    return country_list



# Call the 'top_ten()' function for the three columns :Total_Summer,Total_Winter and Total_Medals and store their respective results in lists called 'top_10_summer', 'top_10_winter' and 'top_10'


top_10_summer = top_ten(top_countries,'Total_Summer')


top_10_winter = top_ten(top_countries,'Total_Winter')


top_10 = top_ten(top_countries,'Total_Medals')



# Create a new list 'common' that stores the common elements between the three lists('top_10_summer', 'top_10_winter' and 'top_10')

common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))





# --------------
# Plotting Top 10
# Plotting Top 10
# From the lists that you have created from the previous task, let's plot the medal count of the top 10 countries for better visualisation


#Code starts here

# Take the three previously created lists(top_10_summer, top_10_winter, top_10)

# Subset the dataframe 'data' based on the country names present in the list top_10_summer using "isin()" function on the column Country_Name. Store the new subsetted dataframes in 'summer_df'. 
# Do the similar operation using top_10_winter and top_10 and store the subset dataframes in 'winter_df' & 'top_df' respectively.


summer_df = data[data['Country_Name'].isin(top_10_summer)]

# for winter_df

winter_df = data[data['Country_Name'].isin(top_10_winter)]

# for top_df

top_df = data[data['Country_Name'].isin(top_10)]

print(summer_df)

print(winter_df)

print(top_df)


# Take each subsetted dataframe and plot a bar graph between the country name and total medal count according to the event 
# (For e.g. for 'summer_df' plot a bar graph between Country_Name and Total_Summer)


# plt.figure(figsize=(20, 6))

plt.figure(figsize=(20,20))

plt.bar(summer_df['Country_Name'], summer_df['Total_Summer'] , facecolor="green" , edgecolor="black")



plt.title('Medal Count Of The Top 10 Countries')

plt.xlabel('Country Name')

plt.ylabel('Total Medals')








# --------------
# Top performing country(Gold)
# Top performing country(Gold)
# Winning silver or bronze medals is a big achievement but winning gold is bigger.

# Using the above created dataframe subsets, in this task let's find out which country has had the best performance with respect to the ratio between gold medals won and total medals won



#Code starts here

# In the dataframe 'summer_df'(created in the previous function) , create a new column Golden_Ratio which is the quotient after dividing the two columns Gold_Summer and Total_Summer.


summer_df["Golden_Ratio"] = summer_df["Gold_Summer"]/summer_df["Total_Summer"]

print(summer_df["Golden_Ratio"])


# Find the max value of Golden_Ratio and the country associated with it and store them in summer_max_ratio and summer_country_gold respectively.

summer_max_ratio = max(summer_df['Golden_Ratio'])

print(summer_max_ratio)


summer_country_gold = summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']

print(summer_country_gold)



# In the dataframe 'winter_df'(created in the previous function) , create a new column Golden_Ratio which is the quotient after dividing the two columns Gold_Winter and Total_Winter


winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']

print(winter_df['Golden_Ratio'])


# Find the max value of Golden_Ratio and the country associated with it and store them in 'winter_max_ratio' and 'winter_country_gold' respectively.


winter_max_ratio = max(winter_df['Golden_Ratio'])

print(winter_max_ratio)


winter_country_gold = winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']

print(winter_country_gold)


# In the dataframe top_df'(created in the previous function) , create a new column Golden_Ratio which is the quotient after dividing the two columns Gold_Total and Total_Medals.


top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']

print(top_df['Golden_Ratio'])


# Find the max value of Golden_Ratio and the country associated with it and store them in top_max_ratio' and 'top_country_gold' respectively.

top_max_ratio = max(top_df['Golden_Ratio'])

print(top_max_ratio)


top_country_gold = top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']

print(top_country_gold)



# --------------
# Best in the world
# Best in the world
# Winning Gold is great but is winning most gold equivalent to being the best overall perfomer? Let's find out.


#Code starts here


# Drop the last row from the dataframe(The last row contains the total of all the values calculated vertically) and save the result in 'data_1'

data_1 = data[:-1]

print(data_1)

# Update the dataframe 'data_1' to include a new column called Total_Points which is a weighted value where each gold medal counts for 3 points, silver medals for 2 points, and bronze medals for 1 point.

# (i.e. You need to take weighted value of Gold_Total, Silver_Total and Bronze_Total)


data_1['Total_Points'] = data_1['Gold_Total']*3+data_1['Silver_Total']*2+data_1['Bronze_Total']

print(data_1['Total_Points'])

# Find the max value of Total_Points in 'data_1' and 
# the country assosciated with it and store it in variables 'most_points' and 'best_country' respectively.

most_points = max(data_1['Total_Points'])

print(most_points)


best_country = data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']

print(best_country)




# --------------
# Plot for the best
# We know which country is best when it comes to winning the most points in Olympic Games. Let's plot the medal count to visualise their success better.


#Code starts here

# Create a single row dataframe called 'best' from 'data' where value of column Country_Name is equal to 'best_country'
# (The variable you created in the previous task)

best = data[data["Country_Name"] == best_country ]

print(best)



# Subset 'best' even further by only including the columns : ['Gold_Total','Silver_Total','Bronze_Total']


best = best[['Gold_Total','Silver_Total','Bronze_Total']]

print(best)


# Create a stacked bar plot of 'best' using "DataFrame.plot.bar()" function

best.plot.bar(stacked=True)


# Name the x-axis as United States using "plt.xlabel()"

plt.xlabel("United States")


# Name the y-axis as Medals Tally using "plt.ylabel()"

plt.ylabel("Medals Tally")


# Rotate the labels of x-axis by 45o using "plt.xticks()"

plt.xticks(rotation=45)





