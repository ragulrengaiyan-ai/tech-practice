# Part 1: Tuples

# Activity 1: Tuples Basics
# Given the tuple: fruits = ("apple", "banana", "cherry", "mango", "banana")

# Address the following:
# Determine the length of the fruits tuple.
# Identify the index of the initial occurrence of "banana".
# Attempt to modify "cherry" to "grape" within the tuple. Explain the outcome and the reason behind it.
# Transform the tuple into a list, make a modification, and then convert it back to a tuple.

# fruits= ("apple", "banana", "cherry", "mango", "banana")
# print(len(fruits))
# print(fruits.index("banana"))
# print(fruits[2]="grapes")
# fruits_list=list(fruits)
# fruits_list[2]="grape"
# fruits=tuple(fruits_list)
# print(fruits)


# Activity 2: Tuples Grouping
# Given the following tuples:
# colors = ("red", "green", "blue")
# shapes = ("circle", "square", "triangle")
# Perform the following operations:
# Combine colors and shapes to create a new tuple called art.
# Demonstrate how to repeat a tuple, specifically colors three times.
# Extract and print the middle element from the art tuple using slicing.
# Verify if the string "square" exists within the art tuple.

# colors = ("red", "green", "blue")
# shapes = ("circle", "square", "triangle")
# art=colors+shapes
# print(art)
# repeated_color=colors*3
# print(repeated_color)
# middle_index1=len(art)//2-1
# middle_index2=len(art)//2
# middle_element=art[middle_index1:middle_index2+1]
# print(middle_element)
# print("square" in art)



# Activity 3: Tuple Operations

# Given the following list of student marks:

# marks = (78, 85, 69, 90, 85)

# Perform the following operations:
# Determine the highest and lowest marks.
# Count the occurrences of the mark 85.
# Calculate the average marks using the sum() and len() functions.

# marks = (78, 85, 69, 90, 85)
# highest=max(marks)
# lowest=min(marks)
# print(highest)
# print(lowest)
# counts=marks.count(85)
# print(counts)
# average=sum(marks)/len(marks)
# print(average)


# Activity 4: Rainfall Data:

# The monthly_rainfall tuple provides the rainfall in millimeters for each month from January to December:

# monthly_rainfall = (120, 150, 120, 180, 120, 90, 110, 130, 100, 140, 120, 160)

# Calculate the total annual rainfall.
# Determine the average monthly rainfall.
# Identify the month(s) with exactly 120 mm of rainfall. (Hint: Consider using enumerate() or .count().)
# Find the highest and lowest rainfall values recorded.

# monthly_rainfall = (120, 150, 120, 180, 120, 90, 110, 130, 100, 140, 120, 160)
# total=sum(monthly_rainfall)
# print(total)
# average_rainfall=total/len(monthly_rainfall)
# print(average_rainfall)
# months_with_120mm=[]
# for index, value in enumerate(monthly_rainfall):
#     if value==120:
#         months_with_120mm.append(index+1)
# print(months_with_120mm)
# highest=max(monthly_rainfall)
# lowest=min(monthly_rainfall)
# print(highest)
# print(lowest)