# importance - we can see this type of pattern used in nature
# 0 1 1 2 3 5 8 13
# Basically in this series, last 2 numbers are added to print the next number

x, y = 0, 1
print(x)

while y < 50:
    print(y)
    x, y = y, x+y
# here assigning 2 variables simultaneously gives the values to both of them

# x = y
# y = x+y
# if we use this, as already x value has been changed, the output will not be correct and y value will be as below
# y = y+y or 2y, hence we use this
