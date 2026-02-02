heros=['spider man','thor','hulk','iron man','captain america']

#1.  Length of the list
print(len(heros))

#2. Add 'black panther' at the end of this list
heros.append('black panther')
print(heros)

#3. You realize that you need to add 'black panther' after 'hulk', so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
print(heros)
heros.insert(3, 'black panther')
print(heros)

#4. Now you don't like thor and hulk because they get angry easily :), So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool). Do that with one line of code.
# Normal method
heros.remove('thor')
heros.remove('hulk')
heros.insert(1, 'doctor strange')
print(heros)

# One line code
# slicing to replace
# 1 included
# 3 excluded
heros[1:3] = ['doctor strange']
print(heros)

# Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
print(dir(heros))
heros.sort()
print(heros)