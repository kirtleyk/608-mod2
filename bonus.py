""" 
Use your new skills to create a new file named bonus.py that calculates the 
count, sum, mean, median, and mode for a new set of data with at least 100 or 
more data points) and display an additional screen shot after executing your 
program. Make sure the output is clearly labeled and useful. 
"""
import statistics
from random import randint


values = list()  #create values list
for n in range(101): #create 101 random numbers between 1-1000 and add to the list 
    values.append(randint(1, 1000))
    
values = sorted(values) #sort values for easier viewing

valuesCount = len(values)
sumTotal = sum(values)
meanValue = statistics.mean(values)
medianValue = statistics.median(values)
modeValue = statistics.mode(values)

print(f'Values: {values}', '\n')
print(f'Count: {valuesCount}')
print(f'Sum: {sumTotal}')
print(f'Mean: {meanValue}') 
print(f'Median: {medianValue}') 
print(f'Mode: {modeValue}')