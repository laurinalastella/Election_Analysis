counties = ["Arapahoe","Denver","Jefferson"]

for county in counties:
    print(county)

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)


for num in range(5):
    print(num)


for i in range(len(counties)):
    print(counties[i])


for i in range(len(counties_dict)):
    print(counties_dict[i])






# Dictionaries
###When iterating over a dictionary:

### The first variable declared in the for loop 
# is assigned to the keys.
### The second variable is assigned to the values.

# KEY:VALUE
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}


for county in counties_dict:
    print(county)

### When using the keys() method, it doesn't 
# matter what variable name we use in the for loop. 
# The keys() method will print each key in order.
for county in counties_dict.keys():
    print(county)


for county in counties_dict:
    print(counties_dict[county])

### Another method we can use to get the values of a key 
# is to use the get() method on the dictionary in the for loop.
for county in counties_dict:
    print(counties_dict.get(county))

### Finally, if we want to print the key-value pair 
# of the dictionary, we use the items() method 
# in the for loop, which follows this general format:

for county, voters in counties_dict.items():
    print(county, voters)

# Skill Drill
for county, voters in counties_dict.items():
    print(
        county + " county has " + str(voters) + " voters."
        )


voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)






for county_dict in voting_data:
    for value in county_dict.values():
        print(value)




### To retrieve only the values from each 
# dictionary in the list of dictionaries, 
# we need to use a nested for loop. 
# Let's see how this can be done with our voting_data.
### First, use the for loop: 
# for county_dict in voting_data: 
# to retrieve each dictionary. 
# Then, in the second for loop, 
# use the values() method on the variable 
# county_dict to reference the data in 
# the second for loop in order to get each value.

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)


### How would you retrieve the number of registered voters 
# from each dictionary?
for county_dict in voting_data:

     print(county_dict['registered_voters'])

     print(county_dict['county'])



### If we only want to print the county name from each dictionary, 
# we can use county_dict['county'] in the print statement 
# for the for loop.
for county_dict in voting_data:
    print(county_dict['county'])





### 3.2.11
### The general format for f-strings is as follows:
### The f-string begins with an f followed by a string contained within quotes. (The term f-string comes from the leading "f" character preceding the string literal.)
### In the f-string, curly braces are used to add variables or expressions to the f-string.

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")



for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)


### The general format for a number to format it in an f-string is as follows:
### f'{value:{width}.{precision}}'
### In the format, the width specifies the number of characters used to display the value. However, if a value needs more space than the width specifies, the additional space is used.
### The precision indicates the number of decimal places to format the value. For example, to format the interest to two decimal places, we would use .2f, where f means "floating-point decimal format".
### When formatting a number, we can also add a thousands separator with a comma, using the following format. The comma is placed after the {width}.
### f'{value:{width},.{precision}}'

message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)




counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
# !!!!!!!!!!! Failed to get final 3.2.11 Skill Drill working:
#Refer to the following dictionary to complete the activity.
#voting_data = [``{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
#Print each county and registered voter from the dictionary. The output should look like the following:
#Each county and its registered voters have printed out in the
#following format:Arapahoe County has 422,829 registered voters. Denver
#County has 463,353 registered voters.Jefferson County has 432,438
#registered
#voters.








