# Part 2: Sets
# rainfall_data = {120, 150, 180, 120, 90, 110, 130}
# (This set represents the rainfall in mm recorded across various districts this week.)


# How many rainfall values are in the set?
# rainfall_data = {120, 150, 180, 120, 90, 110, 130}
# print(len(rainfall_data))


# Can you directly change the value of an item in a set? What output would you get when you try to change the value using its index ?
# rainfall_data = {120, 150, 180, 120, 90, 110, 130}
# rainfall_data[0]=100

# Check if 150 is present inside rainfall_data. (hint: use in keyword and research)
# rainfall_data = {120, 150, 180, 120, 90, 110, 130}
# print(150 in rainfall_data)

# Convert the set to a list 
# rainfall_data = {120, 150, 180, 120, 90, 110, 130}
# rainfall_list=list(rainfall_data)
# print(rainfall_list)

# Print every rainfall value by traversing through the set.
# rainfall_data = {120, 150, 180, 120, 90, 110, 130}
# for i in rainfall_data:
#     print(i)

# Remove the value 120 from the above set.
# rainfall_data = {120, 150, 180, 120, 90, 110, 130}
# rainfall_data.remove(120)
# print(rainfall_data)


# Add the value 110 to the above set and observe if any changes happen ? Why does 110 not appear twice ?
# rainfall_data = {120, 150, 180, 120, 90, 110, 130}
# rainfall_data.add(110)
# print(rainfall_data)


# Joining Multiple Sets
# Given:
# rainfall_chennai = {120, 140, 160, 180}
# rainfall_madurai = {110, 130, 150, 180}
# rainfall_coimbatore = {100, 120, 180, 200}
# The Rainfall data starts from Monday to Thursday here, if added more data, it will be considered as the next day in the week.
# Print all unique rainfall measurements for Chennai and Madurai.
# rainfall_chennai = {120, 140, 160, 180}
# rainfall_madurai = {110, 130, 150, 180}
# unique_chennai_madurai=rainfall_chennai.union(rainfall_madurai)
# print(unique_chennai_madurai)


# Merge all three readings into a new set using both the update() and union() methods.
# rainfall_chennai = {120, 140, 160, 180}
# rainfall_madurai = {110, 130, 150, 180}
# rainfall_coimbatore = {100, 120, 180, 200}
# all_rainfall=rainfall_chennai.union(rainfall_madurai,rainfall_coimbatore)
# print(all_rainfall)


# Common Rainfall: Identify rainfall values present in all three cities.
# rainfall_chennai = {120, 140, 160, 180}
# rainfall_madurai = {110, 130, 150, 180}
# rainfall_coimbatore = {100, 120, 180, 200}
# merge=set(rainfall_chennai)
# merge.update(rainfall_madurai)
# merge.update(rainfall_coimbatore)
# print(merge)


# Unique Chennai Rainfall: Determine rainfall values observed exclusively in Chennai.
# rainfall_chennai = {120, 140, 160, 180}
# rainfall_madurai = {110, 130, 150, 180}
# rainfall_coimbatore = {100, 120, 180, 200}
# unique=rainfall_chennai & rainfall_madurai & rainfall_coimbatore
# print(unique)


# Rainfall in at least Two Cities: Find rainfall values recorded in a minimum of two cities.
# rainfall_chennai = {120, 140, 160, 180}
# rainfall_madurai = {110, 130, 150, 180}
# rainfall_coimbatore = {100, 120, 180, 200}
# unique=rainfall_chennai-(rainfall_madurai|rainfall_coimbatore)
# print(unique)


# Create a new set where every rainfall value is increased by 10.
# rainfall_chennai = {120, 140, 160, 180}
# rainfall_madurai = {110, 130, 150, 180}
# rainfall_coimbatore = {100, 120, 180, 200}
# increased={value+10 for value in rainfall_chennai}
# print(increased)

# For e.g. if input is {120, 140, 160,180}, then output has to be {130, 150, 170, 190}	


# Other Miscellaneous Methods:
# Delete the rainfall_coimbatore set in python.
# rainfall_chennai = {120, 140, 160, 180}
# rainfall_madurai = {110, 130, 150, 180}
# rainfall_coimbatore = {100, 120, 180, 200}
# del rainfall_coimbatore
# print(rainfall_coimbatore)


# Clear the data inside rainfall_chennai set and make it empty.
rainfall_chennai = {120, 140, 160, 180}
rainfall_madurai = {110, 130, 150, 180}

rainfall_chennai.clear()
print(rainfall_chennai)


