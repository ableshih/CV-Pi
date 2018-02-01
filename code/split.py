str = 'blue, red, green'
print(str)
str.split()
print (str.split( ))
print (str.split(' ', 1) )

a,b,c = str.split()

print(a)
print(b)
print(c)
----------------
blue, red, green
['blue,', 'red,', 'green']
['blue,', 'red, green']
blue,
red,
green
