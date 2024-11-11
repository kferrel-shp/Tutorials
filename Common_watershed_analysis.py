# In this tutorial I am attempting to figure out how many common watersheds are subjected to urban development in every
# decade, during the years: 2030, 2060 and 2100.
#
# So this code will figure out what watersheds have a value of urban development greater than or equal to 1 for each
# of these decades

# for example:
#                 watershed     2030     2060     2100
#                     1          0         2        2
#                     2          0         0        1
#                     3          1         4        5
#                     4          0         0        0

# In the above example, there is only one common watershed that has development across all three time frames, which is
# watershed 3.

# Since my data has a wide arrangement of values like the example above, automating this process is a lot easier.

# I will upload my data into this repository named "Common_watershed_analysis.xlsx" if you would like to run this
# and see it for yourself. It would probably be easier that way. You can also edit it and see how things change.


# Good luck :)


# import, we'll be using pandas for this
import pandas as pd

#                                               step 1, Load the Excel file
file_path = 'D:\\Research_and_work_v2\\Excel_files\\Common_watershed_analysis.xlsx'  # path to my data, update for your
#personal pathway when you downloaded the data
df = pd.read_excel(file_path, sheet_name='Low')  # dataframe, sheet 1 has low scenarios
df2 = pd.read_excel(file_path, sheet_name='High')  # dataframe2, sheet 2 has high scenarios




#                                 step 2, check each column that has a common watershed name and value >=1

low_scenario_2030 = df[df['2030d'] >= 1]['watershed']  # in 2030, how many watersheds have a value >=1?
low_scenario_2060 = df[df['2060d'] >= 1]['watershed']  # in 2060, how many watersheds have a value >=1?
low_scenario_2100 = df[df['2100d'] >= 1]['watershed']  # you get the idea

high_scenario_2030 = df2[df2['2030d'] >= 1]['watershed']
high_scenario_2060 = df2[df2['2060d'] >= 1]['watershed']
high_scenario_2100 = df2[df2['2100d'] >= 1]['watershed']



#                                 step 3, find common watersheds across the years for each dataframe

# here the code essentially says "hey find the watersheds that have development across all the years and count them
common_low_scenario = set(low_scenario_2030).intersection(low_scenario_2060, low_scenario_2100)
common_high_scenario = set(high_scenario_2030).intersection(high_scenario_2060, high_scenario_2100)




#                               step 4, show our results

# just simple print functions
print(f"Common watersheds in Low scenario for 2030, 2060, and 2100: {len(common_low_scenario)}")
print(f"Common watersheds in High scenario for 2030, 2060, and 2100: {len(common_high_scenario)}")
