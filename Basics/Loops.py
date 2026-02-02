# For loop

# Iteration over a list
fruits = ["apple", "orange", "mango", "banana"]
for fruit in fruits:
    print(fruit)
    # Fruits: Iterable they implement __iter__().
    # Fruit: Iterator implements both __iter__() and __next__().

# Iteration over a range
for i in range(10):
    if i % 2 == 0:
        print(f"{i} is even")

# While loop
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1

# Loop using len()
for i in range(len(fruits)):
    print(f"Fruit at index {i} is {fruits[i]}")

# if-else  in loop
for fruit in fruits:
    if fruit == "orange":
        print("Found an orange!")
    else:
        print("Found a mango!")