my_expenses = {
    "January": 2200,
    "February": 2350,
    "March": 2600,
    "April": 2130,
    "May": 2190
}

# 1. In February, how many dollars did you spend extra compared to January?
difference_between_deb_jan = my_expenses["February"] - my_expenses["January"]
print(difference_between_deb_jan)

# 2. Find out your total expense for the first quarter (first three months) of the year.
quarter_total = my_expenses["January"] + my_expenses["February"] + my_expenses["March"]
print(quarter_total)

expenses = 0
count = 0
for month in my_expenses:
    expenses += my_expenses[month]
    count +=1
    if count == 2:
        break
print(expenses)

# 3. Find out if you spent exactly 2000 dollars in any month
for month in my_expenses:
    if my_expenses[month] == 2000:
        print("Yes, spent 2000 in ", month)
        break
else:
    print("No month with exactly 2000 dollars")

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
my_expenses["June"] = 1900
print(my_expenses)

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

my_expenses["April"] -= 200
print(my_expenses["April"])

