# Problem 2 Solution

# Surveyed data 
locality_data = {'Name' : ['Abhinav','Sohail','Dheeraj','Rashmi','Vaishali'],
                  'Age' : [42,29,35,28,32],
                  'Sex' : ['Male', 'Male','Male','Female','Female'] , 
                  'Height' : [172,175,170,168,170],
                  'Weight' : [70,82,60,55,64]
                 }

# Calculate the mean height and print it

height = [172,175,170,168,170]
len_heigh = len(height)
print(len_heigh)
sum_height = sum(height)
print(sum_height)

mean_height = (sum_height / len_heigh)
print(mean_height)

# Calculate the median height and print it

sorted_height = sorted(height)
print(sorted_height)

if len_heigh % 2 == 0:
    median1 = height[len_heigh//2]
    median2 = height[len_heigh//2 - 1]
    median = (median1 + median2) / 2
else:
    median = height[len_heigh//2]

print(median)

# Calculate the mean weight and print it

weight =  [70,82,60,55,64]
len_weight = len(weight)
print(len_weight)
sum_weight = sum(weight)
print(sum_weight)

mean_weight = (sum_weight / len_weight)
print(mean_weight)

# Calculate the median weight and print it

sorted_weight = sorted(weight)
print(sorted_weight)

if len_weight % 2 == 0:
    median1 = weight[len_weight//2]
    median2 = weight[len_weight//2 - 1]
    median = (median1 + median2) / 2
else:
    median = weight[len_weight//2]

print(median)

# Python code to print the first three elements for the key 'Age'

name = ['Abhinav','Sohail','Dheeraj','Rashmi','Vaishali']
age = [42,29,35,28,32]

age_key = list(zip(name,age))
print(age_key)

key_value = dict(age_key)
print(key_value)

a = key_value.pop('Vaishali')
print(key_value)

b = key_value.pop('Rashmi')
print(key_value)