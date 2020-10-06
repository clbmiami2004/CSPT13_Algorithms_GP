'''
We'll say that a positive int divides itself if every digit in the number 
divides into the number evenly

'''
# Problem is located here: https://codingbat.com/prob/p165941
# Understand:

# SHOULD WE DEAL WITH NON NUMERIC VALUES? leave up to engineer
# how should we handle decimal values? we should take int
# what should this function return? True or False?

# Plan:

# Loop through the digits in the number
# use % to get the righmost digit
# use / to discard the righmost digit
# if dividing by the single digit leaves a remainder, then return false
# if the digit is zero, then return false

# if the look exits without returning false, then return true

# Todo: finish this problem and solve it.
def divides_self(num):
    # set a temp variable to hold the number
    value = num
    # Loop over the digits in the number
    # check if the num mod is zero
    if num % 10 == 0:
        return False
    # while the value is not zero
    while num != 0:
        # check if our value moded against our num modded against 10 is not zero
        if value % (num % 10) != 0:
            # return false
            return False
        # divide our value by 10 to make sure we do not get an infinite loop
        value /= 10
    # return true if we get to this point.
    return True

print(divides_self(128)) # True
print(divides_self(12)) # True
print(divides_self(120)) # False
